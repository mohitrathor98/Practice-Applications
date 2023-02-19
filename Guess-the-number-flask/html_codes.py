header = """
<!DOCTYPE html>
<html style="background-color: #86A3B8;">
  <head>
    <title>Guess the Number!</title>
  </head>
"""

footer= """
</body>
</html>
"""

validate_input = """
<script>
    function validateForm() {
        var field = document.forms["inputForm"]["user_choice"].value;
        var regex = /^\d+$/;
        if (!regex.test(field)) {
            alert("Please provide integer values between 0 and 9!")
        }
    }
</script>
"""

input_form = """
<form name="inputForm" onsubmit="return validateForm()" action="/submit-form" method="post">
    <label for="text-box">Enter you input here: </label>
    <input type="text" id="user_choice" name="choice-field">
    <input type="submit" value="Submit">
</form>
"""

landing_body = header + """
<body>
<h1 >Guess the number between 0 and 9!!</h1>
<iframe src="https://giphy.com/embed/fDUOY00YvlhvtvJIVm" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
<br>
""" + input_form + validate_input + footer


