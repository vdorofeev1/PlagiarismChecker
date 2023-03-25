package com.vdorofeev.apiclient.controller;

import org.springframework.web.bind.annotation.*;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.stream.Collectors;

@RestController
@RequestMapping
public class RequestController {
    String pathToPythonFile = "/home/vdorofeev/MyProjects/test_project_for_jb/python/check_code.py";
    @PostMapping("checkcode")
    public String getResponce(@RequestBody String str) throws IOException {
        return checkFile(str);
    }

    @GetMapping("ping")
    public String checkAlive() throws IOException {
        ProcessBuilder builder = new ProcessBuilder("python",
                this.pathToPythonFile, "ping");
        Process process = builder.start();
        BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
        return reader.readLine();
    }

    private String checkFile(String pathToFile) throws IOException {
        ProcessBuilder builder = new ProcessBuilder("python",
                this.pathToPythonFile, pathToFile);
        Process process = builder.start();
        BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
        return reader.readLine();
    }
}

