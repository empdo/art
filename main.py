from datetime import datetime
import git
date = datetime.now()

repo = git.Repo('')

repo.index.add(['main.py', 'urandom.txt'])

message = """
xxxx xxxx xx   x xxxx    xx   x x   x xxx  xxxx xxxx
 x    x    xx   x x   x   xx   x x   x x  x x    x   
 x    x    x x  x x   x   x x  x x   x x  x x    x   
 xxxx xxx  x xx x x   x   x xx x x   x x  x xxx  xxxx
    x x    x  x x x   x   x  x x x   x x  x x       x
    x x    x   xx x   x   x   xx x   x x  x x       x
 xxxx xxxx x   xx xxxx    x   xx  xxx  xxx  xxxx xxxx
""".strip().splitlines()

for y,line in enumerate(message):
    for x,char in enumerate(line):
        if char == "x":
            for i in range(y+1):
                print(x,y,char)
                with open("urandom.txt", "wb") as file:
                    with open("/dev/urandom", "rb") as random_file:
                        file.write(random_file.read(1000))
                        repo.index.commit('commit', author_date=datetime.strptime(f'2034-{x}-{y}', "%Y-%W-%w").isoformat())
                        repo.remotes.origin.push()


#28dec, måndagen med 1jan i veckan


