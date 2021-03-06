#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""Add storage_interface DB field and object

Revision ID: 1d6951876d68
Revises: 493d8f27f235
Create Date: 2016-07-26 10:33:22.830739

"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '1d6951876d68'
down_revision = '493d8f27f235'


def upgrade():
    op.add_column('nodes', sa.Column('storage_interface',
                                     sa.String(255),
                                     nullable=True))
