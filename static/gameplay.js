let pendingCardIndex = null;

function play_card(index, cardName) {
    if (cardName.includes('wild') || cardName.includes('draw_four')) {
        pendingCardIndex = index;
        document.getElementById('color-picker').classList.add('active');
        return;
    }
    
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
    })
}

function selectColor(color) {
    document.getElementById('color-picker').classList.remove('active');
    fetch('/play_card', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({card_index: pendingCardIndex, color: color})
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            window.location.href = '/gameplay';
        } else {
            alert(data.message);
        }
    })
}

function draw_card() {
    fetch('/draw_card', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
    })
    .then(response => response.json())
    .then(data => {
        window.location.href = '/gameplay';
    })
}