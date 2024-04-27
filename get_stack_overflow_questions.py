import requests


def get_tag():
    filter_by_tag = input("Do you want to filter by tag? (yes/no) ").lower()
    if filter_by_tag == "yes".lower() or filter_by_tag == "y".lower():
        tag = input("Please enter the tag to search for: ").lower()
        return tag


def get_unanswered():
    unanswered = input("Do you want to filter by unanswered questions? (yes/no) ").lower()
    if unanswered == "yes".lower() or unanswered == "y".lower():
        return True
    return False


def fetch_questions(unanswered, tag):
    url = "https://api.stackexchange.com//2.3/questions?order=desc&sort=activity&site=stackoverflow"
    if tag is not None:
        url += f"&tagged={tag}"
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        return None
    response = response.json()["items"]
    if unanswered:
        response = [q for q in response if q["answer_count"] == 0]
    return response


def print_questions(questions):
    if questions is None:
        return
    for data in questions:
        print()
        print(data["title"])
        print(data["link"])


def main():
    tag = get_tag()
    unanswered = get_unanswered()
    questions = fetch_questions(unanswered, tag)
    print_questions(questions)


if __name__ == "__main__":
    main()
