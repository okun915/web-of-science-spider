from gui.main_gui import *
import settings
from scrapy import cmdline

def crawl_by_query(query, output_path='../output', document_type='', output_format='fieldtagged', sid=None):
    cmdline.execute(
        r'scrapy crawl wos_advanced_query_spider -a output_path={} -a output_format={}'.format(
            output_path, output_format).split() +
        ['-a', 'query={}'.format(query), '-a', 'document_type={}'.format(document_type), '-a', 'sid={}'.format(sid)])

def crawl_by_journal(journal_list_path, output_path='../output', document_type='', output_format='fieldtagged', sid=None):
    cmdline.execute(
        r'scrapy crawl wos_sequential_journal_spider -a journal_list_path={} -a output_path={} -a output_format={}'.format(
            journal_list_path, output_path, output_format).split() + ['-a', 'document_type={}'.format(document_type), '-a', 'sid={}'.format(sid)])


def crawl_by_gui():
    gui_crawler = GuiCrawler()
    gui_crawler.show()
    reactor.run()


if __name__ == '__main__':
    # 按期刊下载
    # crawl_by_journal(journal_list_path=r'../input/journal_list.txt',
    #                  output_path=r'../output', output_format='fieldtagged', document_type='', sid='')

    # 按检索式下载
    crawl_by_query(query='(SO=(SCIENCE) OR SO=(NATURE)) AND PY=(2003-2019)',
                   output_path='../output', output_format='fieldtagged', document_type='Article,Review', sid='')

    # 使用GUI下载
    # crawl_by_gui()
    pass
