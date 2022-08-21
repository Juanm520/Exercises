<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Method POST and GET</title>
</head>
<body>
    <h1>Method GET</h1>
    <form action="./server.php" method="get">

        <label for="name">Enter your fullname</label>
        <input type="text" name="name" id="name">

        <label for="age">Enter your age</label>
        <input type="text" name="age" id="age">

        <button type="submit">Submit Form</button>
    </form>

    <h1>Method POST</h1>
    <form action="./server.php" method="post">

    <label for="name">Enter your fullname</label>
        <input type="text" name="name" id="name">

        <label for="age">Enter your age</label>
        <input type="text" name="age" id="age">

        <button type="submit">Submit Form</button>

    </form>


</body>
</html>