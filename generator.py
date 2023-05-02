import io
import sys
import json

if __name__ == "__main__":

    s = io.StringIO()
    with open(sys.argv[1], "r") as f:
        for line in f:
            ln = json.loads(line)
            jline = json.loads(ln)
            name = jline.get("fullname").strip()
            url = jline.get("url").strip()
            description = jline.get("description")
            print("- [%s](%s)" % (name, url), file=s)
            if description is not None:
                print("  - %s" % description.strip(), file=s)

    with open(sys.argv[2], "w") as f:
        f.write("## List\n\n")
        f.write(s.getvalue())
