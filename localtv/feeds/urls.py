# Copyright 2009 - Participatory Culture Foundation
# 
# This file is part of Miro Community.
# 
# Miro Community is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at your
# option) any later version.
# 
# Miro Community is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
# 
# You should have received a copy of the GNU Affero General Public License
# along with Miro Community.  If not, see <http://www.gnu.org/licenses/>.

from django.conf.urls.defaults import patterns

urlpatterns = patterns(
    'localtv.feeds.views',
    (r'^(json/)?new/$', 'new', {}, 'localtv_feeds_new'),
    (r'^(json/)?featured/$', 'featured', {}, 'localtv_feeds_featured'),
    (r'^(json/)?popular/$', 'popular', {}, 'localtv_feeds_popular'),
    (r'^(json/)?category/([\w-]+)$', 'category', {}, 'localtv_feeds_category'),
    (r'^(json/)?author/(\d+)$', 'author', {}, 'localtv_feeds_author'),
    (r'^(json/)?tag/(.+)$', 'tag', {}, 'localtv_feeds_tag'),
    (r'^(json/)?search/(.+)$', 'search', {}, 'localtv_feeds_search'),
    (r'^(json/)?playlist/(\d+)$', 'playlist', {}, 'localtv_feeds_playlist'),
    )
