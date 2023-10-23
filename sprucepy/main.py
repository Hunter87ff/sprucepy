import flask, os
from flask import Flask, request, render_template

app = Flask("FileShare")


@app.route("/")
def upload():
    return render_template("form.html")



@app.route('/fsend', methods=['POST'])
def upload_file():
    data = request.form.to_dict()
    print(data)
    file = request.files['file']

    fn = os.path.join("D:/github/FileShare/src/files/", file.filename)
    print(fn)
    try:
        with open(fn, "wb") as f:
            f.write(file.read())
    except IOError as e:
        return f"Error saving file: {e}"
    return "<script>alert('uploaded'); window.location.href='/'</script>"
    return "<script>alert('uploaded')</script>"

#os.system("start chrome http://localhost:8787")
app.run(host="0.0.0.0", port=8787, debug=True)
