"""
OWASP Maryam!

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from core.module import BaseModule


class Module(BaseModule):

	meta = {
		'name': 'Bing Search',
		'author': 'Saeeddqn',
		'version': '0.1',
		'description': 'Search your query in the bing.com and show the results.',
		'sources': ('bing',),
		'options': (
			('query', None, True, 'Query string', '-q', 'store'),
			('limit', 1, False, 'Search limit(count of pages, default=1)', '-l', 'store'),
			('count', 50, False, 'Number of results per page(min=10, max=100, default=50)', '-c', 'store'),
			('output', False, False, 'Save output to workspace', '--output', 'store_true'),
		),
        'examples': ('bing -q <QUERY> -l 15 --output',)
	}

	def module_run(self):
		query = self.options['query']
		limit = self.options['limit']
		count = self.options['count']
		run = self.bing(query, limit, count)
		run.run_crawl()
		links = run.links_with_title

		if links == []:
			self.output('Without result')
		else:
			for item in links:
				link,title = item
				self.output(f'{title}', 'G')
				self.output(f'\t{link}')
				print('')
		self.save_gather(links, 'search/bing', query, output=self.options['output'])
