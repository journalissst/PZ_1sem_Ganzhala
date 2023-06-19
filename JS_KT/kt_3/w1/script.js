function printInfo(){
    let figure = document.getElementById('figure').value
    let color = document.getElementById('color').value

    let message = 'Мне нравится фигура ' + figure + '.\nЦвета: ' + color + '\nДлина фигуры: ' + figure.length
    alert(message)
}