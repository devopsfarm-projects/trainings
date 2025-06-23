const express = require('express');
const LokiTransport = require('winston-loki');
const winston = require('winston');

const app = express();
app.use(express.json());

// Configure Loki logger
const logger = winston.createLogger({
    transports: [
        new LokiTransport({
            host: 'https://logs-prod-014.grafana.net/loki/api/v1/push', // Change to your Loki endpoint
            labels: { app: 'expressServer' },
            json: true,
            basicAuth: {
                username: '693051',
                password: 'token'
            },
            replaceTimestamp: true,
            onConnectionError: (err) => console.error(err),
        }),
        new winston.transports.Console()
    ]
});

logger.info('Loki test log: If you see this in Grafana Loki, logging works!');

// Middleware to log all requests
app.use((req, res, next) => {
    logger.info('Incoming request', { method: req.method, url: req.url });
    next();
});

// Sample APIs
app.get('/api/health', (req, res) => {
    logger.info('Health check endpoint hit');
    res.json({ status: 'ok' });
});

app.post('/api/data', (req, res) => {
    logger.info('Data received', { body: req.body });
    res.json({ message: 'Data received', data: req.body });
});

app.get('/api/error', (req, res) => {
    logger.error('Simulated error endpoint hit');
    res.status(500).json({ error: 'Simulated error' });
});

// Start server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    logger.info(`Server running on port ${PORT}`);
});