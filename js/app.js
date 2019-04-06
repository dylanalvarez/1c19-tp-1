const express = require('express');
const app = express();
const port = 3000;

app.get('/', (req, res) => res.send('[js] Hello World'));

app.get('/sleep/', (req, res) =>
    setTimeout(() => res.send('[js] Slept for 1 second'), 1000)
);

app.get('/cpu/', (req, res) => {
    let result = 1;
    for (let i = 0; i < 10000000; i++) {
        result += i / result;
    }
    res.send(`[js] Result: ${result}`);
});

app.listen(port, () => console.log(`App listening on port ${port}!`));
