import luigi

from luigi.mock import MockFile, MockTarget

class DownloadPipeline1(luigi.Task):

    date = luigi.Parameter()

    def requires(self):
        pass

    def output(self):
        return MockTarget('./test')

    def run(self):
        pass


luigi.run(['DownloadPipeline1','--date 2017'])
