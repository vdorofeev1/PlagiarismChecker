package com.vdorofeev.apiclient.controller;

import com.vdorofeev.apiclient.components.PythonExecutor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

@RestController
@RequestMapping
public class RequestController {

    private PythonExecutor pythonExecutor;

    @Autowired
    public void setPythonExecutor(PythonExecutor pythonExecutor) {
        this.pythonExecutor = pythonExecutor;
    }

    @PostMapping("checkcode")
    public ResponseEntity<String> getResponce(@RequestParam("file") MultipartFile file) {
        try {
            String savePath = "/tmp/filetocheck.java";
            Path path = Paths.get(savePath);
            file.transferTo(path);
            return ResponseEntity.ok(this.pythonExecutor.execute(savePath));
        } catch (IOException e) {
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body("Failed to upload file");
        }
    }

    @GetMapping("ping")
    public ResponseEntity<String> checkAlive() throws IOException {
        return ResponseEntity.ok(this.pythonExecutor.execute("ping"));
    }

}

