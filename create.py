
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")
        confirm_password = request.form.get("confirm_password", "")

        # Check empty fields
        if not username or not password or not confirm_password:
            flash("Please fill in all fields.")
            return redirect(url_for("register"))

        # Check password length
        if len(password) < 8:
            flash("Password must be at least 8 characters.")
            return redirect(url_for("register"))

        # Check password confirmation
        if password != confirm_password:
            flash("Passwords do not match.")
            return redirect(url_for("register"))

        # Hash password
        hashed_password = generate_password_hash(password)

        conn = get_db()

        try:
            conn.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                (username, hashed_password)
            )

            conn.commit()

            flash("Account created successfully!")
            return redirect(url_for("login"))

        except sqlite3.IntegrityError:
            flash("Username already exists.")

        finally:
            conn.close()

    return render_template("register.html")
