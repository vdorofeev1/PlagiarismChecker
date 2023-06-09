# PlagiarismChecker

### What is the purpose?
  With the increased popularity of Large Language Models, it becomes crucial for software companies to track the origins of code written by their employees. Using improperly licensed third-party code generated by a language model can lead to significant reputational and financial losses. Code duplication checks against most of the publicly available repositories would avoid these risks and allow detection of problems at earlier stages of the development cycle.
  
### How to use it?
#### Docker
1. Pull docker image \
`docker pull vdorofeev/plagiarism_checker:latest`
2. Run docker container \
`docker run -d -p 8080:8080 vdorofeev/plagiarism_checker` \
You can run this container on any port you like \
2. Check, if you've done everything correctly \
    `curl http://127.0.0.1:8080/ping` \
    Output should be "alive" 
3. Now, you are reardy to check your code \
`curl -X POST -F "file=@/path/to/file" http://127.0.0.1:8080/checkcode"`

#### Running JAR
1. Clone repository to your machine
2. Edit configuration file - `PlagiarismChecker/java/ApiClient/src/main/resources/config.json` 
```
{
  "pathToIndexes": "/home/{$USER}/PlagiarismChecker/python/resources/inverted_indexes", //pass the path to directory with indexes
  "pathToPythonScript": "/home/{$USER}/PlagiarismChecker/python/check_code.py" //pass the path to python script
}
```
3. Run application (openjdk-17 or higher required) \
`java -jar ApiClient-0.0.1-SNAPSHOT.jar --arg=/path/to/config`
4. Check, if you've done everything correctly \
    `curl http://127.0.0.1:8080/ping` \
    Output should be "alive"
5. Now, you are reardy to check your code \
`curl -X POST -F "file=@/path/to/file" http://127.0.0.1:8080/checkcode"`



