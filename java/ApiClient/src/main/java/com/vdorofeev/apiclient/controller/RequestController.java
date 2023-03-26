package com.vdorofeev.apiclient.controller;

import org.springframework.web.bind.annotation.*;

import java.io.IOException;
import java.util.Scanner;

@RestController
@RequestMapping
public class RequestController {
    String pathToPythonFile = "/home/vdorofeev/PlagiarismChecker/python/check_code.py";
    @PostMapping("checkcode")
    public String getResponce(@RequestBody String path) throws IOException {
        return executePython(path);
    }

    @GetMapping("ping")
    public String checkAlive() throws IOException {
        return executePython("ping");
    }

    private String executePython(String argument) throws IOException {
        ProcessBuilder builder = new ProcessBuilder("python",
                this.pathToPythonFile, argument);
        Process process = builder.start();
        Scanner output = new Scanner(process.getInputStream()).useDelimiter("\\A");
        Scanner errors = new Scanner(process.getErrorStream()).useDelimiter("\\A");
        String result_err = errors.hasNext() ? errors.next() : "";
        String result = output.hasNext() ? output.next() : "";
        return result + result_err;
    }
}

