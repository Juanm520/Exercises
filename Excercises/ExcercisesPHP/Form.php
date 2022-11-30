<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Method POST and GET</title>
</head>
<body>
        <!-- <h1>Method GET</h1>
    
    <form action="./server.php" method="get">

        <label for="name">Enter your fullname</label>
        <input type="text" name="name" id="name">

        <label for="age">Enter your age</label>
        <input type="text" name="age" id="age">

        <input type="submit" value= "Send form">
        
    </form>

        <h1>Method POST</h1>

    <form action="./server.php" method="post">

        <label for="name_post">Enter your fullname</label>
        <input type="text" name="name_post" id="name_post">

        <label for="age_post">Enter your age</label>
        <input type="text" name="age_post" id="age_post">

        <input type="submit" value= "Send form">

    </form> -->

    <h1>Send Files</h1>

    <form action="./server.php" method="post" enctype="multipart/form-data">

        <label for="name_file">Enter an image name</label>
        <input type="text" name="name_file" id="name_file">

        <label for="image">Choose a file: </label>
        <input type="file" name="image" id="image">

        <button type="submit">Send Image</button>

    </form>


</body>
</html>