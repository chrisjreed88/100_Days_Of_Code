import requests
import html


def question_data(num_questions, difficulty):
    url = f"https://opentdb.com/api.php?amount={num_questions}&category=9&difficulty={difficulty}&type=boolean"
    request = requests.request("GET", url)
    results = request.json()["results"]
    for n, question in enumerate(results):
        results[n]["question"] = html.unescape(question["question"])
    return results
