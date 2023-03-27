package com.vdorofeev.apiclient.controller;

import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

import java.io.FileReader;
import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Scanner;

@RestController
@RequestMapping
public class RequestController {

    @Value("${arg}")
    private String myProperty;

    @PostMapping("checkcode")
    public ResponseEntity<String> getResponce(@RequestParam("file") MultipartFile file) throws ParseException {
        try {
            String savePath = "/tmp/filetocheck.java";
            Path path = Paths.get(savePath);
            file.transferTo(path);
            return ResponseEntity.ok(executePython(savePath));
        } catch (IOException e) {
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body("Failed to upload file");
        }
    }

    @GetMapping("ping")
    public String checkAlive() throws IOException, ParseException {
        return executePython("ping");
    }

    private String executePython(String argument) throws IOException, ParseException {
        String pathToConfig = this.myProperty;
        Object obj = new JSONParser().parse(new FileReader(pathToConfig));
        JSONObject jsonObject = (JSONObject) obj;
        String pathToPythonScript = (String) jsonObject.get("pathToPythonScript");
        String pathToIndexes = (String) jsonObject.get("pathToIndexes");

        ProcessBuilder builder = new ProcessBuilder("python3",
                pathToPythonScript, argument, pathToIndexes);
        Process process = builder.start();

        Scanner output = new Scanner(process.getInputStream()).useDelimiter("\\A");
        Scanner errors = new Scanner(process.getErrorStream()).useDelimiter("\\A");
        String result_err = errors.hasNext() ? errors.next() : "";
        String result = output.hasNext() ? output.next() : "";
        return result + result_err;
    }
}

