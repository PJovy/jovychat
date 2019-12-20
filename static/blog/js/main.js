// Bulma burger navibar js
document.addEventListener('DOMContentLoaded', () => {
    // Get all "navbar-burger" elements
    const $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0);

    // Check if there are any navbar burgers
    if ($navbarBurgers.length > 0) {

        // Add a click event on each of them
        $navbarBurgers.forEach(el => {
            el.addEventListener('click', () => {

                // Get the target from the "data-target" attribute
                const target = el.dataset.target;
                const $target = document.getElementById(target);

                // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
                el.classList.toggle('is-active');
                $target.classList.toggle('is-active');

            });
        });
    }

});

// Ask for ensure when delete an article js
const tiles = document.getElementsByClassName("is-child");
for (let i = 0; i < tiles.length; i++) {
    tiles[i].addEventListener('mouseover', function () {
        this.className += " animated pulse";
    });
    tiles[i].addEventListener('mouseout', function () {
        this.className = this.className.replace(" animated pulse", "");
    });
}


// Bulma upload file js which is used to display the filename.

const fileInput = document.querySelector('#file-js input[type=file]');
fileInput.onchange = () => {
    if (fileInput.files.length > 0) {
        const fileName = document.querySelector('#file-js .file-name');
        fileName.textContent = fileInput.files[0].name;
    }
}

// 删除文章的函数
function confirm_safe_delete() {
    // 调用layer弹窗组件
    layer.open({
        // 弹窗标题
        title: "Confirm delete",
        // 正文
        content: "Confirm to delete this article？",
        // 点击确定按钮后调用的回调函数
        yes: function (index, layero) {
            // 指定应当前往的 url
            $('form#safe_delete button').click();
            layer.close(index)
        },
    })
}

// 返回顶部的js
