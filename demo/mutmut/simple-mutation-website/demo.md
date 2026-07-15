# Demo Mutmut: Website luồng Login -> Import Store Data

## Bảng số liệu kết quả

| Chỉ số | Trước integrate | Sau integrate | Δ |
|---|---:|---:|---:|
| **Average coverage** | **61%** | **88%** | **+27%** |
| `connection` coverage | 77% | 77% | - |
| `store` coverage | 91% | 91% | - |
| `things` coverage | 0% | 100% | +100% |
| `users` coverage | 18% | 89% | +71% |
| Missed Lines Count | 55 | 17 | -38 |
| Mutation score (killed-only/total) | 46.08% | 93.95% | +47.87% |
| Mutants Killed | 94 | 202 | +108 |
| Mutants Total | 204 | 215 | +11 |

## Các lệnh reset tổng quát
```
$ rm -rf mutants/ .mutmut-cache/ .coverage .pytest_cache/
$ find . -type d -name "__pycache__" -exec rm -rf {} +
$ find . -type f -name "*.pyc" -delete
```
## Script các lệnh cần thực thi cho test
- Setup:
```
$ python3 -m venv venv/
$ source venv/bin/activate
$ pip install mutmut
```
- Before integration:

Dữ liệu file `pyproject.toml`:
```
[tool.mutmut]
source_paths = ["datastore/connection.py", "datastore/store.py", "datastore/users.py", "datastore/things.py"]
pytest_add_cli_args_test_selection = ["tests_mutation/"]
also_copy = ["tests_mutation/", "data/"]
```
Lệnh:
```
python -m pytest --cov=datastore/ tests_mutation/ --cov-report=term-missing
mutmut run
mutmut browse
coverage html
```
- Sau integration:

Dữ liệu file `pyproject.toml`:
```
[tool.mutmut]
source_paths = ["datastore/connection.py", "datastore/store.py", "datastore/users.py", "datastore/things.py"]
pytest_add_cli_args_test_selection = ["tests_mutation_integrated/"]
also_copy = ["tests_mutation_integrated/", "data/"]
```
Lệnh:
```
python -m pytest --cov=datastore/ tests_mutation_integrated/ --cov-report=term-missing
mutmut run
mutmut browse
coverage html
```

