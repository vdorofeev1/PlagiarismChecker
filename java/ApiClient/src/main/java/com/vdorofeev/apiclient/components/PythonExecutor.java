package com.vdorofeev.apiclient.components;

import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;

import java.io.FileReader;
import java.io.IOException;
import java.util.Scanner;

@Component
public class PythonExecutor {

    private final String pathToConfig;
    private String pathToPythonScript;
    private String pathToIndexes;

    @Autowired
    public PythonExecutor(@Value("${arg}") String pathToConfig) throws IOException, ParseException {
        this.pathToConfig = pathToConfig;
        this.setPathToScriptAndIndexes();
    }

    private void setPathToScriptAndIndexes() throws IOException, ParseException {
        Object obj = new JSONParser().parse(new FileReader(pathToConfig));
        JSONObject jsonObject = (JSONObject) obj;
        this.pathToPythonScript = (String) jsonObject.get("pathToPythonScript");
        this.pathToIndexes = (String) jsonObject.get("pathToIndexes");
    }

    public String execute(String argument) throws IOException {
        ProcessBuilder builder = new ProcessBuilder("python",
                this.pathToPythonScript, argument, this.pathToIndexes);
        Process process = builder.start();

        Scanner output = new Scanner(process.getInputStream()).useDelimiter("\\A");
        Scanner errors = new Scanner(process.getErrorStream()).useDelimiter("\\A");
        String result_err = errors.hasNext() ? errors.next() : "";
        String result = output.hasNext() ? output.next() : "";
        return result + result_err;
    }

}
