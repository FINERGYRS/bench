VERSION = "5.14.2"
PROJECT_NAME = "finergy-bench"
FINERGY_VERSION = None
current_path = None
updated_path = None
LOG_BUFFER = []


def set_finergy_version(bench_path="."):
	from .utils.app import get_current_finergy_version

	global FINERGY_VERSION
	if not FINERGY_VERSION:
		FINERGY_VERSION = get_current_finergy_version(bench_path=bench_path)
