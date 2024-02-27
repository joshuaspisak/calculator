# calculator

# Microservice
How to Request Data

- Endpoint: /generate
- Method: GET
- Query Parameters:
  - difficulty: String (optional, default=easy). Accepted values: easy, medium, hard.
- Example Call:
  - Python example using the requests library to fetch an easy Sudoku puzzle:
```python
import requests

# Example URL, replace with actual deployed service URL if different
BASE_URL = "http://localhost:5111"
response = requests.get(f"{BASE_URL}/generate", params={'difficulty': 'easy'})
if response.status_code == 200:
    puzzle_data = response.json()
    print(puzzle_data)
else:
    print("Error fetching puzzle:", response.status_code)
```
How to Receive Data
- Response Format: JSON
- Response Example for an easy puzzle:
```json
{
  "puzzle": "81..7346.5264391836.8197.5613..8574829..5631547..68.243.961287.7.354..9.9678245.",
  "difficulty": "easy"
}
```
![Microservice UML](https://github.com/joshuaspisak/calculator/assets/137116926/ae1d58a5-9398-47a5-b110-ea8d92bdae60)
