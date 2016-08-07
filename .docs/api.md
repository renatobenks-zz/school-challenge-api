# Specifications API Rest

_The API Data are from own API._
 
##  1. ENDPOINTS:
### Issues:
- Issues about themes for user choice: `localhost:5000/api/v1/issues`. [Issues](localhost:5000/api/v1/issues) 
- Specific issue: `localhost:5000/api/v1/issue/<id>`. [Issue](localhost:5000/api/v1/issue/1)

### Questions:
- Questions about issues for preference user: `localhost:5000/api/v1/questions`. [Questions](localhost:5000/api/v1/questions) 
- Specific question: `localhost:5000/api/v1/question/<id>`. [Question](localhost:5000/api/v1/question/1)

### Words:
- Word ramdomly generated according to the user's choice: `POST`, `localhost:5000/api/v1/word`.
- Format request: 
```json
    {
        "id_question": <id_question>,
        "id_issue": <id_issue>
    }
```

- This request will have a response. Look like this:

    ```json
    {
        "word": {
            "characters": 18,
            "id": 3,
            "issues_id_issue": 1,
            "questions_id_question": 2,
            "word": "pizza de chocolate"
        }
    }
    ```

### Response Word:
_The ideal is to be done the request for this ENDPOINT, foreach change in input user try to hit the letter_

- Return if letter try is right according to letters in word: `POST`, `localhost:5000/api/v1/word-response`
- Format for request:
```json
    {
        "word": <word>,
        "letter": <letter>
    }
```

- This request will have a response. Look like this:

    ```json
    {
        "response": {
            "isValid": False,
            "quantity": 0
        }
    }
    ```
    
    
Full developed for: Renato Benkendorf