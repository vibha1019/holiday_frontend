---
layout: post
title: Snake Game
search_exclude: true
hide: true
menu: nav/home.html
---

<style>
    /* Prevent scrolling on the body */
    html, body {
        height: 100%;
        margin: 0;
        overflow: hidden;
        font-family: 'Roboto', sans-serif;
        background: linear-gradient(45deg, #121212, #0c0c0c);
    }

    body {
        color: #ffffff;
    }

    .wrap {
        margin-left: auto;
        margin-right: auto;
        max-width: 320px;
    }

    canvas {
        display: block;
        margin: 0 auto;
        border-style: solid;
        border-width: 5px;
        border-color: #00FF00;
        box-shadow: 0 0 20px lime;
    }

    canvas:focus {
        outline: none;
    }

    h2 {
        text-align: center;
        color: #fff;
        font-size: 3em;
        text-shadow: 0 0 20px lime;
        margin-top: 20px;
    }

    .container {
        text-align: center;
        padding: 20px;
    }

    header {
        font-size: 1.5em;
        margin-bottom: 20px;
        text-align: center;
        color: #00FF00;
        text-shadow: 0 0 10px lime;
    }

    .link-alert {
        color: #00FF00;
        text-decoration: none;
        font-size: 1.2em;
        padding: 10px 20px;
        margin: 10px;
        border: 2px solid #00FF00;
        border-radius: 5px;
        transition: all 0.3s ease-in-out;
    }

    .link-alert:hover {
        background-color: #00FF00;
        color: #121212;
        box-shadow: 0 0 10px lime;
    }

    .modal-content {
        background-color: #121212;
        color: #fff;
        border: 3px solid #00FF00;
        width: 40%;
        margin: auto;
        padding: 30px;
        font-size: 24px;
        box-shadow: 0 0 20px lime;
        border-radius: 10px;
        text-align: center;
    }

    .modal-content .score {
        font-size: 36px;
        font-weight: bold;
        color: lime;
    }

    .modal-content p {
        font-size: 20px;
    }

    .close {
        color: #aaa;
        font-size: 28px;
        font-weight: bold;
    }

    .close:hover,
    .close:focus {
        color: #fff;
        text-decoration: none;
        cursor: pointer;
    }

    #menu, #gameover, #setting {
        transition: opacity 0.3s ease;
    }

    /* Neon glow effect for interactive elements */
    .link-alert:hover,
    #new_game:hover,
    #new_game1:hover,
    #new_game2:hover {
        color: #00FF00;
        text-shadow: 0 0 15px lime, 0 0 10px lime;
    }

    /* Add transition effect for screens */
    #menu, #gameover, #setting {
        opacity: 0;
        display: none;
        transition: opacity 0.3s ease-in-out;
    }

    #menu.active, #gameover.active, #setting.active {
        opacity: 1;
        display: block;
    }

    /* Customize game over screen */
    #gameover p {
        font-size: 1.5em;
        text-shadow: 0 0 10px lime;
    }

    #setting input[type="radio"] {
        margin-right: 10px;
    }

    #setting label {
        cursor: pointer;
        font-size: 1.1em;
        color: #00FF00;
        padding: 5px;
        transition: color 0.3s ease;
    }

    #setting label:hover {
        color: lime;
    }

    #setting input[type="radio"]:checked + label {
        background-color: #00FF00;
        color: #121212;
    }

</style>

<h2>Snake</h2>
<div class="container">
    <header class="pb-3 mb-4 border-bottom border-primary text-dark">
        <p class="fs-4">Score: <span id="score_value">0</span></p>
    </header>
    <div class="container bg-secondary" style="text-align:center;">
        <!-- Main Menu -->
        <div id="menu" class="py-4 text-light">
            <p>Welcome to Snake, press <span style="background-color: #FFFFFF; color: #000000">space</span> to begin</p>
            <a id="new_game" class="link-alert">new game</a>
            <a id="setting_menu" class="link-alert">settings</a>
        </div>
        <!-- Game Over -->
        <div id="gameover" class="py-4 text-light">
            <p>Game Over, press <span style="background-color: #FFFFFF; color: #000000">space</span> to try again</p>
            <a id="new_game1" class="link-alert">new game</a>
            <a id="setting_menu1" class="link-alert">settings</a>
        </div>
        <!-- Play Screen -->
        <canvas id="snake" class="wrap" width="320" height="320" tabindex="1"></canvas>
        <!-- Settings Screen -->
        <div id="setting" class="py-4 text-light">
            <p>Settings Screen, press <span style="background-color: #FFFFFF; color: #000000">space</span> to go back to playing</p>
            <a id="new_game2" class="link-alert">new game</a>
            <br>
            <p>Speed:
                <input id="speed1" type="radio" name="speed" value="120" checked/>
                <label for="speed1">Slow</label>
                <input id="speed2" type="radio" name="speed" value="75"/>
                <label for="speed2">Normal</label>
                <input id="speed3" type="radio" name="speed" value="35"/>
                <label for="speed3">Fast</label>
            </p>
            <p>Wall:
                <input id="wallon" type="radio" name="wall" value="1" checked/>
                <label for="wallon">On</label>
                <input id="walloff" type="radio" name="wall" value="0"/>
                <label for="walloff">Off</label>
            </p>
        </div>
    </div>
</div>

<!-- Modal for score display -->
<div id="scoreModal" class="modal">
    <div class="modal-content">
        <span class="close">&times;</span>
        <p>Your final score:</p>
        <p class="score" id="finalScore"></p>
    </div>
</div>

<script>
    (function(){
        /* Attributes of Game */
        /////////////////////////////////////////////////////////////
        // Canvas & Context
        const canvas = document.getElementById("snake");
        const ctx = canvas.getContext("2d");
        // HTML Game IDs
        const SCREEN_SNAKE = 0;
        const screen_snake = document.getElementById("snake");
        const ele_score = document.getElementById("score_value");
        const speed_setting = document.getElementsByName("speed");
        const wall_setting = document.getElementsByName("wall");
        // HTML Screen IDs (div)
        const SCREEN_MENU = -1, SCREEN_GAME_OVER = 1, SCREEN_SETTING = 2;
        const screen_menu = document.getElementById("menu");
        const screen_game_over = document.getElementById("gameover");
        const screen_setting = document.getElementById("setting");
        // HTML Event IDs (a tags)
        const button_new_game = document.getElementById("new_game");
        const button_new_game1 = document.getElementById("new_game1");
        const button_new_game2 = document.getElementById("new_game2");
        const button_setting_menu = document.getElementById("setting_menu");
        const button_setting_menu1 = document.getElementById("setting_menu1");
        // Game Control
        const BLOCK = 10;   // size of block rendering
        let SCREEN = SCREEN_MENU;
        let snake;
        let snake_dir;
        let snake_next_dir;
        let snake_speed;
        let food = {x: 0, y: 0};
        let score;
        let wall;
        /* Display Control */
        /////////////////////////////////////////////////////////////
        // 0 for the game
        // 1 for the main menu
        // 2 for the settings screen
        // 3 for the game over screen
        let showScreen = function(screen_opt){
            SCREEN = screen_opt;
            switch(screen_opt){
                case SCREEN_SNAKE:
                    screen_snake.style.display = "block";
                    screen_menu.style.display = "none";
                    screen_setting.style.display = "none";
                    screen_game_over.style.display = "none";
                    break;
                case SCREEN_GAME_OVER:
                    screen_snake.style.display = "none";
                    screen_menu.style.display = "none";
                    screen_setting.style.display = "none";
                    screen_game_over.style.display = "block";
                    displayModal();
                    break;
                case SCREEN_SETTING:
                    screen_snake.style.display = "none";
                    screen_menu.style.display = "none";
                    screen_setting.style.display = "block";
                    screen_game_over.style.display = "none";
                    break;
            }
        }

        const modal = document.getElementById("scoreModal");
        const closeModal = document.getElementsByClassName("close")[0];

        function displayModal() {
            document.getElementById("finalScore").textContent = score;
            modal.style.display = "block";
        }

        closeModal.onclick = function() {
            modal.style.display = "none";
            newGame();
        }

        window.onclick = function(event) {
            if (event.target === modal) {
                modal.style.display = "none";
                newGame();
            }
        }

        /* Actions and Events  */
        /////////////////////////////////////////////////////////////
        window.onload = function(){
            // HTML Events to Functions
            button_new_game.onclick = function(){newGame();};
            button_new_game1.onclick = function(){newGame();};
            button_new_game2.onclick = function(){newGame();};
            button_setting_menu.onclick = function(){showScreen(SCREEN_SETTING);};
            button_setting_menu1.onclick = function(){showScreen(SCREEN_SETTING);};
            // Keyboard Control
            document.onkeydown = function(event){
                let dir_key = event.keyCode || event.which;
                if(dir_key == 37 && snake_dir != "RIGHT"){snake_next_dir = "LEFT";}
                else if(dir_key == 38 && snake_dir != "DOWN"){snake_next_dir = "UP";}
                else if(dir_key == 39 && snake_dir != "LEFT"){snake_next_dir = "RIGHT";}
                else if(dir_key == 40 && snake_dir != "UP"){snake_next_dir = "DOWN";}
            }
            newGame();
        }

        /* Game Logic */
        /////////////////////////////////////////////////////////////
        function newGame(){
            score = 0;
            ele_score.innerHTML = score;
            snake = [{x: 5, y: 5}];
            snake_dir = "RIGHT";
            snake_next_dir = snake_dir;
            snake_speed = 120;
            food.x = 10;
            food.y = 10;
            wall = true;
            showScreen(SCREEN_SNAKE);
            startGame();
        }

        function startGame(){
            let gameInterval = setInterval(function(){
                moveSnake();
                if(checkGameOver()){clearInterval(gameInterval); showScreen(SCREEN_GAME_OVER);}
                drawGame();
            }, snake_speed);
        }

        function moveSnake(){
            let head = snake[0];
            let newHead = {x: head.x, y: head.y};
            switch(snake_next_dir){
                case "UP": newHead.y--; break;
                case "DOWN": newHead.y++; break;
                case "LEFT": newHead.x--; break;
                case "RIGHT": newHead.x++; break;
            }
            snake.unshift(newHead);
            if(snake[0].x === food.x && snake[0].y === food.y){
                score++;
                ele_score.innerHTML = score;
                food.x = Math.floor(Math.random() * 32);
                food.y = Math.floor(Math.random() * 32);
            } else {
                snake.pop();
            }
            snake_dir = snake_next_dir;
        }

        function checkGameOver(){
            let head = snake[0];
            if(head.x < 0 || head.x >= 32 || head.y < 0 || head.y >= 32){return true;}
            for(let i = 1; i < snake.length; i++){
                if(snake[i].x === head.x && snake[i].y === head.y){return true;}
            }
            return false;
        }

        function drawGame(){
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            // Draw Snake
            for(let i = 0; i < snake.length; i++){
                ctx.fillStyle = i === 0 ? "#00FF00" : "#008000";
                ctx.fillRect(snake[i].x * BLOCK, snake[i].y * BLOCK, BLOCK, BLOCK);
            }
            // Draw Food
            ctx.fillStyle = "#FF0000";
            ctx.fillRect(food.x * BLOCK, food.y * BLOCK, BLOCK, BLOCK);
        }
    })();
</script>
