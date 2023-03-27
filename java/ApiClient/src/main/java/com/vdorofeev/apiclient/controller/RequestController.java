package com.vdorofeev.apiclient.controller;

import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.web.bind.annotation.*;

import java.io.FileReader;
import java.io.IOException;
import java.util.Scanner;

@RestController
@RequestMapping
public class RequestController {

    @Value("${arg}")
    private String myProperty;

    @PostMapping("checkcode")
    public String getResponce(@RequestBody String path) throws IOException, ParseException {
        return executePython(path);
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

        ProcessBuilder builder = new ProcessBuilder("python",
                pathToPythonScript, argument, pathToIndexes);
        Process process = builder.start();

        Scanner output = new Scanner(process.getInputStream()).useDelimiter("\\A");
        Scanner errors = new Scanner(process.getErrorStream()).useDelimiter("\\A");
        String result_err = errors.hasNext() ? errors.next() : "";
        String result = output.hasNext() ? output.next() : "";
        return result + result_err;
    }
}

