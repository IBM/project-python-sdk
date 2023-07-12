# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2023.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Integration Tests for ProjectV1
"""

from ibm_cloud_sdk_core import *
import os
import pytest
from ibm_cloud.project_v1 import *

# Config file name
config_file = 'project_v1.env'

# Variables to hold link values
config_id_link = None
project_id_link = None


class TestProjectV1:
    """
    Integration Test Class for ProjectV1
    """

    @classmethod
    def setup_class(cls):
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            cls.project_service = ProjectV1.new_instance(
            )
            assert cls.project_service is not None

            cls.config = read_external_sources(ProjectV1.DEFAULT_SERVICE_NAME)
            assert cls.config is not None

            cls.project_service.enable_retries()

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_create_project(self):
        global project_id_link

        # Construct a dict representation of a ProjectConfigAuthTrustedProfile model
        project_config_auth_trusted_profile_model = {
            'id': 'testString',
            'target_iam_id': 'testString',
        }
        # Construct a dict representation of a ProjectConfigAuth model
        project_config_auth_model = {
            'trusted_profile': project_config_auth_trusted_profile_model,
            'method': 'testString',
            'api_key': 'testString',
        }
        # Construct a dict representation of a ProjectConfigComplianceProfile model
        project_config_compliance_profile_model = {
            'id': 'testString',
            'instance_id': 'testString',
            'instance_location': 'testString',
            'attachment_id': 'testString',
            'profile_name': 'testString',
        }
        # Construct a dict representation of a ProjectConfigInputVariable model
        project_config_input_variable_model = {
            'name': 'testString',
            'value': 'testString',
        }
        # Construct a dict representation of a ProjectConfigSettingCollection model
        project_config_setting_collection_model = {
            'name': 'testString',
            'value': 'testString',
        }
        # Construct a dict representation of a ProjectConfigPrototype model
        project_config_prototype_model = {
            'name': 'common-variables',
            'labels': [],
            'description': 'testString',
            'authorizations': project_config_auth_model,
            'compliance_profile': project_config_compliance_profile_model,
            'locator_id': '1082e7d2-5e2f-0a11-a3bc-f88a8e1931fc.018edf04-e772-4ca2-9785-03e8e03bef72-global',
            'input': [project_config_input_variable_model],
            'setting': [project_config_setting_collection_model],
        }

        response = self.project_service.create_project(
            resource_group='Default',
            location='us-south',
            name='acme-microservice',
            description='A microservice to deploy on top of ACME infrastructure.',
            destroy_on_delete=True,
            configs=[project_config_prototype_model],
        )

        assert response.get_status_code() == 201
        project = response.get_result()
        assert project is not None

        project_id_link = project['id']

    @needscredentials
    def test_create_config(self):
        global config_id_link

        # Construct a dict representation of a ProjectConfigAuthTrustedProfile model
        project_config_auth_trusted_profile_model = {
            'id': 'testString',
            'target_iam_id': 'testString',
        }
        # Construct a dict representation of a ProjectConfigAuth model
        project_config_auth_model = {
            'trusted_profile': project_config_auth_trusted_profile_model,
            'method': 'testString',
            'api_key': 'testString',
        }
        # Construct a dict representation of a ProjectConfigComplianceProfile model
        project_config_compliance_profile_model = {
            'id': 'testString',
            'instance_id': 'testString',
            'instance_location': 'testString',
            'attachment_id': 'testString',
            'profile_name': 'testString',
        }
        # Construct a dict representation of a ProjectConfigInputVariable model
        project_config_input_variable_model = {
            'name': 'account_id',
            'value': '$configs[].name[\"account-stage\"].input.account_id',
        }
        # Construct a dict representation of a ProjectConfigSettingCollection model
        project_config_setting_collection_model = {
            'name': 'IBMCLOUD_TOOLCHAIN_ENDPOINT',
            'value': 'https://api.us-south.devops.dev.cloud.ibm.com',
        }

        response = self.project_service.create_config(
            project_id=project_id_link,
            name='env-stage',
            locator_id='1082e7d2-5e2f-0a11-a3bc-f88a8e1931fc.018edf04-e772-4ca2-9785-03e8e03bef72-global',
            labels=['env:stage', 'governance:test', 'build:0'],
            description='Stage environment configuration, which includes services common to all the environment regions. There must be a blueprint configuring all the services common to the stage regions. It is a terraform_template type of configuration that points to a Github repo hosting the terraform modules that can be deployed by a Schematics Workspace.',
            authorizations=project_config_auth_model,
            compliance_profile=project_config_compliance_profile_model,
            input=[project_config_input_variable_model],
            setting=[project_config_setting_collection_model],
        )

        assert response.get_status_code() == 201
        project_config_draft_response = response.get_result()
        assert project_config_draft_response is not None

        config_id_link = project_config_draft_response['id']

    @needscredentials
    def test_list_projects(self):
        response = self.project_service.list_projects(
            start='testString',
            limit=10,
        )

        assert response.get_status_code() == 200
        project_collection = response.get_result()
        assert project_collection is not None

    @needscredentials
    def test_list_projects_with_pager(self):
        all_results = []

        # Test get_next().
        pager = ProjectsPager(
            client=self.project_service,
            limit=10,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)

        # Test get_all().
        pager = ProjectsPager(
            client=self.project_service,
            limit=10,
        )
        all_items = pager.get_all()
        assert all_items is not None

        assert len(all_results) == len(all_items)
        print(f'\nlist_projects() returned a total of {len(all_results)} items(s) using ProjectsPager.')

    @needscredentials
    def test_get_project(self):
        response = self.project_service.get_project(
            id=project_id_link,
        )

        assert response.get_status_code() == 200
        project_summary = response.get_result()
        assert project_summary is not None

    @needscredentials
    def test_update_project(self):
        response = self.project_service.update_project(
            id=project_id_link,
            name='acme-microservice',
            description='A microservice to deploy on top of ACME infrastructure.',
            destroy_on_delete=True,
        )

        assert response.get_status_code() == 200
        project_summary = response.get_result()
        assert project_summary is not None

    @needscredentials
    def test_list_configs(self):
        response = self.project_service.list_configs(
            project_id=project_id_link,
        )

        assert response.get_status_code() == 200
        project_config_collection = response.get_result()
        assert project_config_collection is not None

    @needscredentials
    def test_get_config(self):
        response = self.project_service.get_config(
            project_id=project_id_link,
            id=config_id_link,
        )

        assert response.get_status_code() == 200
        project_config_get_response = response.get_result()
        assert project_config_get_response is not None

    @needscredentials
    def test_update_config(self):
        # Construct a dict representation of a ProjectConfigInputVariable model
        project_config_input_variable_model = {
            'name': 'account_id',
            'value': '$configs[].name[\"account-stage\"].input.account_id',
        }
        # Construct a dict representation of a ProjectConfigSettingCollection model
        project_config_setting_collection_model = {
            'name': 'testString',
            'value': 'testString',
        }
        # Construct a dict representation of a ProjectConfigAuthTrustedProfile model
        project_config_auth_trusted_profile_model = {
            'id': 'testString',
            'target_iam_id': 'testString',
        }
        # Construct a dict representation of a ProjectConfigAuth model
        project_config_auth_model = {
            'trusted_profile': project_config_auth_trusted_profile_model,
            'method': 'testString',
            'api_key': 'testString',
        }
        # Construct a dict representation of a ProjectConfigComplianceProfile model
        project_config_compliance_profile_model = {
            'id': 'testString',
            'instance_id': 'testString',
            'instance_location': 'testString',
            'attachment_id': 'testString',
            'profile_name': 'testString',
        }

        response = self.project_service.update_config(
            project_id=project_id_link,
            id=config_id_link,
            locator_id='testString',
            input=[project_config_input_variable_model],
            setting=[project_config_setting_collection_model],
            name='testString',
            labels=['testString'],
            description='testString',
            authorizations=project_config_auth_model,
            compliance_profile=project_config_compliance_profile_model,
        )

        assert response.get_status_code() == 200
        project_config_draft_response = response.get_result()
        assert project_config_draft_response is not None

    @needscredentials
    def test_force_approve(self):
        response = self.project_service.force_approve(
            project_id=project_id_link,
            id=config_id_link,
            comment='Approving the changes',
        )

        assert response.get_status_code() == 201
        project_config_get_response = response.get_result()
        assert project_config_get_response is not None

    @needscredentials
    def test_approve(self):
        response = self.project_service.approve(
            project_id=project_id_link,
            id=config_id_link,
            comment='Approving the changes',
        )

        assert response.get_status_code() == 201
        project_config_get_response = response.get_result()
        assert project_config_get_response is not None

    @needscredentials
    def test_check_config(self):
        response = self.project_service.check_config(
            project_id=project_id_link,
            id=config_id_link,
            x_auth_refresh_token='testString',
            is_draft=True,
        )

        assert response.get_status_code() == 202
        project_config_get_response = response.get_result()
        assert project_config_get_response is not None

    @needscredentials
    def test_install_config(self):
        response = self.project_service.install_config(
            project_id=project_id_link,
            id=config_id_link,
        )

        assert response.get_status_code() == 202
        project_config_get_response = response.get_result()
        assert project_config_get_response is not None

    @needscredentials
    def test_uninstall_config(self):
        response = self.project_service.uninstall_config(
            project_id=project_id_link,
            id=config_id_link,
        )

        assert response.get_status_code() == 204

    @needscredentials
    def test_list_config_resources(self):
        response = self.project_service.list_config_resources(
            project_id=project_id_link,
            id=config_id_link,
        )

        assert response.get_status_code() == 200
        project_config_resource_collection = response.get_result()
        assert project_config_resource_collection is not None

    @needscredentials
    def test_list_config_drafts(self):
        response = self.project_service.list_config_drafts(
            project_id=project_id_link,
            config_id='testString',
        )

        assert response.get_status_code() == 200
        project_config_draft_summary_collection = response.get_result()
        assert project_config_draft_summary_collection is not None

    @needscredentials
    def test_get_config_draft(self):
        response = self.project_service.get_config_draft(
            project_id=project_id_link,
            config_id='testString',
            version=38,
        )

        assert response.get_status_code() == 200
        project_config_draft_response = response.get_result()
        assert project_config_draft_response is not None

    @needscredentials
    def test_delete_config(self):
        response = self.project_service.delete_config(
            project_id=project_id_link,
            id=config_id_link,
            draft_only=False,
        )

        assert response.get_status_code() == 200
        project_config_delete = response.get_result()
        assert project_config_delete is not None

    @needscredentials
    def test_delete_project(self):
        response = self.project_service.delete_project(
            id=project_id_link,
        )

        assert response.get_status_code() == 204
