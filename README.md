# benchkit

Statistically rigorous benchmarking.

## Install

```bash
git clone https://github.com/openkickstartai/benchkit.git
cd benchkit && pip install -e .
```

## Usage

```bash
benchkit run 'python script.py' --rounds 100
benchkit compare 'python v1.py' 'python v2.py'
benchkit run 'go test -bench .' --format markdown
```

## Testing

```bash
pytest -v
```
