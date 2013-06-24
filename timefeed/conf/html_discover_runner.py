from discover_runner import DiscoverRunner
from timefeed.conf.html_test_runner import HTMLTestRunner

class HTMLDiscoverRunner(DiscoverRunner):
    def run_suite(self, suite, **kwargs):
        fp = file('tests_report.html', 'wb')
        runner = HTMLTestRunner(
                stream=fp
                )
                
        return runner.run(suite)
