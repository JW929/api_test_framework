# 这里可以定义一些pytest的通用fixture
import pytest

@pytest.fixture(scope="session", autouse=True)
def setup_and_teardown():
    # 可以在整个测试会话开始和结束时执行的一些初始化或清理操作
    print("\n[Setup] Starting test session.")
    yield
    print("\n[Teardown] Ending test session.")