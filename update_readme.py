import datetime
import requests
from textwrap import dedent

USERNAME = "0prescu"
BIRTHDAY = datetime.date(2008, 6, 30)

def get_github_stats(username):
    headers = {"Accept": "application/vnd.github.v3+json"}
    user = requests.get(f"https://api.github.com/users/{username}", headers=headers).json()
    repos = requests.get(f"https://api.github.com/users/{username}/repos?per_page=100", headers=headers).json()

    total_stars = sum(r.get("stargazers_count", 0) for r in repos)
    followers = user.get("followers", 0)
    public_repos = user.get("public_repos", 0)
    commits = 0  # Optional: use GitHub GraphQL for real commits
    return public_repos, total_stars, followers, commits

def calculate_uptime(birthday):
    today = datetime.date.today()
    delta = today - birthday
    years = delta.days // 365
    months = (delta.days % 365) // 30
    days = (delta.days % 365) % 30
    return f"{years} years, {months} months, {days} days"

def create_readme(stats, uptime):
    repos, stars, followers, commits = stats
    content = dedent(f"""
    ```
                         &&                   christian@oprescu ————————————————————————————————————————————
                    &&&&&&&&&&&&              . OS: ...................................... Windows 11, Linux
              &&&&&&&&&&&&&&&&&&&&&           . Uptime: ......................... {uptime}
              &&&&&&&&&&&&&&&&&&&&&&&$        . Host: ......................................................
            &&&&&&&&&&&&&&&&&&&&&&&&&&        . Kernel: ....................................................
           &&&&&&&&&&&&&&&&&&&&&&&&&&&&       . IDE: ............................./.................. VSCode
          &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&      
          &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&      . Languages.Programming: ... Java, Python, JavaScript, C++, C#
          &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&      . Languages.Computer: .................. HTML, CSS, JSON, YAML
           &&&&&&&&&&;x&&&&&&&&&&&&&&&&&      . Languages.Real: .................................... English
             &&&&&X+;;xx+X&&&&&&&&&&&&&&      
              $$&&&$:.:;+x$$$XX$$&&&&&&       . Hobbies.Software: ..........................................
              ++$&&&&x;;+X$$$XX$&&&&&         . Hobbies.Hardware: ..........................................
              ;;::::;;..x$&&&X$Xx$&$X        
              +;::..:: :+;;;;:;;xxxx          - Contact ————————————————————————————————————————————————————
               ;;..:;..;+;:.::;xX             . Email.Personal: ............ oprescu.christian.adi@gmail.com
               +;:::;..;x+:::;+xX             . Email.Work: ............. Developer.Christian@protonmail.com
                +++;;+xXX;::;+x$              . LinkedIn: ..................................................
                 x++++xxx+;;;xX&&&            . Discord: ........................................... iackaso
              :. :+++xXXx++xXXXXx:  .         
          :...  .;+XX+++xXXXxxx+.      .      - GitHub Stats ——————————————————————————————————————————————— 
        :..     :+;+xXX$$XXX+;.         .     . Repos: .... {repos} | Stars: ......... {stars}
        .       .;;:::+Xxx+:.            .    . Followers: ...... {followers} | Commits: .... {commits}
       :..    .  .::..:;::               :    . Lines of Code on GitHub:. 446,276 ( 523,178++, 76,902-- ) 
    ```
    """)
    return content

if __name__ == "__main__":
    stats = get_github_stats(USERNAME)
    uptime = calculate_uptime(BIRTHDAY)
    readme_content = create_readme(stats, uptime)
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)
