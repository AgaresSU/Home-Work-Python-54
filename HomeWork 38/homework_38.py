import json
import requests


def get_median(numbers):
    numbers = sorted(numbers)
    count = len(numbers)
    middle = count // 2

    if count % 2:
        return numbers[middle]
    return (numbers[middle - 1] + numbers[middle]) / 2


def main():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    posts = json.loads(response.text)

    posts_by_user = {}
    body_lengths = []
    title_lengths = []
    posts_with_length = []

    for post in posts:
        user_id = post["userId"]
        posts_by_user[user_id] = posts_by_user.get(user_id, 0) + 1

        body_lengths.append(len(post["body"]))
        title_lengths.append(len(post["title"]))

        total_length = len(post["title"]) + len(post["body"])
        posts_with_length.append({
            "id": post["id"],
            "userId": user_id,
            "total_length": total_length
        })

    posts_per_user = []
    for user_id, count in sorted(posts_by_user.items()):
        posts_per_user.append({
            "userId": user_id,
            "posts_count": count
        })

    top_longest_posts = sorted(
        posts_with_length,
        key=lambda item: item["total_length"],
        reverse=True
    )[:5]

    top_user = sorted(
        posts_by_user.items(),
        key=lambda item: item[1],
        reverse=True
    )[0]

    report = {
        "generated_at": "2026-06-04T00:00:00Z",
        "source": url,
        "summary": {
            "total_posts": len(posts),
            "avg_body_length": round(sum(body_lengths) / len(body_lengths), 2),
            "most_active_user_id": top_user[0],
            "median_title_length": get_median(title_lengths)
        },
        "posts_per_user": posts_per_user,
        "top_longest_posts": top_longest_posts
    }

    with open("posts_report.json", "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    print("Отчет сохранен в posts_report.json")


if __name__ == "__main__":
    main()
