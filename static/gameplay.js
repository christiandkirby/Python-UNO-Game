function play_card(index) {
    fetch('/play_card', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({card_index: index})
})
.then(response => response.json())
.then(data => {
    if (data.success) {
        window.location.href = '/gameplay';
    } else {
        alert(data.message);
    }
})}

function draw_card() {
    fetch('/draw_card', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
})
.then(response => response.json())
.then(data => {
    window.location.href = '/gameplay';
})}