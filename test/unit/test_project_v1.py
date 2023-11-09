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
Unit Tests for ProjectV1
"""

from datetime import datetime, timezone
from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
from ibm_cloud_sdk_core.utils import datetime_to_string, string_to_datetime
import inspect
import json
import os
import pytest
import re
import requests
import responses
import urllib
from ibm_cloud.project_v1 import *


_service = ProjectV1(
    authenticator=NoAuthAuthenticator()
)

_base_url = 'https://projects.api.cloud.ibm.com'
_service.set_service_url(_base_url)


def preprocess_url(operation_path: str):
    """
    Returns the request url associated with the specified operation path.
    This will be base_url concatenated with a quoted version of operation_path.
    The returned request URL is used to register the mock response so it needs
    to match the request URL that is formed by the requests library.
    """
    # First, unquote the path since it might have some quoted/escaped characters in it
    # due to how the generator inserts the operation paths into the unit test code.
    operation_path = urllib.parse.unquote(operation_path)

    # Next, quote the path using urllib so that we approximate what will
    # happen during request processing.
    operation_path = urllib.parse.quote(operation_path, safe='/')

    # Finally, form the request URL from the base URL and operation path.
    request_url = _base_url + operation_path

    # If the request url does NOT end with a /, then just return it as-is.
    # Otherwise, return a regular expression that matches one or more trailing /.
    if re.fullmatch('.*/+', request_url) is None:
        return request_url
    else:
        return re.compile(request_url.rstrip('/') + '/+')


##############################################################################
# Start of Service: Projects
##############################################################################
# region


class TestNewInstance:
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = ProjectV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, ProjectV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = ProjectV1.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestCreateProject:
    """
    Test Class for create_project
    """

    @responses.activate
    def test_create_project_all_params(self):
        """
        create_project()
        """
        # Set up mock
        url = preprocess_url('/v1/projects')
        mock_response = '{"crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::", "created_at": "2019-01-01T12:00:00.000Z", "cumulative_needs_attention_view": [{"event": "event", "event_id": "event_id", "config_id": "config_id", "config_version": 14}], "cumulative_needs_attention_view_error": false, "id": "id", "location": "location", "resource_group_id": "resource_group_id", "state": "ready", "resource_group": "resource_group", "event_notifications_crn": "event_notifications_crn", "configs": [{"approved_version": {"state": "approved", "version": 7, "href": "href"}, "deployed_version": {"state": "approved", "version": 7, "href": "href"}, "id": "id", "version": 7, "state": "approved", "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "href": "href", "definition": {"name": "name", "description": "description"}, "project": {"id": "id", "definition": {"name": "name"}, "crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::", "href": "href"}}], "environments": [{"id": "id", "project": {"id": "id", "definition": {"name": "name"}, "crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::", "href": "href"}, "created_at": "2019-01-01T12:00:00.000Z", "href": "href", "definition": {"name": "name", "description": "description"}}], "definition": {"name": "name", "description": "description", "destroy_on_delete": false}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a ProjectPrototypeDefinition model
        project_prototype_definition_model = {}
        project_prototype_definition_model['name'] = 'acme-microservice'
        project_prototype_definition_model['description'] = 'A microservice to deploy on top of ACME infrastructure.'
        project_prototype_definition_model['destroy_on_delete'] = True

        # Construct a dict representation of a ProjectConfigAuth model
        project_config_auth_model = {}
        project_config_auth_model['trusted_profile_id'] = 'testString'
        project_config_auth_model['method'] = 'api_key'
        project_config_auth_model['api_key'] = 'testString'

        # Construct a dict representation of a ProjectComplianceProfile model
        project_compliance_profile_model = {}
        project_compliance_profile_model['id'] = 'testString'
        project_compliance_profile_model['instance_id'] = 'testString'
        project_compliance_profile_model['instance_location'] = 'testString'
        project_compliance_profile_model['attachment_id'] = 'testString'
        project_compliance_profile_model['profile_name'] = 'testString'

        # Construct a dict representation of a InputVariable model
        input_variable_model = {}
        input_variable_model['foo'] = 'testString'

        # Construct a dict representation of a ProjectConfigSetting model
        project_config_setting_model = {}
        project_config_setting_model['foo'] = 'testString'

        # Construct a dict representation of a ProjectConfigPrototypeDefinitionBlock model
        project_config_prototype_definition_block_model = {}
        project_config_prototype_definition_block_model['name'] = 'testString'
        project_config_prototype_definition_block_model['description'] = 'testString'
        project_config_prototype_definition_block_model['environment'] = 'testString'
        project_config_prototype_definition_block_model['authorizations'] = project_config_auth_model
        project_config_prototype_definition_block_model['compliance_profile'] = project_compliance_profile_model
        project_config_prototype_definition_block_model['locator_id'] = 'testString'
        project_config_prototype_definition_block_model['inputs'] = input_variable_model
        project_config_prototype_definition_block_model['settings'] = project_config_setting_model

        # Construct a dict representation of a SchematicsWorkspace model
        schematics_workspace_model = {}
        schematics_workspace_model['workspace_crn'] = 'testString'

        # Construct a dict representation of a ProjectConfigPrototype model
        project_config_prototype_model = {}
        project_config_prototype_model['definition'] = project_config_prototype_definition_block_model
        project_config_prototype_model['schematics'] = schematics_workspace_model

        # Set up parameter values
        definition = project_prototype_definition_model
        location = 'us-south'
        resource_group = 'Default'
        configs = [project_config_prototype_model]

        # Invoke method
        response = _service.create_project(
            definition,
            location,
            resource_group,
            configs=configs,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['definition'] == project_prototype_definition_model
        assert req_body['location'] == 'us-south'
        assert req_body['resource_group'] == 'Default'
        assert req_body['configs'] == [project_config_prototype_model]

    def test_create_project_all_params_with_retries(self):
        # Enable retries and run test_create_project_all_params.
        _service.enable_retries()
        self.test_create_project_all_params()

        # Disable retries and run test_create_project_all_params.
        _service.disable_retries()
        self.test_create_project_all_params()

    @responses.activate
    def test_create_project_value_error(self):
        """
        test_create_project_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/projects')
        mock_response = '{"crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::", "created_at": "2019-01-01T12:00:00.000Z", "cumulative_needs_attention_view": [{"event": "event", "event_id": "event_id", "config_id": "config_id", "config_version": 14}], "cumulative_needs_attention_view_error": false, "id": "id", "location": "location", "resource_group_id": "resource_group_id", "state": "ready", "resource_group": "resource_group", "event_notifications_crn": "event_notifications_crn", "configs": [{"approved_version": {"state": "approved", "version": 7, "href": "href"}, "deployed_version": {"state": "approved", "version": 7, "href": "href"}, "id": "id", "version": 7, "state": "approved", "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "href": "href", "definition": {"name": "name", "description": "description"}, "project": {"id": "id", "definition": {"name": "name"}, "crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::", "href": "href"}}], "environments": [{"id": "id", "project": {"id": "id", "definition": {"name": "name"}, "crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::", "href": "href"}, "created_at": "2019-01-01T12:00:00.000Z", "href": "href", "definition": {"name": "name", "description": "description"}}], "definition": {"name": "name", "description": "description", "destroy_on_delete": false}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a ProjectPrototypeDefinition model
        project_prototype_definition_model = {}
        project_prototype_definition_model['name'] = 'acme-microservice'
        project_prototype_definition_model['description'] = 'A microservice to deploy on top of ACME infrastructure.'
        project_prototype_definition_model['destroy_on_delete'] = True

        # Construct a dict representation of a ProjectConfigAuth model
        project_config_auth_model = {}
        project_config_auth_model['trusted_profile_id'] = 'testString'
        project_config_auth_model['method'] = 'api_key'
        project_config_auth_model['api_key'] = 'testString'

        # Construct a dict representation of a ProjectComplianceProfile model
        project_compliance_profile_model = {}
        project_compliance_profile_model['id'] = 'testString'
        project_compliance_profile_model['instance_id'] = 'testString'
        project_compliance_profile_model['instance_location'] = 'testString'
        project_compliance_profile_model['attachment_id'] = 'testString'
        project_compliance_profile_model['profile_name'] = 'testString'

        # Construct a dict representation of a InputVariable model
        input_variable_model = {}
        input_variable_model['foo'] = 'testString'

        # Construct a dict representation of a ProjectConfigSetting model
        project_config_setting_model = {}
        project_config_setting_model['foo'] = 'testString'

        # Construct a dict representation of a ProjectConfigPrototypeDefinitionBlock model
        project_config_prototype_definition_block_model = {}
        project_config_prototype_definition_block_model['name'] = 'testString'
        project_config_prototype_definition_block_model['description'] = 'testString'
        project_config_prototype_definition_block_model['environment'] = 'testString'
        project_config_prototype_definition_block_model['authorizations'] = project_config_auth_model
        project_config_prototype_definition_block_model['compliance_profile'] = project_compliance_profile_model
        project_config_prototype_definition_block_model['locator_id'] = 'testString'
        project_config_prototype_definition_block_model['inputs'] = input_variable_model
        project_config_prototype_definition_block_model['settings'] = project_config_setting_model

        # Construct a dict representation of a SchematicsWorkspace model
        schematics_workspace_model = {}
        schematics_workspace_model['workspace_crn'] = 'testString'

        # Construct a dict representation of a ProjectConfigPrototype model
        project_config_prototype_model = {}
        project_config_prototype_model['definition'] = project_config_prototype_definition_block_model
        project_config_prototype_model['schematics'] = schematics_workspace_model

        # Set up parameter values
        definition = project_prototype_definition_model
        location = 'us-south'
        resource_group = 'Default'
        configs = [project_config_prototype_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "definition": definition,
            "location": location,
            "resource_group": resource_group,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_project(**req_copy)

    def test_create_project_value_error_with_retries(self):
        # Enable retries and run test_create_project_value_error.
        _service.enable_retries()
        self.test_create_project_value_error()

        # Disable retries and run test_create_project_value_error.
        _service.disable_retries()
        self.test_create_project_value_error()


class TestListProjects:
    """
    Test Class for list_projects
    """

    @responses.activate
    def test_list_projects_all_params(self):
        """
        list_projects()
        """
        # Set up mock
        url = preprocess_url('/v1/projects')
        mock_response = '{"limit": 10, "total_count": 0, "first": {"href": "href"}, "last": {"href": "href"}, "previous": {"href": "href"}, "next": {"href": "href"}, "projects": [{"crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::", "created_at": "2019-01-01T12:00:00.000Z", "cumulative_needs_attention_view": [{"event": "event", "event_id": "event_id", "config_id": "config_id", "config_version": 14}], "cumulative_needs_attention_view_error": false, "id": "id", "location": "location", "resource_group_id": "resource_group_id", "state": "ready", "definition": {"name": "name", "description": "description", "destroy_on_delete": false}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        start = 'testString'
        limit = 10

        # Invoke method
        response = _service.list_projects(
            start=start,
            limit=limit,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'start={}'.format(start) in query_string
        assert 'limit={}'.format(limit) in query_string

    def test_list_projects_all_params_with_retries(self):
        # Enable retries and run test_list_projects_all_params.
        _service.enable_retries()
        self.test_list_projects_all_params()

        # Disable retries and run test_list_projects_all_params.
        _service.disable_retries()
        self.test_list_projects_all_params()

    @responses.activate
    def test_list_projects_required_params(self):
        """
        test_list_projects_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/projects')
        mock_response = '{"limit": 10, "total_count": 0, "first": {"href": "href"}, "last": {"href": "href"}, "previous": {"href": "href"}, "next": {"href": "href"}, "projects": [{"crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::", "created_at": "2019-01-01T12:00:00.000Z", "cumulative_needs_attention_view": [{"event": "event", "event_id": "event_id", "config_id": "config_id", "config_version": 14}], "cumulative_needs_attention_view_error": false, "id": "id", "location": "location", "resource_group_id": "resource_group_id", "state": "ready", "definition": {"name": "name", "description": "description", "destroy_on_delete": false}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.list_projects()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_projects_required_params_with_retries(self):
        # Enable retries and run test_list_projects_required_params.
        _service.enable_retries()
        self.test_list_projects_required_params()

        # Disable retries and run test_list_projects_required_params.
        _service.disable_retries()
        self.test_list_projects_required_params()

    @responses.activate
    def test_list_projects_with_pager_get_next(self):
        """
        test_list_projects_with_pager_get_next()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v1/projects')
        mock_response1 = '{"next":{"href":"https://myhost.com/somePath?start=1"},"projects":[{"crn":"crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::","created_at":"2019-01-01T12:00:00.000Z","cumulative_needs_attention_view":[{"event":"event","event_id":"event_id","config_id":"config_id","config_version":14}],"cumulative_needs_attention_view_error":false,"id":"id","location":"location","resource_group_id":"resource_group_id","state":"ready","definition":{"name":"name","description":"description","destroy_on_delete":false}}],"total_count":2,"limit":1}'
        mock_response2 = '{"projects":[{"crn":"crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::","created_at":"2019-01-01T12:00:00.000Z","cumulative_needs_attention_view":[{"event":"event","event_id":"event_id","config_id":"config_id","config_version":14}],"cumulative_needs_attention_view_error":false,"id":"id","location":"location","resource_group_id":"resource_group_id","state":"ready","definition":{"name":"name","description":"description","destroy_on_delete":false}}],"total_count":2,"limit":1}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        all_results = []
        pager = ProjectsPager(
            client=_service,
            limit=10,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)
        assert len(all_results) == 2

    @responses.activate
    def test_list_projects_with_pager_get_all(self):
        """
        test_list_projects_with_pager_get_all()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v1/projects')
        mock_response1 = '{"next":{"href":"https://myhost.com/somePath?start=1"},"projects":[{"crn":"crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::","created_at":"2019-01-01T12:00:00.000Z","cumulative_needs_attention_view":[{"event":"event","event_id":"event_id","config_id":"config_id","config_version":14}],"cumulative_needs_attention_view_error":false,"id":"id","location":"location","resource_group_id":"resource_group_id","state":"ready","definition":{"name":"name","description":"description","destroy_on_delete":false}}],"total_count":2,"limit":1}'
        mock_response2 = '{"projects":[{"crn":"crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::","created_at":"2019-01-01T12:00:00.000Z","cumulative_needs_attention_view":[{"event":"event","event_id":"event_id","config_id":"config_id","config_version":14}],"cumulative_needs_attention_view_error":false,"id":"id","location":"location","resource_group_id":"resource_group_id","state":"ready","definition":{"name":"name","description":"description","destroy_on_delete":false}}],"total_count":2,"limit":1}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        pager = ProjectsPager(
            client=_service,
            limit=10,
        )
        all_results = pager.get_all()
        assert all_results is not None
        assert len(all_results) == 2


class TestGetProject:
    """
    Test Class for get_project
    """

    @responses.activate
    def test_get_project_all_params(self):
        """
        get_project()
        """
        # Set up mock
        url = preprocess_url('/v1/projects/testString')
        mock_response = '{"crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::", "created_at": "2019-01-01T12:00:00.000Z", "cumulative_needs_attention_view": [{"event": "event", "event_id": "event_id", "config_id": "config_id", "config_version": 14}], "cumulative_needs_attention_view_error": false, "id": "id", "location": "location", "resource_group_id": "resource_group_id", "state": "ready", "resource_group": "resource_group", "event_notifications_crn": "event_notifications_crn", "configs": [{"approved_version": {"state": "approved", "version": 7, "href": "href"}, "deployed_version": {"state": "approved", "version": 7, "href": "href"}, "id": "id", "version": 7, "state": "approved", "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "href": "href", "definition": {"name": "name", "description": "description"}, "project": {"id": "id", "definition": {"name": "name"}, "crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::", "href": "href"}}], "environments": [{"id": "id", "project": {"id": "id", "definition": {"name": "name"}, "crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::", "href": "href"}, "created_at": "2019-01-01T12:00:00.000Z", "href": "href", "definition": {"name": "name", "description": "description"}}], "definition": {"name": "name", "description": "description", "destroy_on_delete": false}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = _service.get_project(
            id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_project_all_params_with_retries(self):
        # Enable retries and run test_get_project_all_params.
        _service.enable_retries()
        self.test_get_project_all_params()

        # Disable retries and run test_get_project_all_params.
        _service.disable_retries()
        self.test_get_project_all_params()

    @responses.activate
    def test_get_project_value_error(self):
        """
        test_get_project_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/projects/testString')
        mock_response = '{"crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::", "created_at": "2019-01-01T12:00:00.000Z", "cumulative_needs_attention_view": [{"event": "event", "event_id": "event_id", "config_id": "config_id", "config_version": 14}], "cumulative_needs_attention_view_error": false, "id": "id", "location": "location", "resource_group_id": "resource_group_id", "state": "ready", "resource_group": "resource_group", "event_notifications_crn": "event_notifications_crn", "configs": [{"approved_version": {"state": "approved", "version": 7, "href": "href"}, "deployed_version": {"state": "approved", "version": 7, "href": "href"}, "id": "id", "version": 7, "state": "approved", "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "href": "href", "definition": {"name": "name", "description": "description"}, "project": {"id": "id", "definition": {"name": "name"}, "crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::", "href": "href"}}], "environments": [{"id": "id", "project": {"id": "id", "definition": {"name": "name"}, "crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::", "href": "href"}, "created_at": "2019-01-01T12:00:00.000Z", "href": "href", "definition": {"name": "name", "description": "description"}}], "definition": {"name": "name", "description": "description", "destroy_on_delete": false}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_project(**req_copy)

    def test_get_project_value_error_with_retries(self):
        # Enable retries and run test_get_project_value_error.
        _service.enable_retries()
        self.test_get_project_value_error()

        # Disable retries and run test_get_project_value_error.
        _service.disable_retries()
        self.test_get_project_value_error()


class TestUpdateProject:
    """
    Test Class for update_project
    """

    @responses.activate
    def test_update_project_all_params(self):
        """
        update_project()
        """
        # Set up mock
        url = preprocess_url('/v1/projects/testString')
        mock_response = '{"crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::", "created_at": "2019-01-01T12:00:00.000Z", "cumulative_needs_attention_view": [{"event": "event", "event_id": "event_id", "config_id": "config_id", "config_version": 14}], "cumulative_needs_attention_view_error": false, "id": "id", "location": "location", "resource_group_id": "resource_group_id", "state": "ready", "resource_group": "resource_group", "event_notifications_crn": "event_notifications_crn", "configs": [{"approved_version": {"state": "approved", "version": 7, "href": "href"}, "deployed_version": {"state": "approved", "version": 7, "href": "href"}, "id": "id", "version": 7, "state": "approved", "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "href": "href", "definition": {"name": "name", "description": "description"}, "project": {"id": "id", "definition": {"name": "name"}, "crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::", "href": "href"}}], "environments": [{"id": "id", "project": {"id": "id", "definition": {"name": "name"}, "crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::", "href": "href"}, "created_at": "2019-01-01T12:00:00.000Z", "href": "href", "definition": {"name": "name", "description": "description"}}], "definition": {"name": "name", "description": "description", "destroy_on_delete": false}}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a ProjectPatchDefinitionBlock model
        project_patch_definition_block_model = {}
        project_patch_definition_block_model['name'] = 'acme-microservice'
        project_patch_definition_block_model['description'] = 'A microservice to deploy on top of ACME infrastructure.'
        project_patch_definition_block_model['destroy_on_delete'] = True

        # Set up parameter values
        id = 'testString'
        definition = project_patch_definition_block_model

        # Invoke method
        response = _service.update_project(
            id,
            definition,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['definition'] == project_patch_definition_block_model

    def test_update_project_all_params_with_retries(self):
        # Enable retries and run test_update_project_all_params.
        _service.enable_retries()
        self.test_update_project_all_params()

        # Disable retries and run test_update_project_all_params.
        _service.disable_retries()
        self.test_update_project_all_params()

    @responses.activate
    def test_update_project_value_error(self):
        """
        test_update_project_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/projects/testString')
        mock_response = '{"crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::", "created_at": "2019-01-01T12:00:00.000Z", "cumulative_needs_attention_view": [{"event": "event", "event_id": "event_id", "config_id": "config_id", "config_version": 14}], "cumulative_needs_attention_view_error": false, "id": "id", "location": "location", "resource_group_id": "resource_group_id", "state": "ready", "resource_group": "resource_group", "event_notifications_crn": "event_notifications_crn", "configs": [{"approved_version": {"state": "approved", "version": 7, "href": "href"}, "deployed_version": {"state": "approved", "version": 7, "href": "href"}, "id": "id", "version": 7, "state": "approved", "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "href": "href", "definition": {"name": "name", "description": "description"}, "project": {"id": "id", "definition": {"name": "name"}, "crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::", "href": "href"}}], "environments": [{"id": "id", "project": {"id": "id", "definition": {"name": "name"}, "crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::", "href": "href"}, "created_at": "2019-01-01T12:00:00.000Z", "href": "href", "definition": {"name": "name", "description": "description"}}], "definition": {"name": "name", "description": "description", "destroy_on_delete": false}}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a ProjectPatchDefinitionBlock model
        project_patch_definition_block_model = {}
        project_patch_definition_block_model['name'] = 'acme-microservice'
        project_patch_definition_block_model['description'] = 'A microservice to deploy on top of ACME infrastructure.'
        project_patch_definition_block_model['destroy_on_delete'] = True

        # Set up parameter values
        id = 'testString'
        definition = project_patch_definition_block_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
            "definition": definition,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_project(**req_copy)

    def test_update_project_value_error_with_retries(self):
        # Enable retries and run test_update_project_value_error.
        _service.enable_retries()
        self.test_update_project_value_error()

        # Disable retries and run test_update_project_value_error.
        _service.disable_retries()
        self.test_update_project_value_error()


class TestDeleteProject:
    """
    Test Class for delete_project
    """

    @responses.activate
    def test_delete_project_all_params(self):
        """
        delete_project()
        """
        # Set up mock
        url = preprocess_url('/v1/projects/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = _service.delete_project(
            id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_project_all_params_with_retries(self):
        # Enable retries and run test_delete_project_all_params.
        _service.enable_retries()
        self.test_delete_project_all_params()

        # Disable retries and run test_delete_project_all_params.
        _service.disable_retries()
        self.test_delete_project_all_params()

    @responses.activate
    def test_delete_project_value_error(self):
        """
        test_delete_project_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/projects/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_project(**req_copy)

    def test_delete_project_value_error_with_retries(self):
        # Enable retries and run test_delete_project_value_error.
        _service.enable_retries()
        self.test_delete_project_value_error()

        # Disable retries and run test_delete_project_value_error.
        _service.disable_retries()
        self.test_delete_project_value_error()


# endregion
##############################################################################
# End of Service: Projects
##############################################################################

##############################################################################
# Start of Service: Environments
##############################################################################
# region


class TestNewInstance:
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = ProjectV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, ProjectV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = ProjectV1.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestCreateProjectEnvironment:
    """
    Test Class for create_project_environment
    """

    @responses.activate
    def test_create_project_environment_all_params(self):
        """
        create_project_environment()
        """
        # Set up mock
        url = preprocess_url('/v1/projects/testString/environments')
        mock_response = '{"id": "id", "project": {"id": "id", "definition": {"name": "name"}, "crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::", "href": "href"}, "created_at": "2019-01-01T12:00:00.000Z", "target_account": "target_account", "modified_at": "2019-01-01T12:00:00.000Z", "definition": {"name": "name", "description": "description", "authorizations": {"trusted_profile_id": "trusted_profile_id", "method": "api_key", "api_key": "api_key"}, "inputs": {}, "compliance_profile": {"id": "id", "instance_id": "instance_id", "instance_location": "instance_location", "attachment_id": "attachment_id", "profile_name": "profile_name"}}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a ProjectConfigAuth model
        project_config_auth_model = {}
        project_config_auth_model['trusted_profile_id'] = 'testString'
        project_config_auth_model['method'] = 'api_key'
        project_config_auth_model['api_key'] = 'TbcdlprpFODhkpns9e0daOWnAwd2tXwSYtPn8rpEd8d9'

        # Construct a dict representation of a InputVariable model
        input_variable_model = {}
        input_variable_model['resource_group'] = 'stage'
        input_variable_model['region'] = 'us-south'

        # Construct a dict representation of a ProjectComplianceProfile model
        project_compliance_profile_model = {}
        project_compliance_profile_model['id'] = 'some-profile-id'
        project_compliance_profile_model['instance_id'] = 'some-instance-id'
        project_compliance_profile_model['instance_location'] = 'us-south'
        project_compliance_profile_model['attachment_id'] = 'some-attachment-id'
        project_compliance_profile_model['profile_name'] = 'some-profile-name'

        # Construct a dict representation of a EnvironmentDefinitionRequiredProperties model
        environment_definition_required_properties_model = {}
        environment_definition_required_properties_model['name'] = 'development'
        environment_definition_required_properties_model['description'] = 'The environment \'development\''
        environment_definition_required_properties_model['authorizations'] = project_config_auth_model
        environment_definition_required_properties_model['inputs'] = input_variable_model
        environment_definition_required_properties_model['compliance_profile'] = project_compliance_profile_model

        # Set up parameter values
        project_id = 'testString'
        definition = environment_definition_required_properties_model

        # Invoke method
        response = _service.create_project_environment(
            project_id,
            definition,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['definition'] == environment_definition_required_properties_model

    def test_create_project_environment_all_params_with_retries(self):
        # Enable retries and run test_create_project_environment_all_params.
        _service.enable_retries()
        self.test_create_project_environment_all_params()

        # Disable retries and run test_create_project_environment_all_params.
        _service.disable_retries()
        self.test_create_project_environment_all_params()

    @responses.activate
    def test_create_project_environment_value_error(self):
        """
        test_create_project_environment_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/projects/testString/environments')
        mock_response = '{"id": "id", "project": {"id": "id", "definition": {"name": "name"}, "crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::", "href": "href"}, "created_at": "2019-01-01T12:00:00.000Z", "target_account": "target_account", "modified_at": "2019-01-01T12:00:00.000Z", "definition": {"name": "name", "description": "description", "authorizations": {"trusted_profile_id": "trusted_profile_id", "method": "api_key", "api_key": "api_key"}, "inputs": {}, "compliance_profile": {"id": "id", "instance_id": "instance_id", "instance_location": "instance_location", "attachment_id": "attachment_id", "profile_name": "profile_name"}}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a ProjectConfigAuth model
        project_config_auth_model = {}
        project_config_auth_model['trusted_profile_id'] = 'testString'
        project_config_auth_model['method'] = 'api_key'
        project_config_auth_model['api_key'] = 'TbcdlprpFODhkpns9e0daOWnAwd2tXwSYtPn8rpEd8d9'

        # Construct a dict representation of a InputVariable model
        input_variable_model = {}
        input_variable_model['resource_group'] = 'stage'
        input_variable_model['region'] = 'us-south'

        # Construct a dict representation of a ProjectComplianceProfile model
        project_compliance_profile_model = {}
        project_compliance_profile_model['id'] = 'some-profile-id'
        project_compliance_profile_model['instance_id'] = 'some-instance-id'
        project_compliance_profile_model['instance_location'] = 'us-south'
        project_compliance_profile_model['attachment_id'] = 'some-attachment-id'
        project_compliance_profile_model['profile_name'] = 'some-profile-name'

        # Construct a dict representation of a EnvironmentDefinitionRequiredProperties model
        environment_definition_required_properties_model = {}
        environment_definition_required_properties_model['name'] = 'development'
        environment_definition_required_properties_model['description'] = 'The environment \'development\''
        environment_definition_required_properties_model['authorizations'] = project_config_auth_model
        environment_definition_required_properties_model['inputs'] = input_variable_model
        environment_definition_required_properties_model['compliance_profile'] = project_compliance_profile_model

        # Set up parameter values
        project_id = 'testString'
        definition = environment_definition_required_properties_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "definition": definition,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_project_environment(**req_copy)

    def test_create_project_environment_value_error_with_retries(self):
        # Enable retries and run test_create_project_environment_value_error.
        _service.enable_retries()
        self.test_create_project_environment_value_error()

        # Disable retries and run test_create_project_environment_value_error.
        _service.disable_retries()
        self.test_create_project_environment_value_error()


class TestListProjectEnvironments:
    """
    Test Class for list_project_environments
    """

    @responses.activate
    def test_list_project_environments_all_params(self):
        """
        list_project_environments()
        """
        # Set up mock
        url = preprocess_url('/v1/projects/testString/environments')
        mock_response = '{"environments": [{"id": "id", "project": {"id": "id", "definition": {"name": "name"}, "crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::", "href": "href"}, "created_at": "2019-01-01T12:00:00.000Z", "target_account": "target_account", "modified_at": "2019-01-01T12:00:00.000Z", "definition": {"name": "name", "description": "description", "authorizations": {"trusted_profile_id": "trusted_profile_id", "method": "api_key", "api_key": "api_key"}, "inputs": {}, "compliance_profile": {"id": "id", "instance_id": "instance_id", "instance_location": "instance_location", "attachment_id": "attachment_id", "profile_name": "profile_name"}}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = 'testString'

        # Invoke method
        response = _service.list_project_environments(
            project_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_project_environments_all_params_with_retries(self):
        # Enable retries and run test_list_project_environments_all_params.
        _service.enable_retries()
        self.test_list_project_environments_all_params()

        # Disable retries and run test_list_project_environments_all_params.
        _service.disable_retries()
        self.test_list_project_environments_all_params()

    @responses.activate
    def test_list_project_environments_value_error(self):
        """
        test_list_project_environments_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/projects/testString/environments')
        mock_response = '{"environments": [{"id": "id", "project": {"id": "id", "definition": {"name": "name"}, "crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::", "href": "href"}, "created_at": "2019-01-01T12:00:00.000Z", "target_account": "target_account", "modified_at": "2019-01-01T12:00:00.000Z", "definition": {"name": "name", "description": "description", "authorizations": {"trusted_profile_id": "trusted_profile_id", "method": "api_key", "api_key": "api_key"}, "inputs": {}, "compliance_profile": {"id": "id", "instance_id": "instance_id", "instance_location": "instance_location", "attachment_id": "attachment_id", "profile_name": "profile_name"}}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_project_environments(**req_copy)

    def test_list_project_environments_value_error_with_retries(self):
        # Enable retries and run test_list_project_environments_value_error.
        _service.enable_retries()
        self.test_list_project_environments_value_error()

        # Disable retries and run test_list_project_environments_value_error.
        _service.disable_retries()
        self.test_list_project_environments_value_error()


class TestGetProjectEnvironment:
    """
    Test Class for get_project_environment
    """

    @responses.activate
    def test_get_project_environment_all_params(self):
        """
        get_project_environment()
        """
        # Set up mock
        url = preprocess_url('/v1/projects/testString/environments/testString')
        mock_response = '{"id": "id", "project": {"id": "id", "definition": {"name": "name"}, "crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::", "href": "href"}, "created_at": "2019-01-01T12:00:00.000Z", "target_account": "target_account", "modified_at": "2019-01-01T12:00:00.000Z", "definition": {"name": "name", "description": "description", "authorizations": {"trusted_profile_id": "trusted_profile_id", "method": "api_key", "api_key": "api_key"}, "inputs": {}, "compliance_profile": {"id": "id", "instance_id": "instance_id", "instance_location": "instance_location", "attachment_id": "attachment_id", "profile_name": "profile_name"}}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = 'testString'
        id = 'testString'

        # Invoke method
        response = _service.get_project_environment(
            project_id,
            id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_project_environment_all_params_with_retries(self):
        # Enable retries and run test_get_project_environment_all_params.
        _service.enable_retries()
        self.test_get_project_environment_all_params()

        # Disable retries and run test_get_project_environment_all_params.
        _service.disable_retries()
        self.test_get_project_environment_all_params()

    @responses.activate
    def test_get_project_environment_value_error(self):
        """
        test_get_project_environment_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/projects/testString/environments/testString')
        mock_response = '{"id": "id", "project": {"id": "id", "definition": {"name": "name"}, "crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::", "href": "href"}, "created_at": "2019-01-01T12:00:00.000Z", "target_account": "target_account", "modified_at": "2019-01-01T12:00:00.000Z", "definition": {"name": "name", "description": "description", "authorizations": {"trusted_profile_id": "trusted_profile_id", "method": "api_key", "api_key": "api_key"}, "inputs": {}, "compliance_profile": {"id": "id", "instance_id": "instance_id", "instance_location": "instance_location", "attachment_id": "attachment_id", "profile_name": "profile_name"}}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = 'testString'
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_project_environment(**req_copy)

    def test_get_project_environment_value_error_with_retries(self):
        # Enable retries and run test_get_project_environment_value_error.
        _service.enable_retries()
        self.test_get_project_environment_value_error()

        # Disable retries and run test_get_project_environment_value_error.
        _service.disable_retries()
        self.test_get_project_environment_value_error()


class TestUpdateProjectEnvironment:
    """
    Test Class for update_project_environment
    """

    @responses.activate
    def test_update_project_environment_all_params(self):
        """
        update_project_environment()
        """
        # Set up mock
        url = preprocess_url('/v1/projects/testString/environments/testString')
        mock_response = '{"id": "id", "project": {"id": "id", "definition": {"name": "name"}, "crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::", "href": "href"}, "created_at": "2019-01-01T12:00:00.000Z", "target_account": "target_account", "modified_at": "2019-01-01T12:00:00.000Z", "definition": {"name": "name", "description": "description", "authorizations": {"trusted_profile_id": "trusted_profile_id", "method": "api_key", "api_key": "api_key"}, "inputs": {}, "compliance_profile": {"id": "id", "instance_id": "instance_id", "instance_location": "instance_location", "attachment_id": "attachment_id", "profile_name": "profile_name"}}}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a ProjectConfigAuth model
        project_config_auth_model = {}
        project_config_auth_model['trusted_profile_id'] = 'testString'
        project_config_auth_model['method'] = 'api_key'
        project_config_auth_model['api_key'] = 'TbcdlprpFODhkpns9e0daOWnAwd2tXwSYtPn8rpEd8d9'

        # Construct a dict representation of a InputVariable model
        input_variable_model = {}
        input_variable_model['resource_group'] = 'stage'
        input_variable_model['region'] = 'us-south'

        # Construct a dict representation of a ProjectComplianceProfile model
        project_compliance_profile_model = {}
        project_compliance_profile_model['id'] = 'some-profile-id'
        project_compliance_profile_model['instance_id'] = 'some-instance-id'
        project_compliance_profile_model['instance_location'] = 'us-south'
        project_compliance_profile_model['attachment_id'] = 'some-attachment-id'
        project_compliance_profile_model['profile_name'] = 'some-profile-name'

        # Construct a dict representation of a EnvironmentDefinitionProperties model
        environment_definition_properties_model = {}
        environment_definition_properties_model['name'] = 'development'
        environment_definition_properties_model['description'] = 'The environment \'development\''
        environment_definition_properties_model['authorizations'] = project_config_auth_model
        environment_definition_properties_model['inputs'] = input_variable_model
        environment_definition_properties_model['compliance_profile'] = project_compliance_profile_model

        # Set up parameter values
        project_id = 'testString'
        id = 'testString'
        definition = environment_definition_properties_model

        # Invoke method
        response = _service.update_project_environment(
            project_id,
            id,
            definition,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['definition'] == environment_definition_properties_model

    def test_update_project_environment_all_params_with_retries(self):
        # Enable retries and run test_update_project_environment_all_params.
        _service.enable_retries()
        self.test_update_project_environment_all_params()

        # Disable retries and run test_update_project_environment_all_params.
        _service.disable_retries()
        self.test_update_project_environment_all_params()

    @responses.activate
    def test_update_project_environment_value_error(self):
        """
        test_update_project_environment_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/projects/testString/environments/testString')
        mock_response = '{"id": "id", "project": {"id": "id", "definition": {"name": "name"}, "crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::", "href": "href"}, "created_at": "2019-01-01T12:00:00.000Z", "target_account": "target_account", "modified_at": "2019-01-01T12:00:00.000Z", "definition": {"name": "name", "description": "description", "authorizations": {"trusted_profile_id": "trusted_profile_id", "method": "api_key", "api_key": "api_key"}, "inputs": {}, "compliance_profile": {"id": "id", "instance_id": "instance_id", "instance_location": "instance_location", "attachment_id": "attachment_id", "profile_name": "profile_name"}}}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a ProjectConfigAuth model
        project_config_auth_model = {}
        project_config_auth_model['trusted_profile_id'] = 'testString'
        project_config_auth_model['method'] = 'api_key'
        project_config_auth_model['api_key'] = 'TbcdlprpFODhkpns9e0daOWnAwd2tXwSYtPn8rpEd8d9'

        # Construct a dict representation of a InputVariable model
        input_variable_model = {}
        input_variable_model['resource_group'] = 'stage'
        input_variable_model['region'] = 'us-south'

        # Construct a dict representation of a ProjectComplianceProfile model
        project_compliance_profile_model = {}
        project_compliance_profile_model['id'] = 'some-profile-id'
        project_compliance_profile_model['instance_id'] = 'some-instance-id'
        project_compliance_profile_model['instance_location'] = 'us-south'
        project_compliance_profile_model['attachment_id'] = 'some-attachment-id'
        project_compliance_profile_model['profile_name'] = 'some-profile-name'

        # Construct a dict representation of a EnvironmentDefinitionProperties model
        environment_definition_properties_model = {}
        environment_definition_properties_model['name'] = 'development'
        environment_definition_properties_model['description'] = 'The environment \'development\''
        environment_definition_properties_model['authorizations'] = project_config_auth_model
        environment_definition_properties_model['inputs'] = input_variable_model
        environment_definition_properties_model['compliance_profile'] = project_compliance_profile_model

        # Set up parameter values
        project_id = 'testString'
        id = 'testString'
        definition = environment_definition_properties_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "id": id,
            "definition": definition,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_project_environment(**req_copy)

    def test_update_project_environment_value_error_with_retries(self):
        # Enable retries and run test_update_project_environment_value_error.
        _service.enable_retries()
        self.test_update_project_environment_value_error()

        # Disable retries and run test_update_project_environment_value_error.
        _service.disable_retries()
        self.test_update_project_environment_value_error()


class TestDeleteProjectEnvironment:
    """
    Test Class for delete_project_environment
    """

    @responses.activate
    def test_delete_project_environment_all_params(self):
        """
        delete_project_environment()
        """
        # Set up mock
        url = preprocess_url('/v1/projects/testString/environments/testString')
        mock_response = '{"id": "id"}'
        responses.add(
            responses.DELETE,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = 'testString'
        id = 'testString'

        # Invoke method
        response = _service.delete_project_environment(
            project_id,
            id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_delete_project_environment_all_params_with_retries(self):
        # Enable retries and run test_delete_project_environment_all_params.
        _service.enable_retries()
        self.test_delete_project_environment_all_params()

        # Disable retries and run test_delete_project_environment_all_params.
        _service.disable_retries()
        self.test_delete_project_environment_all_params()

    @responses.activate
    def test_delete_project_environment_value_error(self):
        """
        test_delete_project_environment_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/projects/testString/environments/testString')
        mock_response = '{"id": "id"}'
        responses.add(
            responses.DELETE,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = 'testString'
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_project_environment(**req_copy)

    def test_delete_project_environment_value_error_with_retries(self):
        # Enable retries and run test_delete_project_environment_value_error.
        _service.enable_retries()
        self.test_delete_project_environment_value_error()

        # Disable retries and run test_delete_project_environment_value_error.
        _service.disable_retries()
        self.test_delete_project_environment_value_error()


# endregion
##############################################################################
# End of Service: Environments
##############################################################################

##############################################################################
# Start of Service: Configurations
##############################################################################
# region


class TestNewInstance:
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = ProjectV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, ProjectV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = ProjectV1.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestCreateConfig:
    """
    Test Class for create_config
    """

    @responses.activate
    def test_create_config_all_params(self):
        """
        create_config()
        """
        # Set up mock
        url = preprocess_url('/v1/projects/testString/configs')
        mock_response = '{"id": "id", "version": 7, "is_draft": true, "needs_attention_state": ["anyValue"], "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "last_approved": {"at": "2019-01-01T12:00:00.000Z", "comment": "comment", "is_forced": false, "user_id": "user_id"}, "last_saved_at": "2019-01-01T12:00:00.000Z", "last_validated": {"href": "href", "result": "failed", "pre_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "post_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "job": {"id": "id", "summary": {"plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "sucess_message": ["sucess_message"], "update_message": ["update_message"], "destroy_message": ["destroy_message"]}, "apply_messages": {"error_messages": [{}], "sucess_message": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}, "cost_estimate": {"version": "version", "currency": "USD", "totalHourlyCost": "total_hourly_cost", "totalMonthlyCost": "total_monthly_cost", "pastTotalHourlyCost": "past_total_hourly_cost", "pastTotalMonthlyCost": "past_total_monthly_cost", "diffTotalHourlyCost": "diff_total_hourly_cost", "diffTotalMonthlyCost": "diff_total_monthly_cost", "timeGenerated": "2019-01-01T12:00:00.000Z", "user_id": "user_id"}, "cra_logs": {"cra_version": "cra_version", "schema_version": "schema_version", "status": "passed", "summary": {"total": "total", "passed": "passed", "failed": "failed", "skipped": "skipped"}, "timestamp": "2019-01-01T12:00:00.000Z"}}, "last_deployed": {"href": "href", "result": "failed", "pre_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "post_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "job": {"id": "id", "summary": {"plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "sucess_message": ["sucess_message"], "update_message": ["update_message"], "destroy_message": ["destroy_message"]}, "apply_messages": {"error_messages": [{}], "sucess_message": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}}, "last_undeployed": {"href": "href", "result": "failed", "pre_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "post_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "job": {"id": "id", "summary": {"plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "sucess_message": ["sucess_message"], "update_message": ["update_message"], "destroy_message": ["destroy_message"]}, "apply_messages": {"error_messages": [{}], "sucess_message": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}}, "outputs": [{"name": "name", "description": "description", "value": "anyValue"}], "project": {"id": "id", "definition": {"name": "name"}, "crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::", "href": "href"}, "references": {"anyKey": "anyValue"}, "schematics": {"workspace_crn": "workspace_crn"}, "state": "approved", "update_available": true, "definition": {"name": "name", "description": "description", "environment": "environment", "authorizations": {"trusted_profile_id": "trusted_profile_id", "method": "api_key", "api_key": "api_key"}, "compliance_profile": {"id": "id", "instance_id": "instance_id", "instance_location": "instance_location", "attachment_id": "attachment_id", "profile_name": "profile_name"}, "locator_id": "locator_id", "inputs": {}, "settings": {}, "type": "terraform_template"}, "approved_version": {"state": "approved", "version": 7, "href": "href"}, "deployed_version": {"state": "approved", "version": 7, "href": "href"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a ProjectConfigAuth model
        project_config_auth_model = {}
        project_config_auth_model['trusted_profile_id'] = 'testString'
        project_config_auth_model['method'] = 'api_key'
        project_config_auth_model['api_key'] = 'testString'

        # Construct a dict representation of a ProjectComplianceProfile model
        project_compliance_profile_model = {}
        project_compliance_profile_model['id'] = 'testString'
        project_compliance_profile_model['instance_id'] = 'testString'
        project_compliance_profile_model['instance_location'] = 'testString'
        project_compliance_profile_model['attachment_id'] = 'testString'
        project_compliance_profile_model['profile_name'] = 'testString'

        # Construct a dict representation of a InputVariable model
        input_variable_model = {}
        input_variable_model['account_id'] = '$configs[].name["account-stage"].inputs.account_id'
        input_variable_model['resource_group'] = 'stage'
        input_variable_model['access_tags'] = '["env:stage"]'
        input_variable_model['logdna_name'] = 'Name of the LogDNA stage service instance'
        input_variable_model['sysdig_name'] = 'Name of the SysDig stage service instance'

        # Construct a dict representation of a ProjectConfigSetting model
        project_config_setting_model = {}
        project_config_setting_model['IBMCLOUD_TOOLCHAIN_ENDPOINT'] = 'https://api.us-south.devops.dev.cloud.ibm.com'

        # Construct a dict representation of a ProjectConfigPrototypeDefinitionBlock model
        project_config_prototype_definition_block_model = {}
        project_config_prototype_definition_block_model['name'] = 'env-stage'
        project_config_prototype_definition_block_model['description'] = 'Stage environment configuration, which includes services common to all the environment regions. There must be a blueprint configuring all the services common to the stage regions. It is a terraform_template type of configuration that points to a Github repo hosting the terraform modules that can be deployed by a Schematics Workspace.'
        project_config_prototype_definition_block_model['environment'] = 'testString'
        project_config_prototype_definition_block_model['authorizations'] = project_config_auth_model
        project_config_prototype_definition_block_model['compliance_profile'] = project_compliance_profile_model
        project_config_prototype_definition_block_model['locator_id'] = '1082e7d2-5e2f-0a11-a3bc-f88a8e1931fc.018edf04-e772-4ca2-9785-03e8e03bef72-global'
        project_config_prototype_definition_block_model['inputs'] = input_variable_model
        project_config_prototype_definition_block_model['settings'] = project_config_setting_model

        # Construct a dict representation of a SchematicsWorkspace model
        schematics_workspace_model = {}
        schematics_workspace_model['workspace_crn'] = 'testString'

        # Set up parameter values
        project_id = 'testString'
        definition = project_config_prototype_definition_block_model
        schematics = schematics_workspace_model

        # Invoke method
        response = _service.create_config(
            project_id,
            definition,
            schematics=schematics,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['definition'] == project_config_prototype_definition_block_model
        assert req_body['schematics'] == schematics_workspace_model

    def test_create_config_all_params_with_retries(self):
        # Enable retries and run test_create_config_all_params.
        _service.enable_retries()
        self.test_create_config_all_params()

        # Disable retries and run test_create_config_all_params.
        _service.disable_retries()
        self.test_create_config_all_params()

    @responses.activate
    def test_create_config_value_error(self):
        """
        test_create_config_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/projects/testString/configs')
        mock_response = '{"id": "id", "version": 7, "is_draft": true, "needs_attention_state": ["anyValue"], "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "last_approved": {"at": "2019-01-01T12:00:00.000Z", "comment": "comment", "is_forced": false, "user_id": "user_id"}, "last_saved_at": "2019-01-01T12:00:00.000Z", "last_validated": {"href": "href", "result": "failed", "pre_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "post_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "job": {"id": "id", "summary": {"plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "sucess_message": ["sucess_message"], "update_message": ["update_message"], "destroy_message": ["destroy_message"]}, "apply_messages": {"error_messages": [{}], "sucess_message": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}, "cost_estimate": {"version": "version", "currency": "USD", "totalHourlyCost": "total_hourly_cost", "totalMonthlyCost": "total_monthly_cost", "pastTotalHourlyCost": "past_total_hourly_cost", "pastTotalMonthlyCost": "past_total_monthly_cost", "diffTotalHourlyCost": "diff_total_hourly_cost", "diffTotalMonthlyCost": "diff_total_monthly_cost", "timeGenerated": "2019-01-01T12:00:00.000Z", "user_id": "user_id"}, "cra_logs": {"cra_version": "cra_version", "schema_version": "schema_version", "status": "passed", "summary": {"total": "total", "passed": "passed", "failed": "failed", "skipped": "skipped"}, "timestamp": "2019-01-01T12:00:00.000Z"}}, "last_deployed": {"href": "href", "result": "failed", "pre_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "post_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "job": {"id": "id", "summary": {"plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "sucess_message": ["sucess_message"], "update_message": ["update_message"], "destroy_message": ["destroy_message"]}, "apply_messages": {"error_messages": [{}], "sucess_message": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}}, "last_undeployed": {"href": "href", "result": "failed", "pre_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "post_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "job": {"id": "id", "summary": {"plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "sucess_message": ["sucess_message"], "update_message": ["update_message"], "destroy_message": ["destroy_message"]}, "apply_messages": {"error_messages": [{}], "sucess_message": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}}, "outputs": [{"name": "name", "description": "description", "value": "anyValue"}], "project": {"id": "id", "definition": {"name": "name"}, "crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::", "href": "href"}, "references": {"anyKey": "anyValue"}, "schematics": {"workspace_crn": "workspace_crn"}, "state": "approved", "update_available": true, "definition": {"name": "name", "description": "description", "environment": "environment", "authorizations": {"trusted_profile_id": "trusted_profile_id", "method": "api_key", "api_key": "api_key"}, "compliance_profile": {"id": "id", "instance_id": "instance_id", "instance_location": "instance_location", "attachment_id": "attachment_id", "profile_name": "profile_name"}, "locator_id": "locator_id", "inputs": {}, "settings": {}, "type": "terraform_template"}, "approved_version": {"state": "approved", "version": 7, "href": "href"}, "deployed_version": {"state": "approved", "version": 7, "href": "href"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a ProjectConfigAuth model
        project_config_auth_model = {}
        project_config_auth_model['trusted_profile_id'] = 'testString'
        project_config_auth_model['method'] = 'api_key'
        project_config_auth_model['api_key'] = 'testString'

        # Construct a dict representation of a ProjectComplianceProfile model
        project_compliance_profile_model = {}
        project_compliance_profile_model['id'] = 'testString'
        project_compliance_profile_model['instance_id'] = 'testString'
        project_compliance_profile_model['instance_location'] = 'testString'
        project_compliance_profile_model['attachment_id'] = 'testString'
        project_compliance_profile_model['profile_name'] = 'testString'

        # Construct a dict representation of a InputVariable model
        input_variable_model = {}
        input_variable_model['account_id'] = '$configs[].name["account-stage"].inputs.account_id'
        input_variable_model['resource_group'] = 'stage'
        input_variable_model['access_tags'] = '["env:stage"]'
        input_variable_model['logdna_name'] = 'Name of the LogDNA stage service instance'
        input_variable_model['sysdig_name'] = 'Name of the SysDig stage service instance'

        # Construct a dict representation of a ProjectConfigSetting model
        project_config_setting_model = {}
        project_config_setting_model['IBMCLOUD_TOOLCHAIN_ENDPOINT'] = 'https://api.us-south.devops.dev.cloud.ibm.com'

        # Construct a dict representation of a ProjectConfigPrototypeDefinitionBlock model
        project_config_prototype_definition_block_model = {}
        project_config_prototype_definition_block_model['name'] = 'env-stage'
        project_config_prototype_definition_block_model['description'] = 'Stage environment configuration, which includes services common to all the environment regions. There must be a blueprint configuring all the services common to the stage regions. It is a terraform_template type of configuration that points to a Github repo hosting the terraform modules that can be deployed by a Schematics Workspace.'
        project_config_prototype_definition_block_model['environment'] = 'testString'
        project_config_prototype_definition_block_model['authorizations'] = project_config_auth_model
        project_config_prototype_definition_block_model['compliance_profile'] = project_compliance_profile_model
        project_config_prototype_definition_block_model['locator_id'] = '1082e7d2-5e2f-0a11-a3bc-f88a8e1931fc.018edf04-e772-4ca2-9785-03e8e03bef72-global'
        project_config_prototype_definition_block_model['inputs'] = input_variable_model
        project_config_prototype_definition_block_model['settings'] = project_config_setting_model

        # Construct a dict representation of a SchematicsWorkspace model
        schematics_workspace_model = {}
        schematics_workspace_model['workspace_crn'] = 'testString'

        # Set up parameter values
        project_id = 'testString'
        definition = project_config_prototype_definition_block_model
        schematics = schematics_workspace_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "definition": definition,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_config(**req_copy)

    def test_create_config_value_error_with_retries(self):
        # Enable retries and run test_create_config_value_error.
        _service.enable_retries()
        self.test_create_config_value_error()

        # Disable retries and run test_create_config_value_error.
        _service.disable_retries()
        self.test_create_config_value_error()


class TestListConfigs:
    """
    Test Class for list_configs
    """

    @responses.activate
    def test_list_configs_all_params(self):
        """
        list_configs()
        """
        # Set up mock
        url = preprocess_url('/v1/projects/testString/configs')
        mock_response = '{"configs": [{"approved_version": {"state": "approved", "version": 7, "href": "href"}, "deployed_version": {"state": "approved", "version": 7, "href": "href"}, "id": "id", "version": 7, "state": "approved", "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "href": "href", "definition": {"name": "name", "description": "description"}, "project": {"id": "id", "definition": {"name": "name"}, "crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::", "href": "href"}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = 'testString'

        # Invoke method
        response = _service.list_configs(
            project_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_configs_all_params_with_retries(self):
        # Enable retries and run test_list_configs_all_params.
        _service.enable_retries()
        self.test_list_configs_all_params()

        # Disable retries and run test_list_configs_all_params.
        _service.disable_retries()
        self.test_list_configs_all_params()

    @responses.activate
    def test_list_configs_value_error(self):
        """
        test_list_configs_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/projects/testString/configs')
        mock_response = '{"configs": [{"approved_version": {"state": "approved", "version": 7, "href": "href"}, "deployed_version": {"state": "approved", "version": 7, "href": "href"}, "id": "id", "version": 7, "state": "approved", "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "href": "href", "definition": {"name": "name", "description": "description"}, "project": {"id": "id", "definition": {"name": "name"}, "crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::", "href": "href"}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_configs(**req_copy)

    def test_list_configs_value_error_with_retries(self):
        # Enable retries and run test_list_configs_value_error.
        _service.enable_retries()
        self.test_list_configs_value_error()

        # Disable retries and run test_list_configs_value_error.
        _service.disable_retries()
        self.test_list_configs_value_error()


class TestGetConfig:
    """
    Test Class for get_config
    """

    @responses.activate
    def test_get_config_all_params(self):
        """
        get_config()
        """
        # Set up mock
        url = preprocess_url('/v1/projects/testString/configs/testString')
        mock_response = '{"id": "id", "version": 7, "is_draft": true, "needs_attention_state": ["anyValue"], "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "last_approved": {"at": "2019-01-01T12:00:00.000Z", "comment": "comment", "is_forced": false, "user_id": "user_id"}, "last_saved_at": "2019-01-01T12:00:00.000Z", "last_validated": {"href": "href", "result": "failed", "pre_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "post_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "job": {"id": "id", "summary": {"plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "sucess_message": ["sucess_message"], "update_message": ["update_message"], "destroy_message": ["destroy_message"]}, "apply_messages": {"error_messages": [{}], "sucess_message": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}, "cost_estimate": {"version": "version", "currency": "USD", "totalHourlyCost": "total_hourly_cost", "totalMonthlyCost": "total_monthly_cost", "pastTotalHourlyCost": "past_total_hourly_cost", "pastTotalMonthlyCost": "past_total_monthly_cost", "diffTotalHourlyCost": "diff_total_hourly_cost", "diffTotalMonthlyCost": "diff_total_monthly_cost", "timeGenerated": "2019-01-01T12:00:00.000Z", "user_id": "user_id"}, "cra_logs": {"cra_version": "cra_version", "schema_version": "schema_version", "status": "passed", "summary": {"total": "total", "passed": "passed", "failed": "failed", "skipped": "skipped"}, "timestamp": "2019-01-01T12:00:00.000Z"}}, "last_deployed": {"href": "href", "result": "failed", "pre_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "post_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "job": {"id": "id", "summary": {"plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "sucess_message": ["sucess_message"], "update_message": ["update_message"], "destroy_message": ["destroy_message"]}, "apply_messages": {"error_messages": [{}], "sucess_message": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}}, "last_undeployed": {"href": "href", "result": "failed", "pre_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "post_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "job": {"id": "id", "summary": {"plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "sucess_message": ["sucess_message"], "update_message": ["update_message"], "destroy_message": ["destroy_message"]}, "apply_messages": {"error_messages": [{}], "sucess_message": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}}, "outputs": [{"name": "name", "description": "description", "value": "anyValue"}], "project": {"id": "id", "definition": {"name": "name"}, "crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::", "href": "href"}, "references": {"anyKey": "anyValue"}, "schematics": {"workspace_crn": "workspace_crn"}, "state": "approved", "update_available": true, "definition": {"name": "name", "description": "description", "environment": "environment", "authorizations": {"trusted_profile_id": "trusted_profile_id", "method": "api_key", "api_key": "api_key"}, "compliance_profile": {"id": "id", "instance_id": "instance_id", "instance_location": "instance_location", "attachment_id": "attachment_id", "profile_name": "profile_name"}, "locator_id": "locator_id", "inputs": {}, "settings": {}, "type": "terraform_template"}, "approved_version": {"state": "approved", "version": 7, "href": "href"}, "deployed_version": {"state": "approved", "version": 7, "href": "href"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = 'testString'
        id = 'testString'

        # Invoke method
        response = _service.get_config(
            project_id,
            id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_config_all_params_with_retries(self):
        # Enable retries and run test_get_config_all_params.
        _service.enable_retries()
        self.test_get_config_all_params()

        # Disable retries and run test_get_config_all_params.
        _service.disable_retries()
        self.test_get_config_all_params()

    @responses.activate
    def test_get_config_value_error(self):
        """
        test_get_config_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/projects/testString/configs/testString')
        mock_response = '{"id": "id", "version": 7, "is_draft": true, "needs_attention_state": ["anyValue"], "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "last_approved": {"at": "2019-01-01T12:00:00.000Z", "comment": "comment", "is_forced": false, "user_id": "user_id"}, "last_saved_at": "2019-01-01T12:00:00.000Z", "last_validated": {"href": "href", "result": "failed", "pre_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "post_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "job": {"id": "id", "summary": {"plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "sucess_message": ["sucess_message"], "update_message": ["update_message"], "destroy_message": ["destroy_message"]}, "apply_messages": {"error_messages": [{}], "sucess_message": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}, "cost_estimate": {"version": "version", "currency": "USD", "totalHourlyCost": "total_hourly_cost", "totalMonthlyCost": "total_monthly_cost", "pastTotalHourlyCost": "past_total_hourly_cost", "pastTotalMonthlyCost": "past_total_monthly_cost", "diffTotalHourlyCost": "diff_total_hourly_cost", "diffTotalMonthlyCost": "diff_total_monthly_cost", "timeGenerated": "2019-01-01T12:00:00.000Z", "user_id": "user_id"}, "cra_logs": {"cra_version": "cra_version", "schema_version": "schema_version", "status": "passed", "summary": {"total": "total", "passed": "passed", "failed": "failed", "skipped": "skipped"}, "timestamp": "2019-01-01T12:00:00.000Z"}}, "last_deployed": {"href": "href", "result": "failed", "pre_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "post_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "job": {"id": "id", "summary": {"plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "sucess_message": ["sucess_message"], "update_message": ["update_message"], "destroy_message": ["destroy_message"]}, "apply_messages": {"error_messages": [{}], "sucess_message": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}}, "last_undeployed": {"href": "href", "result": "failed", "pre_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "post_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "job": {"id": "id", "summary": {"plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "sucess_message": ["sucess_message"], "update_message": ["update_message"], "destroy_message": ["destroy_message"]}, "apply_messages": {"error_messages": [{}], "sucess_message": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}}, "outputs": [{"name": "name", "description": "description", "value": "anyValue"}], "project": {"id": "id", "definition": {"name": "name"}, "crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::", "href": "href"}, "references": {"anyKey": "anyValue"}, "schematics": {"workspace_crn": "workspace_crn"}, "state": "approved", "update_available": true, "definition": {"name": "name", "description": "description", "environment": "environment", "authorizations": {"trusted_profile_id": "trusted_profile_id", "method": "api_key", "api_key": "api_key"}, "compliance_profile": {"id": "id", "instance_id": "instance_id", "instance_location": "instance_location", "attachment_id": "attachment_id", "profile_name": "profile_name"}, "locator_id": "locator_id", "inputs": {}, "settings": {}, "type": "terraform_template"}, "approved_version": {"state": "approved", "version": 7, "href": "href"}, "deployed_version": {"state": "approved", "version": 7, "href": "href"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = 'testString'
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_config(**req_copy)

    def test_get_config_value_error_with_retries(self):
        # Enable retries and run test_get_config_value_error.
        _service.enable_retries()
        self.test_get_config_value_error()

        # Disable retries and run test_get_config_value_error.
        _service.disable_retries()
        self.test_get_config_value_error()


class TestUpdateConfig:
    """
    Test Class for update_config
    """

    @responses.activate
    def test_update_config_all_params(self):
        """
        update_config()
        """
        # Set up mock
        url = preprocess_url('/v1/projects/testString/configs/testString')
        mock_response = '{"id": "id", "version": 7, "is_draft": true, "needs_attention_state": ["anyValue"], "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "last_approved": {"at": "2019-01-01T12:00:00.000Z", "comment": "comment", "is_forced": false, "user_id": "user_id"}, "last_saved_at": "2019-01-01T12:00:00.000Z", "last_validated": {"href": "href", "result": "failed", "pre_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "post_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "job": {"id": "id", "summary": {"plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "sucess_message": ["sucess_message"], "update_message": ["update_message"], "destroy_message": ["destroy_message"]}, "apply_messages": {"error_messages": [{}], "sucess_message": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}, "cost_estimate": {"version": "version", "currency": "USD", "totalHourlyCost": "total_hourly_cost", "totalMonthlyCost": "total_monthly_cost", "pastTotalHourlyCost": "past_total_hourly_cost", "pastTotalMonthlyCost": "past_total_monthly_cost", "diffTotalHourlyCost": "diff_total_hourly_cost", "diffTotalMonthlyCost": "diff_total_monthly_cost", "timeGenerated": "2019-01-01T12:00:00.000Z", "user_id": "user_id"}, "cra_logs": {"cra_version": "cra_version", "schema_version": "schema_version", "status": "passed", "summary": {"total": "total", "passed": "passed", "failed": "failed", "skipped": "skipped"}, "timestamp": "2019-01-01T12:00:00.000Z"}}, "last_deployed": {"href": "href", "result": "failed", "pre_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "post_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "job": {"id": "id", "summary": {"plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "sucess_message": ["sucess_message"], "update_message": ["update_message"], "destroy_message": ["destroy_message"]}, "apply_messages": {"error_messages": [{}], "sucess_message": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}}, "last_undeployed": {"href": "href", "result": "failed", "pre_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "post_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "job": {"id": "id", "summary": {"plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "sucess_message": ["sucess_message"], "update_message": ["update_message"], "destroy_message": ["destroy_message"]}, "apply_messages": {"error_messages": [{}], "sucess_message": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}}, "outputs": [{"name": "name", "description": "description", "value": "anyValue"}], "project": {"id": "id", "definition": {"name": "name"}, "crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::", "href": "href"}, "references": {"anyKey": "anyValue"}, "schematics": {"workspace_crn": "workspace_crn"}, "state": "approved", "update_available": true, "definition": {"name": "name", "description": "description", "environment": "environment", "authorizations": {"trusted_profile_id": "trusted_profile_id", "method": "api_key", "api_key": "api_key"}, "compliance_profile": {"id": "id", "instance_id": "instance_id", "instance_location": "instance_location", "attachment_id": "attachment_id", "profile_name": "profile_name"}, "locator_id": "locator_id", "inputs": {}, "settings": {}, "type": "terraform_template"}, "approved_version": {"state": "approved", "version": 7, "href": "href"}, "deployed_version": {"state": "approved", "version": 7, "href": "href"}}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a ProjectConfigAuth model
        project_config_auth_model = {}
        project_config_auth_model['trusted_profile_id'] = 'testString'
        project_config_auth_model['method'] = 'api_key'
        project_config_auth_model['api_key'] = 'testString'

        # Construct a dict representation of a ProjectComplianceProfile model
        project_compliance_profile_model = {}
        project_compliance_profile_model['id'] = 'testString'
        project_compliance_profile_model['instance_id'] = 'testString'
        project_compliance_profile_model['instance_location'] = 'testString'
        project_compliance_profile_model['attachment_id'] = 'testString'
        project_compliance_profile_model['profile_name'] = 'testString'

        # Construct a dict representation of a InputVariable model
        input_variable_model = {}
        input_variable_model['account_id'] = '$configs[].name["account-stage"].inputs.account_id'
        input_variable_model['resource_group'] = 'stage'
        input_variable_model['access_tags'] = '["env:stage"]'
        input_variable_model['logdna_name'] = 'Name of the LogDNA stage service instance'
        input_variable_model['sysdig_name'] = 'Name of the SysDig stage service instance'

        # Construct a dict representation of a ProjectConfigSetting model
        project_config_setting_model = {}
        project_config_setting_model['foo'] = 'testString'

        # Construct a dict representation of a ProjectConfigPatchDefinitionBlock model
        project_config_patch_definition_block_model = {}
        project_config_patch_definition_block_model['name'] = 'testString'
        project_config_patch_definition_block_model['description'] = 'testString'
        project_config_patch_definition_block_model['environment'] = 'testString'
        project_config_patch_definition_block_model['authorizations'] = project_config_auth_model
        project_config_patch_definition_block_model['compliance_profile'] = project_compliance_profile_model
        project_config_patch_definition_block_model['locator_id'] = 'testString'
        project_config_patch_definition_block_model['inputs'] = input_variable_model
        project_config_patch_definition_block_model['settings'] = project_config_setting_model

        # Set up parameter values
        project_id = 'testString'
        id = 'testString'
        definition = project_config_patch_definition_block_model

        # Invoke method
        response = _service.update_config(
            project_id,
            id,
            definition,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['definition'] == project_config_patch_definition_block_model

    def test_update_config_all_params_with_retries(self):
        # Enable retries and run test_update_config_all_params.
        _service.enable_retries()
        self.test_update_config_all_params()

        # Disable retries and run test_update_config_all_params.
        _service.disable_retries()
        self.test_update_config_all_params()

    @responses.activate
    def test_update_config_value_error(self):
        """
        test_update_config_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/projects/testString/configs/testString')
        mock_response = '{"id": "id", "version": 7, "is_draft": true, "needs_attention_state": ["anyValue"], "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "last_approved": {"at": "2019-01-01T12:00:00.000Z", "comment": "comment", "is_forced": false, "user_id": "user_id"}, "last_saved_at": "2019-01-01T12:00:00.000Z", "last_validated": {"href": "href", "result": "failed", "pre_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "post_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "job": {"id": "id", "summary": {"plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "sucess_message": ["sucess_message"], "update_message": ["update_message"], "destroy_message": ["destroy_message"]}, "apply_messages": {"error_messages": [{}], "sucess_message": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}, "cost_estimate": {"version": "version", "currency": "USD", "totalHourlyCost": "total_hourly_cost", "totalMonthlyCost": "total_monthly_cost", "pastTotalHourlyCost": "past_total_hourly_cost", "pastTotalMonthlyCost": "past_total_monthly_cost", "diffTotalHourlyCost": "diff_total_hourly_cost", "diffTotalMonthlyCost": "diff_total_monthly_cost", "timeGenerated": "2019-01-01T12:00:00.000Z", "user_id": "user_id"}, "cra_logs": {"cra_version": "cra_version", "schema_version": "schema_version", "status": "passed", "summary": {"total": "total", "passed": "passed", "failed": "failed", "skipped": "skipped"}, "timestamp": "2019-01-01T12:00:00.000Z"}}, "last_deployed": {"href": "href", "result": "failed", "pre_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "post_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "job": {"id": "id", "summary": {"plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "sucess_message": ["sucess_message"], "update_message": ["update_message"], "destroy_message": ["destroy_message"]}, "apply_messages": {"error_messages": [{}], "sucess_message": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}}, "last_undeployed": {"href": "href", "result": "failed", "pre_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "post_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "job": {"id": "id", "summary": {"plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "sucess_message": ["sucess_message"], "update_message": ["update_message"], "destroy_message": ["destroy_message"]}, "apply_messages": {"error_messages": [{}], "sucess_message": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}}, "outputs": [{"name": "name", "description": "description", "value": "anyValue"}], "project": {"id": "id", "definition": {"name": "name"}, "crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::", "href": "href"}, "references": {"anyKey": "anyValue"}, "schematics": {"workspace_crn": "workspace_crn"}, "state": "approved", "update_available": true, "definition": {"name": "name", "description": "description", "environment": "environment", "authorizations": {"trusted_profile_id": "trusted_profile_id", "method": "api_key", "api_key": "api_key"}, "compliance_profile": {"id": "id", "instance_id": "instance_id", "instance_location": "instance_location", "attachment_id": "attachment_id", "profile_name": "profile_name"}, "locator_id": "locator_id", "inputs": {}, "settings": {}, "type": "terraform_template"}, "approved_version": {"state": "approved", "version": 7, "href": "href"}, "deployed_version": {"state": "approved", "version": 7, "href": "href"}}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a ProjectConfigAuth model
        project_config_auth_model = {}
        project_config_auth_model['trusted_profile_id'] = 'testString'
        project_config_auth_model['method'] = 'api_key'
        project_config_auth_model['api_key'] = 'testString'

        # Construct a dict representation of a ProjectComplianceProfile model
        project_compliance_profile_model = {}
        project_compliance_profile_model['id'] = 'testString'
        project_compliance_profile_model['instance_id'] = 'testString'
        project_compliance_profile_model['instance_location'] = 'testString'
        project_compliance_profile_model['attachment_id'] = 'testString'
        project_compliance_profile_model['profile_name'] = 'testString'

        # Construct a dict representation of a InputVariable model
        input_variable_model = {}
        input_variable_model['account_id'] = '$configs[].name["account-stage"].inputs.account_id'
        input_variable_model['resource_group'] = 'stage'
        input_variable_model['access_tags'] = '["env:stage"]'
        input_variable_model['logdna_name'] = 'Name of the LogDNA stage service instance'
        input_variable_model['sysdig_name'] = 'Name of the SysDig stage service instance'

        # Construct a dict representation of a ProjectConfigSetting model
        project_config_setting_model = {}
        project_config_setting_model['foo'] = 'testString'

        # Construct a dict representation of a ProjectConfigPatchDefinitionBlock model
        project_config_patch_definition_block_model = {}
        project_config_patch_definition_block_model['name'] = 'testString'
        project_config_patch_definition_block_model['description'] = 'testString'
        project_config_patch_definition_block_model['environment'] = 'testString'
        project_config_patch_definition_block_model['authorizations'] = project_config_auth_model
        project_config_patch_definition_block_model['compliance_profile'] = project_compliance_profile_model
        project_config_patch_definition_block_model['locator_id'] = 'testString'
        project_config_patch_definition_block_model['inputs'] = input_variable_model
        project_config_patch_definition_block_model['settings'] = project_config_setting_model

        # Set up parameter values
        project_id = 'testString'
        id = 'testString'
        definition = project_config_patch_definition_block_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "id": id,
            "definition": definition,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_config(**req_copy)

    def test_update_config_value_error_with_retries(self):
        # Enable retries and run test_update_config_value_error.
        _service.enable_retries()
        self.test_update_config_value_error()

        # Disable retries and run test_update_config_value_error.
        _service.disable_retries()
        self.test_update_config_value_error()


class TestDeleteConfig:
    """
    Test Class for delete_config
    """

    @responses.activate
    def test_delete_config_all_params(self):
        """
        delete_config()
        """
        # Set up mock
        url = preprocess_url('/v1/projects/testString/configs/testString')
        mock_response = '{"id": "id"}'
        responses.add(
            responses.DELETE,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = 'testString'
        id = 'testString'

        # Invoke method
        response = _service.delete_config(
            project_id,
            id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_delete_config_all_params_with_retries(self):
        # Enable retries and run test_delete_config_all_params.
        _service.enable_retries()
        self.test_delete_config_all_params()

        # Disable retries and run test_delete_config_all_params.
        _service.disable_retries()
        self.test_delete_config_all_params()

    @responses.activate
    def test_delete_config_value_error(self):
        """
        test_delete_config_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/projects/testString/configs/testString')
        mock_response = '{"id": "id"}'
        responses.add(
            responses.DELETE,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = 'testString'
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_config(**req_copy)

    def test_delete_config_value_error_with_retries(self):
        # Enable retries and run test_delete_config_value_error.
        _service.enable_retries()
        self.test_delete_config_value_error()

        # Disable retries and run test_delete_config_value_error.
        _service.disable_retries()
        self.test_delete_config_value_error()


class TestForceApprove:
    """
    Test Class for force_approve
    """

    @responses.activate
    def test_force_approve_all_params(self):
        """
        force_approve()
        """
        # Set up mock
        url = preprocess_url('/v1/projects/testString/configs/testString/force_approve')
        mock_response = '{"id": "id", "version": 7, "is_draft": true, "needs_attention_state": ["anyValue"], "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "last_approved": {"at": "2019-01-01T12:00:00.000Z", "comment": "comment", "is_forced": false, "user_id": "user_id"}, "last_saved_at": "2019-01-01T12:00:00.000Z", "last_validated": {"href": "href", "result": "failed", "pre_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "post_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "job": {"id": "id", "summary": {"plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "sucess_message": ["sucess_message"], "update_message": ["update_message"], "destroy_message": ["destroy_message"]}, "apply_messages": {"error_messages": [{}], "sucess_message": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}, "cost_estimate": {"version": "version", "currency": "USD", "totalHourlyCost": "total_hourly_cost", "totalMonthlyCost": "total_monthly_cost", "pastTotalHourlyCost": "past_total_hourly_cost", "pastTotalMonthlyCost": "past_total_monthly_cost", "diffTotalHourlyCost": "diff_total_hourly_cost", "diffTotalMonthlyCost": "diff_total_monthly_cost", "timeGenerated": "2019-01-01T12:00:00.000Z", "user_id": "user_id"}, "cra_logs": {"cra_version": "cra_version", "schema_version": "schema_version", "status": "passed", "summary": {"total": "total", "passed": "passed", "failed": "failed", "skipped": "skipped"}, "timestamp": "2019-01-01T12:00:00.000Z"}}, "last_deployed": {"href": "href", "result": "failed", "pre_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "post_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "job": {"id": "id", "summary": {"plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "sucess_message": ["sucess_message"], "update_message": ["update_message"], "destroy_message": ["destroy_message"]}, "apply_messages": {"error_messages": [{}], "sucess_message": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}}, "last_undeployed": {"href": "href", "result": "failed", "pre_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "post_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "job": {"id": "id", "summary": {"plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "sucess_message": ["sucess_message"], "update_message": ["update_message"], "destroy_message": ["destroy_message"]}, "apply_messages": {"error_messages": [{}], "sucess_message": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}}, "outputs": [{"name": "name", "description": "description", "value": "anyValue"}], "project": {"id": "id", "definition": {"name": "name"}, "crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::", "href": "href"}, "references": {"anyKey": "anyValue"}, "schematics": {"workspace_crn": "workspace_crn"}, "state": "approved", "update_available": true, "definition": {"name": "name", "description": "description", "environment": "environment", "authorizations": {"trusted_profile_id": "trusted_profile_id", "method": "api_key", "api_key": "api_key"}, "compliance_profile": {"id": "id", "instance_id": "instance_id", "instance_location": "instance_location", "attachment_id": "attachment_id", "profile_name": "profile_name"}, "locator_id": "locator_id", "inputs": {}, "settings": {}, "type": "terraform_template"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        project_id = 'testString'
        id = 'testString'
        comment = 'Approving the changes'

        # Invoke method
        response = _service.force_approve(
            project_id,
            id,
            comment=comment,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['comment'] == 'Approving the changes'

    def test_force_approve_all_params_with_retries(self):
        # Enable retries and run test_force_approve_all_params.
        _service.enable_retries()
        self.test_force_approve_all_params()

        # Disable retries and run test_force_approve_all_params.
        _service.disable_retries()
        self.test_force_approve_all_params()

    @responses.activate
    def test_force_approve_value_error(self):
        """
        test_force_approve_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/projects/testString/configs/testString/force_approve')
        mock_response = '{"id": "id", "version": 7, "is_draft": true, "needs_attention_state": ["anyValue"], "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "last_approved": {"at": "2019-01-01T12:00:00.000Z", "comment": "comment", "is_forced": false, "user_id": "user_id"}, "last_saved_at": "2019-01-01T12:00:00.000Z", "last_validated": {"href": "href", "result": "failed", "pre_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "post_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "job": {"id": "id", "summary": {"plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "sucess_message": ["sucess_message"], "update_message": ["update_message"], "destroy_message": ["destroy_message"]}, "apply_messages": {"error_messages": [{}], "sucess_message": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}, "cost_estimate": {"version": "version", "currency": "USD", "totalHourlyCost": "total_hourly_cost", "totalMonthlyCost": "total_monthly_cost", "pastTotalHourlyCost": "past_total_hourly_cost", "pastTotalMonthlyCost": "past_total_monthly_cost", "diffTotalHourlyCost": "diff_total_hourly_cost", "diffTotalMonthlyCost": "diff_total_monthly_cost", "timeGenerated": "2019-01-01T12:00:00.000Z", "user_id": "user_id"}, "cra_logs": {"cra_version": "cra_version", "schema_version": "schema_version", "status": "passed", "summary": {"total": "total", "passed": "passed", "failed": "failed", "skipped": "skipped"}, "timestamp": "2019-01-01T12:00:00.000Z"}}, "last_deployed": {"href": "href", "result": "failed", "pre_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "post_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "job": {"id": "id", "summary": {"plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "sucess_message": ["sucess_message"], "update_message": ["update_message"], "destroy_message": ["destroy_message"]}, "apply_messages": {"error_messages": [{}], "sucess_message": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}}, "last_undeployed": {"href": "href", "result": "failed", "pre_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "post_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "job": {"id": "id", "summary": {"plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "sucess_message": ["sucess_message"], "update_message": ["update_message"], "destroy_message": ["destroy_message"]}, "apply_messages": {"error_messages": [{}], "sucess_message": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}}, "outputs": [{"name": "name", "description": "description", "value": "anyValue"}], "project": {"id": "id", "definition": {"name": "name"}, "crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::", "href": "href"}, "references": {"anyKey": "anyValue"}, "schematics": {"workspace_crn": "workspace_crn"}, "state": "approved", "update_available": true, "definition": {"name": "name", "description": "description", "environment": "environment", "authorizations": {"trusted_profile_id": "trusted_profile_id", "method": "api_key", "api_key": "api_key"}, "compliance_profile": {"id": "id", "instance_id": "instance_id", "instance_location": "instance_location", "attachment_id": "attachment_id", "profile_name": "profile_name"}, "locator_id": "locator_id", "inputs": {}, "settings": {}, "type": "terraform_template"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        project_id = 'testString'
        id = 'testString'
        comment = 'Approving the changes'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.force_approve(**req_copy)

    def test_force_approve_value_error_with_retries(self):
        # Enable retries and run test_force_approve_value_error.
        _service.enable_retries()
        self.test_force_approve_value_error()

        # Disable retries and run test_force_approve_value_error.
        _service.disable_retries()
        self.test_force_approve_value_error()


class TestApprove:
    """
    Test Class for approve
    """

    @responses.activate
    def test_approve_all_params(self):
        """
        approve()
        """
        # Set up mock
        url = preprocess_url('/v1/projects/testString/configs/testString/approve')
        mock_response = '{"id": "id", "version": 7, "is_draft": true, "needs_attention_state": ["anyValue"], "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "last_approved": {"at": "2019-01-01T12:00:00.000Z", "comment": "comment", "is_forced": false, "user_id": "user_id"}, "last_saved_at": "2019-01-01T12:00:00.000Z", "last_validated": {"href": "href", "result": "failed", "pre_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "post_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "job": {"id": "id", "summary": {"plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "sucess_message": ["sucess_message"], "update_message": ["update_message"], "destroy_message": ["destroy_message"]}, "apply_messages": {"error_messages": [{}], "sucess_message": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}, "cost_estimate": {"version": "version", "currency": "USD", "totalHourlyCost": "total_hourly_cost", "totalMonthlyCost": "total_monthly_cost", "pastTotalHourlyCost": "past_total_hourly_cost", "pastTotalMonthlyCost": "past_total_monthly_cost", "diffTotalHourlyCost": "diff_total_hourly_cost", "diffTotalMonthlyCost": "diff_total_monthly_cost", "timeGenerated": "2019-01-01T12:00:00.000Z", "user_id": "user_id"}, "cra_logs": {"cra_version": "cra_version", "schema_version": "schema_version", "status": "passed", "summary": {"total": "total", "passed": "passed", "failed": "failed", "skipped": "skipped"}, "timestamp": "2019-01-01T12:00:00.000Z"}}, "last_deployed": {"href": "href", "result": "failed", "pre_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "post_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "job": {"id": "id", "summary": {"plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "sucess_message": ["sucess_message"], "update_message": ["update_message"], "destroy_message": ["destroy_message"]}, "apply_messages": {"error_messages": [{}], "sucess_message": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}}, "last_undeployed": {"href": "href", "result": "failed", "pre_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "post_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "job": {"id": "id", "summary": {"plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "sucess_message": ["sucess_message"], "update_message": ["update_message"], "destroy_message": ["destroy_message"]}, "apply_messages": {"error_messages": [{}], "sucess_message": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}}, "outputs": [{"name": "name", "description": "description", "value": "anyValue"}], "project": {"id": "id", "definition": {"name": "name"}, "crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::", "href": "href"}, "references": {"anyKey": "anyValue"}, "schematics": {"workspace_crn": "workspace_crn"}, "state": "approved", "update_available": true, "definition": {"name": "name", "description": "description", "environment": "environment", "authorizations": {"trusted_profile_id": "trusted_profile_id", "method": "api_key", "api_key": "api_key"}, "compliance_profile": {"id": "id", "instance_id": "instance_id", "instance_location": "instance_location", "attachment_id": "attachment_id", "profile_name": "profile_name"}, "locator_id": "locator_id", "inputs": {}, "settings": {}, "type": "terraform_template"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        project_id = 'testString'
        id = 'testString'
        comment = 'Approving the changes'

        # Invoke method
        response = _service.approve(
            project_id,
            id,
            comment=comment,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['comment'] == 'Approving the changes'

    def test_approve_all_params_with_retries(self):
        # Enable retries and run test_approve_all_params.
        _service.enable_retries()
        self.test_approve_all_params()

        # Disable retries and run test_approve_all_params.
        _service.disable_retries()
        self.test_approve_all_params()

    @responses.activate
    def test_approve_required_params(self):
        """
        test_approve_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/projects/testString/configs/testString/approve')
        mock_response = '{"id": "id", "version": 7, "is_draft": true, "needs_attention_state": ["anyValue"], "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "last_approved": {"at": "2019-01-01T12:00:00.000Z", "comment": "comment", "is_forced": false, "user_id": "user_id"}, "last_saved_at": "2019-01-01T12:00:00.000Z", "last_validated": {"href": "href", "result": "failed", "pre_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "post_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "job": {"id": "id", "summary": {"plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "sucess_message": ["sucess_message"], "update_message": ["update_message"], "destroy_message": ["destroy_message"]}, "apply_messages": {"error_messages": [{}], "sucess_message": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}, "cost_estimate": {"version": "version", "currency": "USD", "totalHourlyCost": "total_hourly_cost", "totalMonthlyCost": "total_monthly_cost", "pastTotalHourlyCost": "past_total_hourly_cost", "pastTotalMonthlyCost": "past_total_monthly_cost", "diffTotalHourlyCost": "diff_total_hourly_cost", "diffTotalMonthlyCost": "diff_total_monthly_cost", "timeGenerated": "2019-01-01T12:00:00.000Z", "user_id": "user_id"}, "cra_logs": {"cra_version": "cra_version", "schema_version": "schema_version", "status": "passed", "summary": {"total": "total", "passed": "passed", "failed": "failed", "skipped": "skipped"}, "timestamp": "2019-01-01T12:00:00.000Z"}}, "last_deployed": {"href": "href", "result": "failed", "pre_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "post_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "job": {"id": "id", "summary": {"plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "sucess_message": ["sucess_message"], "update_message": ["update_message"], "destroy_message": ["destroy_message"]}, "apply_messages": {"error_messages": [{}], "sucess_message": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}}, "last_undeployed": {"href": "href", "result": "failed", "pre_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "post_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "job": {"id": "id", "summary": {"plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "sucess_message": ["sucess_message"], "update_message": ["update_message"], "destroy_message": ["destroy_message"]}, "apply_messages": {"error_messages": [{}], "sucess_message": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}}, "outputs": [{"name": "name", "description": "description", "value": "anyValue"}], "project": {"id": "id", "definition": {"name": "name"}, "crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::", "href": "href"}, "references": {"anyKey": "anyValue"}, "schematics": {"workspace_crn": "workspace_crn"}, "state": "approved", "update_available": true, "definition": {"name": "name", "description": "description", "environment": "environment", "authorizations": {"trusted_profile_id": "trusted_profile_id", "method": "api_key", "api_key": "api_key"}, "compliance_profile": {"id": "id", "instance_id": "instance_id", "instance_location": "instance_location", "attachment_id": "attachment_id", "profile_name": "profile_name"}, "locator_id": "locator_id", "inputs": {}, "settings": {}, "type": "terraform_template"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        project_id = 'testString'
        id = 'testString'

        # Invoke method
        response = _service.approve(
            project_id,
            id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201

    def test_approve_required_params_with_retries(self):
        # Enable retries and run test_approve_required_params.
        _service.enable_retries()
        self.test_approve_required_params()

        # Disable retries and run test_approve_required_params.
        _service.disable_retries()
        self.test_approve_required_params()

    @responses.activate
    def test_approve_value_error(self):
        """
        test_approve_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/projects/testString/configs/testString/approve')
        mock_response = '{"id": "id", "version": 7, "is_draft": true, "needs_attention_state": ["anyValue"], "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "last_approved": {"at": "2019-01-01T12:00:00.000Z", "comment": "comment", "is_forced": false, "user_id": "user_id"}, "last_saved_at": "2019-01-01T12:00:00.000Z", "last_validated": {"href": "href", "result": "failed", "pre_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "post_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "job": {"id": "id", "summary": {"plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "sucess_message": ["sucess_message"], "update_message": ["update_message"], "destroy_message": ["destroy_message"]}, "apply_messages": {"error_messages": [{}], "sucess_message": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}, "cost_estimate": {"version": "version", "currency": "USD", "totalHourlyCost": "total_hourly_cost", "totalMonthlyCost": "total_monthly_cost", "pastTotalHourlyCost": "past_total_hourly_cost", "pastTotalMonthlyCost": "past_total_monthly_cost", "diffTotalHourlyCost": "diff_total_hourly_cost", "diffTotalMonthlyCost": "diff_total_monthly_cost", "timeGenerated": "2019-01-01T12:00:00.000Z", "user_id": "user_id"}, "cra_logs": {"cra_version": "cra_version", "schema_version": "schema_version", "status": "passed", "summary": {"total": "total", "passed": "passed", "failed": "failed", "skipped": "skipped"}, "timestamp": "2019-01-01T12:00:00.000Z"}}, "last_deployed": {"href": "href", "result": "failed", "pre_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "post_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "job": {"id": "id", "summary": {"plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "sucess_message": ["sucess_message"], "update_message": ["update_message"], "destroy_message": ["destroy_message"]}, "apply_messages": {"error_messages": [{}], "sucess_message": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}}, "last_undeployed": {"href": "href", "result": "failed", "pre_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "post_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "job": {"id": "id", "summary": {"plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "sucess_message": ["sucess_message"], "update_message": ["update_message"], "destroy_message": ["destroy_message"]}, "apply_messages": {"error_messages": [{}], "sucess_message": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}}, "outputs": [{"name": "name", "description": "description", "value": "anyValue"}], "project": {"id": "id", "definition": {"name": "name"}, "crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::", "href": "href"}, "references": {"anyKey": "anyValue"}, "schematics": {"workspace_crn": "workspace_crn"}, "state": "approved", "update_available": true, "definition": {"name": "name", "description": "description", "environment": "environment", "authorizations": {"trusted_profile_id": "trusted_profile_id", "method": "api_key", "api_key": "api_key"}, "compliance_profile": {"id": "id", "instance_id": "instance_id", "instance_location": "instance_location", "attachment_id": "attachment_id", "profile_name": "profile_name"}, "locator_id": "locator_id", "inputs": {}, "settings": {}, "type": "terraform_template"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        project_id = 'testString'
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.approve(**req_copy)

    def test_approve_value_error_with_retries(self):
        # Enable retries and run test_approve_value_error.
        _service.enable_retries()
        self.test_approve_value_error()

        # Disable retries and run test_approve_value_error.
        _service.disable_retries()
        self.test_approve_value_error()


class TestValidateConfig:
    """
    Test Class for validate_config
    """

    @responses.activate
    def test_validate_config_all_params(self):
        """
        validate_config()
        """
        # Set up mock
        url = preprocess_url('/v1/projects/testString/configs/testString/validate')
        mock_response = '{"id": "id", "version": 7, "is_draft": true, "needs_attention_state": ["anyValue"], "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "last_approved": {"at": "2019-01-01T12:00:00.000Z", "comment": "comment", "is_forced": false, "user_id": "user_id"}, "last_saved_at": "2019-01-01T12:00:00.000Z", "last_validated": {"href": "href", "result": "failed", "pre_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "post_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "job": {"id": "id", "summary": {"plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "sucess_message": ["sucess_message"], "update_message": ["update_message"], "destroy_message": ["destroy_message"]}, "apply_messages": {"error_messages": [{}], "sucess_message": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}, "cost_estimate": {"version": "version", "currency": "USD", "totalHourlyCost": "total_hourly_cost", "totalMonthlyCost": "total_monthly_cost", "pastTotalHourlyCost": "past_total_hourly_cost", "pastTotalMonthlyCost": "past_total_monthly_cost", "diffTotalHourlyCost": "diff_total_hourly_cost", "diffTotalMonthlyCost": "diff_total_monthly_cost", "timeGenerated": "2019-01-01T12:00:00.000Z", "user_id": "user_id"}, "cra_logs": {"cra_version": "cra_version", "schema_version": "schema_version", "status": "passed", "summary": {"total": "total", "passed": "passed", "failed": "failed", "skipped": "skipped"}, "timestamp": "2019-01-01T12:00:00.000Z"}}, "last_deployed": {"href": "href", "result": "failed", "pre_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "post_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "job": {"id": "id", "summary": {"plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "sucess_message": ["sucess_message"], "update_message": ["update_message"], "destroy_message": ["destroy_message"]}, "apply_messages": {"error_messages": [{}], "sucess_message": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}}, "last_undeployed": {"href": "href", "result": "failed", "pre_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "post_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "job": {"id": "id", "summary": {"plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "sucess_message": ["sucess_message"], "update_message": ["update_message"], "destroy_message": ["destroy_message"]}, "apply_messages": {"error_messages": [{}], "sucess_message": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}}, "outputs": [{"name": "name", "description": "description", "value": "anyValue"}], "project": {"id": "id", "definition": {"name": "name"}, "crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::", "href": "href"}, "references": {"anyKey": "anyValue"}, "schematics": {"workspace_crn": "workspace_crn"}, "state": "approved", "update_available": true, "definition": {"name": "name", "description": "description", "environment": "environment", "authorizations": {"trusted_profile_id": "trusted_profile_id", "method": "api_key", "api_key": "api_key"}, "compliance_profile": {"id": "id", "instance_id": "instance_id", "instance_location": "instance_location", "attachment_id": "attachment_id", "profile_name": "profile_name"}, "locator_id": "locator_id", "inputs": {}, "settings": {}, "type": "terraform_template"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=202,
        )

        # Set up parameter values
        project_id = 'testString'
        id = 'testString'

        # Invoke method
        response = _service.validate_config(
            project_id,
            id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202

    def test_validate_config_all_params_with_retries(self):
        # Enable retries and run test_validate_config_all_params.
        _service.enable_retries()
        self.test_validate_config_all_params()

        # Disable retries and run test_validate_config_all_params.
        _service.disable_retries()
        self.test_validate_config_all_params()

    @responses.activate
    def test_validate_config_value_error(self):
        """
        test_validate_config_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/projects/testString/configs/testString/validate')
        mock_response = '{"id": "id", "version": 7, "is_draft": true, "needs_attention_state": ["anyValue"], "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "last_approved": {"at": "2019-01-01T12:00:00.000Z", "comment": "comment", "is_forced": false, "user_id": "user_id"}, "last_saved_at": "2019-01-01T12:00:00.000Z", "last_validated": {"href": "href", "result": "failed", "pre_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "post_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "job": {"id": "id", "summary": {"plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "sucess_message": ["sucess_message"], "update_message": ["update_message"], "destroy_message": ["destroy_message"]}, "apply_messages": {"error_messages": [{}], "sucess_message": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}, "cost_estimate": {"version": "version", "currency": "USD", "totalHourlyCost": "total_hourly_cost", "totalMonthlyCost": "total_monthly_cost", "pastTotalHourlyCost": "past_total_hourly_cost", "pastTotalMonthlyCost": "past_total_monthly_cost", "diffTotalHourlyCost": "diff_total_hourly_cost", "diffTotalMonthlyCost": "diff_total_monthly_cost", "timeGenerated": "2019-01-01T12:00:00.000Z", "user_id": "user_id"}, "cra_logs": {"cra_version": "cra_version", "schema_version": "schema_version", "status": "passed", "summary": {"total": "total", "passed": "passed", "failed": "failed", "skipped": "skipped"}, "timestamp": "2019-01-01T12:00:00.000Z"}}, "last_deployed": {"href": "href", "result": "failed", "pre_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "post_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "job": {"id": "id", "summary": {"plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "sucess_message": ["sucess_message"], "update_message": ["update_message"], "destroy_message": ["destroy_message"]}, "apply_messages": {"error_messages": [{}], "sucess_message": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}}, "last_undeployed": {"href": "href", "result": "failed", "pre_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "post_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "job": {"id": "id", "summary": {"plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "sucess_message": ["sucess_message"], "update_message": ["update_message"], "destroy_message": ["destroy_message"]}, "apply_messages": {"error_messages": [{}], "sucess_message": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}}, "outputs": [{"name": "name", "description": "description", "value": "anyValue"}], "project": {"id": "id", "definition": {"name": "name"}, "crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::", "href": "href"}, "references": {"anyKey": "anyValue"}, "schematics": {"workspace_crn": "workspace_crn"}, "state": "approved", "update_available": true, "definition": {"name": "name", "description": "description", "environment": "environment", "authorizations": {"trusted_profile_id": "trusted_profile_id", "method": "api_key", "api_key": "api_key"}, "compliance_profile": {"id": "id", "instance_id": "instance_id", "instance_location": "instance_location", "attachment_id": "attachment_id", "profile_name": "profile_name"}, "locator_id": "locator_id", "inputs": {}, "settings": {}, "type": "terraform_template"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=202,
        )

        # Set up parameter values
        project_id = 'testString'
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.validate_config(**req_copy)

    def test_validate_config_value_error_with_retries(self):
        # Enable retries and run test_validate_config_value_error.
        _service.enable_retries()
        self.test_validate_config_value_error()

        # Disable retries and run test_validate_config_value_error.
        _service.disable_retries()
        self.test_validate_config_value_error()


class TestDeployConfig:
    """
    Test Class for deploy_config
    """

    @responses.activate
    def test_deploy_config_all_params(self):
        """
        deploy_config()
        """
        # Set up mock
        url = preprocess_url('/v1/projects/testString/configs/testString/deploy')
        mock_response = '{"id": "id", "version": 7, "is_draft": true, "needs_attention_state": ["anyValue"], "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "last_approved": {"at": "2019-01-01T12:00:00.000Z", "comment": "comment", "is_forced": false, "user_id": "user_id"}, "last_saved_at": "2019-01-01T12:00:00.000Z", "last_validated": {"href": "href", "result": "failed", "pre_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "post_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "job": {"id": "id", "summary": {"plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "sucess_message": ["sucess_message"], "update_message": ["update_message"], "destroy_message": ["destroy_message"]}, "apply_messages": {"error_messages": [{}], "sucess_message": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}, "cost_estimate": {"version": "version", "currency": "USD", "totalHourlyCost": "total_hourly_cost", "totalMonthlyCost": "total_monthly_cost", "pastTotalHourlyCost": "past_total_hourly_cost", "pastTotalMonthlyCost": "past_total_monthly_cost", "diffTotalHourlyCost": "diff_total_hourly_cost", "diffTotalMonthlyCost": "diff_total_monthly_cost", "timeGenerated": "2019-01-01T12:00:00.000Z", "user_id": "user_id"}, "cra_logs": {"cra_version": "cra_version", "schema_version": "schema_version", "status": "passed", "summary": {"total": "total", "passed": "passed", "failed": "failed", "skipped": "skipped"}, "timestamp": "2019-01-01T12:00:00.000Z"}}, "last_deployed": {"href": "href", "result": "failed", "pre_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "post_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "job": {"id": "id", "summary": {"plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "sucess_message": ["sucess_message"], "update_message": ["update_message"], "destroy_message": ["destroy_message"]}, "apply_messages": {"error_messages": [{}], "sucess_message": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}}, "last_undeployed": {"href": "href", "result": "failed", "pre_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "post_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "job": {"id": "id", "summary": {"plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "sucess_message": ["sucess_message"], "update_message": ["update_message"], "destroy_message": ["destroy_message"]}, "apply_messages": {"error_messages": [{}], "sucess_message": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}}, "outputs": [{"name": "name", "description": "description", "value": "anyValue"}], "project": {"id": "id", "definition": {"name": "name"}, "crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::", "href": "href"}, "references": {"anyKey": "anyValue"}, "schematics": {"workspace_crn": "workspace_crn"}, "state": "approved", "update_available": true, "definition": {"name": "name", "description": "description", "environment": "environment", "authorizations": {"trusted_profile_id": "trusted_profile_id", "method": "api_key", "api_key": "api_key"}, "compliance_profile": {"id": "id", "instance_id": "instance_id", "instance_location": "instance_location", "attachment_id": "attachment_id", "profile_name": "profile_name"}, "locator_id": "locator_id", "inputs": {}, "settings": {}, "type": "terraform_template"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=202,
        )

        # Set up parameter values
        project_id = 'testString'
        id = 'testString'

        # Invoke method
        response = _service.deploy_config(
            project_id,
            id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202

    def test_deploy_config_all_params_with_retries(self):
        # Enable retries and run test_deploy_config_all_params.
        _service.enable_retries()
        self.test_deploy_config_all_params()

        # Disable retries and run test_deploy_config_all_params.
        _service.disable_retries()
        self.test_deploy_config_all_params()

    @responses.activate
    def test_deploy_config_value_error(self):
        """
        test_deploy_config_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/projects/testString/configs/testString/deploy')
        mock_response = '{"id": "id", "version": 7, "is_draft": true, "needs_attention_state": ["anyValue"], "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "last_approved": {"at": "2019-01-01T12:00:00.000Z", "comment": "comment", "is_forced": false, "user_id": "user_id"}, "last_saved_at": "2019-01-01T12:00:00.000Z", "last_validated": {"href": "href", "result": "failed", "pre_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "post_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "job": {"id": "id", "summary": {"plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "sucess_message": ["sucess_message"], "update_message": ["update_message"], "destroy_message": ["destroy_message"]}, "apply_messages": {"error_messages": [{}], "sucess_message": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}, "cost_estimate": {"version": "version", "currency": "USD", "totalHourlyCost": "total_hourly_cost", "totalMonthlyCost": "total_monthly_cost", "pastTotalHourlyCost": "past_total_hourly_cost", "pastTotalMonthlyCost": "past_total_monthly_cost", "diffTotalHourlyCost": "diff_total_hourly_cost", "diffTotalMonthlyCost": "diff_total_monthly_cost", "timeGenerated": "2019-01-01T12:00:00.000Z", "user_id": "user_id"}, "cra_logs": {"cra_version": "cra_version", "schema_version": "schema_version", "status": "passed", "summary": {"total": "total", "passed": "passed", "failed": "failed", "skipped": "skipped"}, "timestamp": "2019-01-01T12:00:00.000Z"}}, "last_deployed": {"href": "href", "result": "failed", "pre_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "post_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "job": {"id": "id", "summary": {"plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "sucess_message": ["sucess_message"], "update_message": ["update_message"], "destroy_message": ["destroy_message"]}, "apply_messages": {"error_messages": [{}], "sucess_message": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}}, "last_undeployed": {"href": "href", "result": "failed", "pre_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "post_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "job": {"id": "id", "summary": {"plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "sucess_message": ["sucess_message"], "update_message": ["update_message"], "destroy_message": ["destroy_message"]}, "apply_messages": {"error_messages": [{}], "sucess_message": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}}, "outputs": [{"name": "name", "description": "description", "value": "anyValue"}], "project": {"id": "id", "definition": {"name": "name"}, "crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::", "href": "href"}, "references": {"anyKey": "anyValue"}, "schematics": {"workspace_crn": "workspace_crn"}, "state": "approved", "update_available": true, "definition": {"name": "name", "description": "description", "environment": "environment", "authorizations": {"trusted_profile_id": "trusted_profile_id", "method": "api_key", "api_key": "api_key"}, "compliance_profile": {"id": "id", "instance_id": "instance_id", "instance_location": "instance_location", "attachment_id": "attachment_id", "profile_name": "profile_name"}, "locator_id": "locator_id", "inputs": {}, "settings": {}, "type": "terraform_template"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=202,
        )

        # Set up parameter values
        project_id = 'testString'
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.deploy_config(**req_copy)

    def test_deploy_config_value_error_with_retries(self):
        # Enable retries and run test_deploy_config_value_error.
        _service.enable_retries()
        self.test_deploy_config_value_error()

        # Disable retries and run test_deploy_config_value_error.
        _service.disable_retries()
        self.test_deploy_config_value_error()


class TestUndeployConfig:
    """
    Test Class for undeploy_config
    """

    @responses.activate
    def test_undeploy_config_all_params(self):
        """
        undeploy_config()
        """
        # Set up mock
        url = preprocess_url('/v1/projects/testString/configs/testString/undeploy')
        responses.add(
            responses.POST,
            url,
            status=204,
        )

        # Set up parameter values
        project_id = 'testString'
        id = 'testString'

        # Invoke method
        response = _service.undeploy_config(
            project_id,
            id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_undeploy_config_all_params_with_retries(self):
        # Enable retries and run test_undeploy_config_all_params.
        _service.enable_retries()
        self.test_undeploy_config_all_params()

        # Disable retries and run test_undeploy_config_all_params.
        _service.disable_retries()
        self.test_undeploy_config_all_params()

    @responses.activate
    def test_undeploy_config_value_error(self):
        """
        test_undeploy_config_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/projects/testString/configs/testString/undeploy')
        responses.add(
            responses.POST,
            url,
            status=204,
        )

        # Set up parameter values
        project_id = 'testString'
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.undeploy_config(**req_copy)

    def test_undeploy_config_value_error_with_retries(self):
        # Enable retries and run test_undeploy_config_value_error.
        _service.enable_retries()
        self.test_undeploy_config_value_error()

        # Disable retries and run test_undeploy_config_value_error.
        _service.disable_retries()
        self.test_undeploy_config_value_error()


class TestSyncConfig:
    """
    Test Class for sync_config
    """

    @responses.activate
    def test_sync_config_all_params(self):
        """
        sync_config()
        """
        # Set up mock
        url = preprocess_url('/v1/projects/testString/configs/testString/sync')
        responses.add(
            responses.POST,
            url,
            status=204,
        )

        # Construct a dict representation of a SchematicsWorkspace model
        schematics_workspace_model = {}
        schematics_workspace_model['workspace_crn'] = 'crn:v1:staging:public:schematics:us-south:a/38acaf4469814090a4e675dc0c317a0d:95ad49de-ab96-4e7d-a08c-45c38aa448e6:workspace:us-south.workspace.service.e0106139'

        # Set up parameter values
        project_id = 'testString'
        id = 'testString'
        schematics = schematics_workspace_model

        # Invoke method
        response = _service.sync_config(
            project_id,
            id,
            schematics=schematics,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['schematics'] == schematics_workspace_model

    def test_sync_config_all_params_with_retries(self):
        # Enable retries and run test_sync_config_all_params.
        _service.enable_retries()
        self.test_sync_config_all_params()

        # Disable retries and run test_sync_config_all_params.
        _service.disable_retries()
        self.test_sync_config_all_params()

    @responses.activate
    def test_sync_config_required_params(self):
        """
        test_sync_config_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/projects/testString/configs/testString/sync')
        responses.add(
            responses.POST,
            url,
            status=204,
        )

        # Set up parameter values
        project_id = 'testString'
        id = 'testString'

        # Invoke method
        response = _service.sync_config(
            project_id,
            id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_sync_config_required_params_with_retries(self):
        # Enable retries and run test_sync_config_required_params.
        _service.enable_retries()
        self.test_sync_config_required_params()

        # Disable retries and run test_sync_config_required_params.
        _service.disable_retries()
        self.test_sync_config_required_params()

    @responses.activate
    def test_sync_config_value_error(self):
        """
        test_sync_config_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/projects/testString/configs/testString/sync')
        responses.add(
            responses.POST,
            url,
            status=204,
        )

        # Set up parameter values
        project_id = 'testString'
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.sync_config(**req_copy)

    def test_sync_config_value_error_with_retries(self):
        # Enable retries and run test_sync_config_value_error.
        _service.enable_retries()
        self.test_sync_config_value_error()

        # Disable retries and run test_sync_config_value_error.
        _service.disable_retries()
        self.test_sync_config_value_error()


class TestListConfigResources:
    """
    Test Class for list_config_resources
    """

    @responses.activate
    def test_list_config_resources_all_params(self):
        """
        list_config_resources()
        """
        # Set up mock
        url = preprocess_url('/v1/projects/testString/configs/testString/resources')
        mock_response = '{"resources": [{"resource_crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::", "resource_name": "resource_name", "resource_type": "resource_type", "resource_tainted": true, "resource_group_name": "resource_group_name"}], "resources_count": 15}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = 'testString'
        id = 'testString'

        # Invoke method
        response = _service.list_config_resources(
            project_id,
            id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_config_resources_all_params_with_retries(self):
        # Enable retries and run test_list_config_resources_all_params.
        _service.enable_retries()
        self.test_list_config_resources_all_params()

        # Disable retries and run test_list_config_resources_all_params.
        _service.disable_retries()
        self.test_list_config_resources_all_params()

    @responses.activate
    def test_list_config_resources_value_error(self):
        """
        test_list_config_resources_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/projects/testString/configs/testString/resources')
        mock_response = '{"resources": [{"resource_crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::", "resource_name": "resource_name", "resource_type": "resource_type", "resource_tainted": true, "resource_group_name": "resource_group_name"}], "resources_count": 15}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = 'testString'
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_config_resources(**req_copy)

    def test_list_config_resources_value_error_with_retries(self):
        # Enable retries and run test_list_config_resources_value_error.
        _service.enable_retries()
        self.test_list_config_resources_value_error()

        # Disable retries and run test_list_config_resources_value_error.
        _service.disable_retries()
        self.test_list_config_resources_value_error()


class TestListConfigVersions:
    """
    Test Class for list_config_versions
    """

    @responses.activate
    def test_list_config_versions_all_params(self):
        """
        list_config_versions()
        """
        # Set up mock
        url = preprocess_url('/v1/projects/testString/configs/testString/versions')
        mock_response = '{"versions": [{"state": "approved", "version": 7, "href": "href"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = 'testString'
        id = 'testString'

        # Invoke method
        response = _service.list_config_versions(
            project_id,
            id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_config_versions_all_params_with_retries(self):
        # Enable retries and run test_list_config_versions_all_params.
        _service.enable_retries()
        self.test_list_config_versions_all_params()

        # Disable retries and run test_list_config_versions_all_params.
        _service.disable_retries()
        self.test_list_config_versions_all_params()

    @responses.activate
    def test_list_config_versions_value_error(self):
        """
        test_list_config_versions_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/projects/testString/configs/testString/versions')
        mock_response = '{"versions": [{"state": "approved", "version": 7, "href": "href"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = 'testString'
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_config_versions(**req_copy)

    def test_list_config_versions_value_error_with_retries(self):
        # Enable retries and run test_list_config_versions_value_error.
        _service.enable_retries()
        self.test_list_config_versions_value_error()

        # Disable retries and run test_list_config_versions_value_error.
        _service.disable_retries()
        self.test_list_config_versions_value_error()


class TestGetConfigVersion:
    """
    Test Class for get_config_version
    """

    @responses.activate
    def test_get_config_version_all_params(self):
        """
        get_config_version()
        """
        # Set up mock
        url = preprocess_url('/v1/projects/testString/configs/testString/versions/38')
        mock_response = '{"id": "id", "version": 7, "is_draft": true, "needs_attention_state": ["anyValue"], "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "last_approved": {"at": "2019-01-01T12:00:00.000Z", "comment": "comment", "is_forced": false, "user_id": "user_id"}, "last_saved_at": "2019-01-01T12:00:00.000Z", "last_validated": {"href": "href", "result": "failed", "pre_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "post_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "job": {"id": "id", "summary": {"plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "sucess_message": ["sucess_message"], "update_message": ["update_message"], "destroy_message": ["destroy_message"]}, "apply_messages": {"error_messages": [{}], "sucess_message": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}, "cost_estimate": {"version": "version", "currency": "USD", "totalHourlyCost": "total_hourly_cost", "totalMonthlyCost": "total_monthly_cost", "pastTotalHourlyCost": "past_total_hourly_cost", "pastTotalMonthlyCost": "past_total_monthly_cost", "diffTotalHourlyCost": "diff_total_hourly_cost", "diffTotalMonthlyCost": "diff_total_monthly_cost", "timeGenerated": "2019-01-01T12:00:00.000Z", "user_id": "user_id"}, "cra_logs": {"cra_version": "cra_version", "schema_version": "schema_version", "status": "passed", "summary": {"total": "total", "passed": "passed", "failed": "failed", "skipped": "skipped"}, "timestamp": "2019-01-01T12:00:00.000Z"}}, "last_deployed": {"href": "href", "result": "failed", "pre_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "post_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "job": {"id": "id", "summary": {"plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "sucess_message": ["sucess_message"], "update_message": ["update_message"], "destroy_message": ["destroy_message"]}, "apply_messages": {"error_messages": [{}], "sucess_message": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}}, "last_undeployed": {"href": "href", "result": "failed", "pre_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "post_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "job": {"id": "id", "summary": {"plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "sucess_message": ["sucess_message"], "update_message": ["update_message"], "destroy_message": ["destroy_message"]}, "apply_messages": {"error_messages": [{}], "sucess_message": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}}, "outputs": [{"name": "name", "description": "description", "value": "anyValue"}], "project": {"id": "id", "definition": {"name": "name"}, "crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::", "href": "href"}, "references": {"anyKey": "anyValue"}, "schematics": {"workspace_crn": "workspace_crn"}, "state": "approved", "update_available": true, "definition": {"name": "name", "description": "description", "environment": "environment", "authorizations": {"trusted_profile_id": "trusted_profile_id", "method": "api_key", "api_key": "api_key"}, "compliance_profile": {"id": "id", "instance_id": "instance_id", "instance_location": "instance_location", "attachment_id": "attachment_id", "profile_name": "profile_name"}, "locator_id": "locator_id", "inputs": {}, "settings": {}, "type": "terraform_template"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = 'testString'
        id = 'testString'
        version = 38

        # Invoke method
        response = _service.get_config_version(
            project_id,
            id,
            version,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_config_version_all_params_with_retries(self):
        # Enable retries and run test_get_config_version_all_params.
        _service.enable_retries()
        self.test_get_config_version_all_params()

        # Disable retries and run test_get_config_version_all_params.
        _service.disable_retries()
        self.test_get_config_version_all_params()

    @responses.activate
    def test_get_config_version_value_error(self):
        """
        test_get_config_version_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/projects/testString/configs/testString/versions/38')
        mock_response = '{"id": "id", "version": 7, "is_draft": true, "needs_attention_state": ["anyValue"], "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "last_approved": {"at": "2019-01-01T12:00:00.000Z", "comment": "comment", "is_forced": false, "user_id": "user_id"}, "last_saved_at": "2019-01-01T12:00:00.000Z", "last_validated": {"href": "href", "result": "failed", "pre_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "post_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "job": {"id": "id", "summary": {"plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "sucess_message": ["sucess_message"], "update_message": ["update_message"], "destroy_message": ["destroy_message"]}, "apply_messages": {"error_messages": [{}], "sucess_message": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}, "cost_estimate": {"version": "version", "currency": "USD", "totalHourlyCost": "total_hourly_cost", "totalMonthlyCost": "total_monthly_cost", "pastTotalHourlyCost": "past_total_hourly_cost", "pastTotalMonthlyCost": "past_total_monthly_cost", "diffTotalHourlyCost": "diff_total_hourly_cost", "diffTotalMonthlyCost": "diff_total_monthly_cost", "timeGenerated": "2019-01-01T12:00:00.000Z", "user_id": "user_id"}, "cra_logs": {"cra_version": "cra_version", "schema_version": "schema_version", "status": "passed", "summary": {"total": "total", "passed": "passed", "failed": "failed", "skipped": "skipped"}, "timestamp": "2019-01-01T12:00:00.000Z"}}, "last_deployed": {"href": "href", "result": "failed", "pre_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "post_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "job": {"id": "id", "summary": {"plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "sucess_message": ["sucess_message"], "update_message": ["update_message"], "destroy_message": ["destroy_message"]}, "apply_messages": {"error_messages": [{}], "sucess_message": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}}, "last_undeployed": {"href": "href", "result": "failed", "pre_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "post_job": {"id": "id", "summary": {"anyKey": "anyValue"}}, "job": {"id": "id", "summary": {"plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "sucess_message": ["sucess_message"], "update_message": ["update_message"], "destroy_message": ["destroy_message"]}, "apply_messages": {"error_messages": [{}], "sucess_message": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}}, "outputs": [{"name": "name", "description": "description", "value": "anyValue"}], "project": {"id": "id", "definition": {"name": "name"}, "crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::", "href": "href"}, "references": {"anyKey": "anyValue"}, "schematics": {"workspace_crn": "workspace_crn"}, "state": "approved", "update_available": true, "definition": {"name": "name", "description": "description", "environment": "environment", "authorizations": {"trusted_profile_id": "trusted_profile_id", "method": "api_key", "api_key": "api_key"}, "compliance_profile": {"id": "id", "instance_id": "instance_id", "instance_location": "instance_location", "attachment_id": "attachment_id", "profile_name": "profile_name"}, "locator_id": "locator_id", "inputs": {}, "settings": {}, "type": "terraform_template"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = 'testString'
        id = 'testString'
        version = 38

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "id": id,
            "version": version,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_config_version(**req_copy)

    def test_get_config_version_value_error_with_retries(self):
        # Enable retries and run test_get_config_version_value_error.
        _service.enable_retries()
        self.test_get_config_version_value_error()

        # Disable retries and run test_get_config_version_value_error.
        _service.disable_retries()
        self.test_get_config_version_value_error()


class TestDeleteConfigVersion:
    """
    Test Class for delete_config_version
    """

    @responses.activate
    def test_delete_config_version_all_params(self):
        """
        delete_config_version()
        """
        # Set up mock
        url = preprocess_url('/v1/projects/testString/configs/testString/versions/38')
        mock_response = '{"id": "id"}'
        responses.add(
            responses.DELETE,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = 'testString'
        id = 'testString'
        version = 38

        # Invoke method
        response = _service.delete_config_version(
            project_id,
            id,
            version,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_delete_config_version_all_params_with_retries(self):
        # Enable retries and run test_delete_config_version_all_params.
        _service.enable_retries()
        self.test_delete_config_version_all_params()

        # Disable retries and run test_delete_config_version_all_params.
        _service.disable_retries()
        self.test_delete_config_version_all_params()

    @responses.activate
    def test_delete_config_version_value_error(self):
        """
        test_delete_config_version_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/projects/testString/configs/testString/versions/38')
        mock_response = '{"id": "id"}'
        responses.add(
            responses.DELETE,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = 'testString'
        id = 'testString'
        version = 38

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "id": id,
            "version": version,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_config_version(**req_copy)

    def test_delete_config_version_value_error_with_retries(self):
        # Enable retries and run test_delete_config_version_value_error.
        _service.enable_retries()
        self.test_delete_config_version_value_error()

        # Disable retries and run test_delete_config_version_value_error.
        _service.disable_retries()
        self.test_delete_config_version_value_error()


# endregion
##############################################################################
# End of Service: Configurations
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region


class TestModel_ActionJobApplyMessagesSummary:
    """
    Test Class for ActionJobApplyMessagesSummary
    """

    def test_action_job_apply_messages_summary_serialization(self):
        """
        Test serialization/deserialization for ActionJobApplyMessagesSummary
        """

        # Construct dict forms of any model objects needed in order to build this model.

        terraform_log_analyzer_error_message_model = {}  # TerraformLogAnalyzerErrorMessage
        terraform_log_analyzer_error_message_model['foo'] = 'testString'

        terraform_log_analyzer_success_message_model = {}  # TerraformLogAnalyzerSuccessMessage
        terraform_log_analyzer_success_message_model['resource_type'] = 'testString'
        terraform_log_analyzer_success_message_model['time-taken'] = 'testString'
        terraform_log_analyzer_success_message_model['id'] = 'testString'

        # Construct a json representation of a ActionJobApplyMessagesSummary model
        action_job_apply_messages_summary_model_json = {}
        action_job_apply_messages_summary_model_json['error_messages'] = [terraform_log_analyzer_error_message_model]
        action_job_apply_messages_summary_model_json['sucess_message'] = [terraform_log_analyzer_success_message_model]

        # Construct a model instance of ActionJobApplyMessagesSummary by calling from_dict on the json representation
        action_job_apply_messages_summary_model = ActionJobApplyMessagesSummary.from_dict(action_job_apply_messages_summary_model_json)
        assert action_job_apply_messages_summary_model != False

        # Construct a model instance of ActionJobApplyMessagesSummary by calling from_dict on the json representation
        action_job_apply_messages_summary_model_dict = ActionJobApplyMessagesSummary.from_dict(action_job_apply_messages_summary_model_json).__dict__
        action_job_apply_messages_summary_model2 = ActionJobApplyMessagesSummary(**action_job_apply_messages_summary_model_dict)

        # Verify the model instances are equivalent
        assert action_job_apply_messages_summary_model == action_job_apply_messages_summary_model2

        # Convert model instance back to dict and verify no loss of data
        action_job_apply_messages_summary_model_json2 = action_job_apply_messages_summary_model.to_dict()
        assert action_job_apply_messages_summary_model_json2 == action_job_apply_messages_summary_model_json


class TestModel_ActionJobApplySummary:
    """
    Test Class for ActionJobApplySummary
    """

    def test_action_job_apply_summary_serialization(self):
        """
        Test serialization/deserialization for ActionJobApplySummary
        """

        # Construct a json representation of a ActionJobApplySummary model
        action_job_apply_summary_model_json = {}
        action_job_apply_summary_model_json['success'] = 38
        action_job_apply_summary_model_json['failed'] = 38
        action_job_apply_summary_model_json['success_resources'] = ['testString']
        action_job_apply_summary_model_json['failed_resources'] = ['testString']

        # Construct a model instance of ActionJobApplySummary by calling from_dict on the json representation
        action_job_apply_summary_model = ActionJobApplySummary.from_dict(action_job_apply_summary_model_json)
        assert action_job_apply_summary_model != False

        # Construct a model instance of ActionJobApplySummary by calling from_dict on the json representation
        action_job_apply_summary_model_dict = ActionJobApplySummary.from_dict(action_job_apply_summary_model_json).__dict__
        action_job_apply_summary_model2 = ActionJobApplySummary(**action_job_apply_summary_model_dict)

        # Verify the model instances are equivalent
        assert action_job_apply_summary_model == action_job_apply_summary_model2

        # Convert model instance back to dict and verify no loss of data
        action_job_apply_summary_model_json2 = action_job_apply_summary_model.to_dict()
        assert action_job_apply_summary_model_json2 == action_job_apply_summary_model_json


class TestModel_ActionJobDestroyMessagesSummary:
    """
    Test Class for ActionJobDestroyMessagesSummary
    """

    def test_action_job_destroy_messages_summary_serialization(self):
        """
        Test serialization/deserialization for ActionJobDestroyMessagesSummary
        """

        # Construct dict forms of any model objects needed in order to build this model.

        terraform_log_analyzer_error_message_model = {}  # TerraformLogAnalyzerErrorMessage
        terraform_log_analyzer_error_message_model['foo'] = 'testString'

        # Construct a json representation of a ActionJobDestroyMessagesSummary model
        action_job_destroy_messages_summary_model_json = {}
        action_job_destroy_messages_summary_model_json['error_messages'] = [terraform_log_analyzer_error_message_model]

        # Construct a model instance of ActionJobDestroyMessagesSummary by calling from_dict on the json representation
        action_job_destroy_messages_summary_model = ActionJobDestroyMessagesSummary.from_dict(action_job_destroy_messages_summary_model_json)
        assert action_job_destroy_messages_summary_model != False

        # Construct a model instance of ActionJobDestroyMessagesSummary by calling from_dict on the json representation
        action_job_destroy_messages_summary_model_dict = ActionJobDestroyMessagesSummary.from_dict(action_job_destroy_messages_summary_model_json).__dict__
        action_job_destroy_messages_summary_model2 = ActionJobDestroyMessagesSummary(**action_job_destroy_messages_summary_model_dict)

        # Verify the model instances are equivalent
        assert action_job_destroy_messages_summary_model == action_job_destroy_messages_summary_model2

        # Convert model instance back to dict and verify no loss of data
        action_job_destroy_messages_summary_model_json2 = action_job_destroy_messages_summary_model.to_dict()
        assert action_job_destroy_messages_summary_model_json2 == action_job_destroy_messages_summary_model_json


class TestModel_ActionJobDestroySummary:
    """
    Test Class for ActionJobDestroySummary
    """

    def test_action_job_destroy_summary_serialization(self):
        """
        Test serialization/deserialization for ActionJobDestroySummary
        """

        # Construct dict forms of any model objects needed in order to build this model.

        action_job_destroy_summary_resources_model = {}  # ActionJobDestroySummaryResources
        action_job_destroy_summary_resources_model['success'] = ['testString']
        action_job_destroy_summary_resources_model['failed'] = ['testString']
        action_job_destroy_summary_resources_model['tainted'] = ['testString']

        # Construct a json representation of a ActionJobDestroySummary model
        action_job_destroy_summary_model_json = {}
        action_job_destroy_summary_model_json['success'] = 38
        action_job_destroy_summary_model_json['failed'] = 38
        action_job_destroy_summary_model_json['tainted'] = 38
        action_job_destroy_summary_model_json['resources'] = action_job_destroy_summary_resources_model

        # Construct a model instance of ActionJobDestroySummary by calling from_dict on the json representation
        action_job_destroy_summary_model = ActionJobDestroySummary.from_dict(action_job_destroy_summary_model_json)
        assert action_job_destroy_summary_model != False

        # Construct a model instance of ActionJobDestroySummary by calling from_dict on the json representation
        action_job_destroy_summary_model_dict = ActionJobDestroySummary.from_dict(action_job_destroy_summary_model_json).__dict__
        action_job_destroy_summary_model2 = ActionJobDestroySummary(**action_job_destroy_summary_model_dict)

        # Verify the model instances are equivalent
        assert action_job_destroy_summary_model == action_job_destroy_summary_model2

        # Convert model instance back to dict and verify no loss of data
        action_job_destroy_summary_model_json2 = action_job_destroy_summary_model.to_dict()
        assert action_job_destroy_summary_model_json2 == action_job_destroy_summary_model_json


class TestModel_ActionJobDestroySummaryResources:
    """
    Test Class for ActionJobDestroySummaryResources
    """

    def test_action_job_destroy_summary_resources_serialization(self):
        """
        Test serialization/deserialization for ActionJobDestroySummaryResources
        """

        # Construct a json representation of a ActionJobDestroySummaryResources model
        action_job_destroy_summary_resources_model_json = {}
        action_job_destroy_summary_resources_model_json['success'] = ['testString']
        action_job_destroy_summary_resources_model_json['failed'] = ['testString']
        action_job_destroy_summary_resources_model_json['tainted'] = ['testString']

        # Construct a model instance of ActionJobDestroySummaryResources by calling from_dict on the json representation
        action_job_destroy_summary_resources_model = ActionJobDestroySummaryResources.from_dict(action_job_destroy_summary_resources_model_json)
        assert action_job_destroy_summary_resources_model != False

        # Construct a model instance of ActionJobDestroySummaryResources by calling from_dict on the json representation
        action_job_destroy_summary_resources_model_dict = ActionJobDestroySummaryResources.from_dict(action_job_destroy_summary_resources_model_json).__dict__
        action_job_destroy_summary_resources_model2 = ActionJobDestroySummaryResources(**action_job_destroy_summary_resources_model_dict)

        # Verify the model instances are equivalent
        assert action_job_destroy_summary_resources_model == action_job_destroy_summary_resources_model2

        # Convert model instance back to dict and verify no loss of data
        action_job_destroy_summary_resources_model_json2 = action_job_destroy_summary_resources_model.to_dict()
        assert action_job_destroy_summary_resources_model_json2 == action_job_destroy_summary_resources_model_json


class TestModel_ActionJobMessageSummary:
    """
    Test Class for ActionJobMessageSummary
    """

    def test_action_job_message_summary_serialization(self):
        """
        Test serialization/deserialization for ActionJobMessageSummary
        """

        # Construct a json representation of a ActionJobMessageSummary model
        action_job_message_summary_model_json = {}
        action_job_message_summary_model_json['info'] = 38
        action_job_message_summary_model_json['debug'] = 38
        action_job_message_summary_model_json['error'] = 38

        # Construct a model instance of ActionJobMessageSummary by calling from_dict on the json representation
        action_job_message_summary_model = ActionJobMessageSummary.from_dict(action_job_message_summary_model_json)
        assert action_job_message_summary_model != False

        # Construct a model instance of ActionJobMessageSummary by calling from_dict on the json representation
        action_job_message_summary_model_dict = ActionJobMessageSummary.from_dict(action_job_message_summary_model_json).__dict__
        action_job_message_summary_model2 = ActionJobMessageSummary(**action_job_message_summary_model_dict)

        # Verify the model instances are equivalent
        assert action_job_message_summary_model == action_job_message_summary_model2

        # Convert model instance back to dict and verify no loss of data
        action_job_message_summary_model_json2 = action_job_message_summary_model.to_dict()
        assert action_job_message_summary_model_json2 == action_job_message_summary_model_json


class TestModel_ActionJobPlanMessagesSummary:
    """
    Test Class for ActionJobPlanMessagesSummary
    """

    def test_action_job_plan_messages_summary_serialization(self):
        """
        Test serialization/deserialization for ActionJobPlanMessagesSummary
        """

        # Construct dict forms of any model objects needed in order to build this model.

        terraform_log_analyzer_error_message_model = {}  # TerraformLogAnalyzerErrorMessage
        terraform_log_analyzer_error_message_model['foo'] = 'testString'

        # Construct a json representation of a ActionJobPlanMessagesSummary model
        action_job_plan_messages_summary_model_json = {}
        action_job_plan_messages_summary_model_json['error_messages'] = [terraform_log_analyzer_error_message_model]
        action_job_plan_messages_summary_model_json['sucess_message'] = ['testString']
        action_job_plan_messages_summary_model_json['update_message'] = ['testString']
        action_job_plan_messages_summary_model_json['destroy_message'] = ['testString']

        # Construct a model instance of ActionJobPlanMessagesSummary by calling from_dict on the json representation
        action_job_plan_messages_summary_model = ActionJobPlanMessagesSummary.from_dict(action_job_plan_messages_summary_model_json)
        assert action_job_plan_messages_summary_model != False

        # Construct a model instance of ActionJobPlanMessagesSummary by calling from_dict on the json representation
        action_job_plan_messages_summary_model_dict = ActionJobPlanMessagesSummary.from_dict(action_job_plan_messages_summary_model_json).__dict__
        action_job_plan_messages_summary_model2 = ActionJobPlanMessagesSummary(**action_job_plan_messages_summary_model_dict)

        # Verify the model instances are equivalent
        assert action_job_plan_messages_summary_model == action_job_plan_messages_summary_model2

        # Convert model instance back to dict and verify no loss of data
        action_job_plan_messages_summary_model_json2 = action_job_plan_messages_summary_model.to_dict()
        assert action_job_plan_messages_summary_model_json2 == action_job_plan_messages_summary_model_json


class TestModel_ActionJobPlanSummary:
    """
    Test Class for ActionJobPlanSummary
    """

    def test_action_job_plan_summary_serialization(self):
        """
        Test serialization/deserialization for ActionJobPlanSummary
        """

        # Construct a json representation of a ActionJobPlanSummary model
        action_job_plan_summary_model_json = {}
        action_job_plan_summary_model_json['add'] = 38
        action_job_plan_summary_model_json['failed'] = 38
        action_job_plan_summary_model_json['update'] = 38
        action_job_plan_summary_model_json['destroy'] = 38
        action_job_plan_summary_model_json['add_resources'] = ['testString']
        action_job_plan_summary_model_json['failed_resources'] = ['testString']
        action_job_plan_summary_model_json['updated_resources'] = ['testString']
        action_job_plan_summary_model_json['destroy_resources'] = ['testString']

        # Construct a model instance of ActionJobPlanSummary by calling from_dict on the json representation
        action_job_plan_summary_model = ActionJobPlanSummary.from_dict(action_job_plan_summary_model_json)
        assert action_job_plan_summary_model != False

        # Construct a model instance of ActionJobPlanSummary by calling from_dict on the json representation
        action_job_plan_summary_model_dict = ActionJobPlanSummary.from_dict(action_job_plan_summary_model_json).__dict__
        action_job_plan_summary_model2 = ActionJobPlanSummary(**action_job_plan_summary_model_dict)

        # Verify the model instances are equivalent
        assert action_job_plan_summary_model == action_job_plan_summary_model2

        # Convert model instance back to dict and verify no loss of data
        action_job_plan_summary_model_json2 = action_job_plan_summary_model.to_dict()
        assert action_job_plan_summary_model_json2 == action_job_plan_summary_model_json


class TestModel_ActionJobSummary:
    """
    Test Class for ActionJobSummary
    """

    def test_action_job_summary_serialization(self):
        """
        Test serialization/deserialization for ActionJobSummary
        """

        # Construct dict forms of any model objects needed in order to build this model.

        action_job_plan_summary_model = {}  # ActionJobPlanSummary
        action_job_plan_summary_model['add'] = 38
        action_job_plan_summary_model['failed'] = 38
        action_job_plan_summary_model['update'] = 38
        action_job_plan_summary_model['destroy'] = 38
        action_job_plan_summary_model['add_resources'] = ['testString']
        action_job_plan_summary_model['failed_resources'] = ['testString']
        action_job_plan_summary_model['updated_resources'] = ['testString']
        action_job_plan_summary_model['destroy_resources'] = ['testString']

        action_job_apply_summary_model = {}  # ActionJobApplySummary
        action_job_apply_summary_model['success'] = 38
        action_job_apply_summary_model['failed'] = 38
        action_job_apply_summary_model['success_resources'] = ['testString']
        action_job_apply_summary_model['failed_resources'] = ['testString']

        action_job_destroy_summary_resources_model = {}  # ActionJobDestroySummaryResources
        action_job_destroy_summary_resources_model['success'] = ['testString']
        action_job_destroy_summary_resources_model['failed'] = ['testString']
        action_job_destroy_summary_resources_model['tainted'] = ['testString']

        action_job_destroy_summary_model = {}  # ActionJobDestroySummary
        action_job_destroy_summary_model['success'] = 38
        action_job_destroy_summary_model['failed'] = 38
        action_job_destroy_summary_model['tainted'] = 38
        action_job_destroy_summary_model['resources'] = action_job_destroy_summary_resources_model

        action_job_message_summary_model = {}  # ActionJobMessageSummary
        action_job_message_summary_model['info'] = 38
        action_job_message_summary_model['debug'] = 38
        action_job_message_summary_model['error'] = 38

        terraform_log_analyzer_error_message_model = {}  # TerraformLogAnalyzerErrorMessage
        terraform_log_analyzer_error_message_model['foo'] = 'testString'

        action_job_plan_messages_summary_model = {}  # ActionJobPlanMessagesSummary
        action_job_plan_messages_summary_model['error_messages'] = [terraform_log_analyzer_error_message_model]
        action_job_plan_messages_summary_model['sucess_message'] = ['testString']
        action_job_plan_messages_summary_model['update_message'] = ['testString']
        action_job_plan_messages_summary_model['destroy_message'] = ['testString']

        terraform_log_analyzer_success_message_model = {}  # TerraformLogAnalyzerSuccessMessage
        terraform_log_analyzer_success_message_model['resource_type'] = 'testString'
        terraform_log_analyzer_success_message_model['time-taken'] = 'testString'
        terraform_log_analyzer_success_message_model['id'] = 'testString'

        action_job_apply_messages_summary_model = {}  # ActionJobApplyMessagesSummary
        action_job_apply_messages_summary_model['error_messages'] = [terraform_log_analyzer_error_message_model]
        action_job_apply_messages_summary_model['sucess_message'] = [terraform_log_analyzer_success_message_model]

        action_job_destroy_messages_summary_model = {}  # ActionJobDestroyMessagesSummary
        action_job_destroy_messages_summary_model['error_messages'] = [terraform_log_analyzer_error_message_model]

        # Construct a json representation of a ActionJobSummary model
        action_job_summary_model_json = {}
        action_job_summary_model_json['plan_summary'] = action_job_plan_summary_model
        action_job_summary_model_json['apply_summary'] = action_job_apply_summary_model
        action_job_summary_model_json['destroy_summary'] = action_job_destroy_summary_model
        action_job_summary_model_json['message_summary'] = action_job_message_summary_model
        action_job_summary_model_json['plan_messages'] = action_job_plan_messages_summary_model
        action_job_summary_model_json['apply_messages'] = action_job_apply_messages_summary_model
        action_job_summary_model_json['destroy_messages'] = action_job_destroy_messages_summary_model

        # Construct a model instance of ActionJobSummary by calling from_dict on the json representation
        action_job_summary_model = ActionJobSummary.from_dict(action_job_summary_model_json)
        assert action_job_summary_model != False

        # Construct a model instance of ActionJobSummary by calling from_dict on the json representation
        action_job_summary_model_dict = ActionJobSummary.from_dict(action_job_summary_model_json).__dict__
        action_job_summary_model2 = ActionJobSummary(**action_job_summary_model_dict)

        # Verify the model instances are equivalent
        assert action_job_summary_model == action_job_summary_model2

        # Convert model instance back to dict and verify no loss of data
        action_job_summary_model_json2 = action_job_summary_model.to_dict()
        assert action_job_summary_model_json2 == action_job_summary_model_json


class TestModel_ActionJobWithIdAndSummary:
    """
    Test Class for ActionJobWithIdAndSummary
    """

    def test_action_job_with_id_and_summary_serialization(self):
        """
        Test serialization/deserialization for ActionJobWithIdAndSummary
        """

        # Construct dict forms of any model objects needed in order to build this model.

        action_job_plan_summary_model = {}  # ActionJobPlanSummary
        action_job_plan_summary_model['add'] = 38
        action_job_plan_summary_model['failed'] = 38
        action_job_plan_summary_model['update'] = 38
        action_job_plan_summary_model['destroy'] = 38
        action_job_plan_summary_model['add_resources'] = ['testString']
        action_job_plan_summary_model['failed_resources'] = ['testString']
        action_job_plan_summary_model['updated_resources'] = ['testString']
        action_job_plan_summary_model['destroy_resources'] = ['testString']

        action_job_apply_summary_model = {}  # ActionJobApplySummary
        action_job_apply_summary_model['success'] = 38
        action_job_apply_summary_model['failed'] = 38
        action_job_apply_summary_model['success_resources'] = ['testString']
        action_job_apply_summary_model['failed_resources'] = ['testString']

        action_job_destroy_summary_resources_model = {}  # ActionJobDestroySummaryResources
        action_job_destroy_summary_resources_model['success'] = ['testString']
        action_job_destroy_summary_resources_model['failed'] = ['testString']
        action_job_destroy_summary_resources_model['tainted'] = ['testString']

        action_job_destroy_summary_model = {}  # ActionJobDestroySummary
        action_job_destroy_summary_model['success'] = 38
        action_job_destroy_summary_model['failed'] = 38
        action_job_destroy_summary_model['tainted'] = 38
        action_job_destroy_summary_model['resources'] = action_job_destroy_summary_resources_model

        action_job_message_summary_model = {}  # ActionJobMessageSummary
        action_job_message_summary_model['info'] = 38
        action_job_message_summary_model['debug'] = 38
        action_job_message_summary_model['error'] = 38

        terraform_log_analyzer_error_message_model = {}  # TerraformLogAnalyzerErrorMessage
        terraform_log_analyzer_error_message_model['foo'] = 'testString'

        action_job_plan_messages_summary_model = {}  # ActionJobPlanMessagesSummary
        action_job_plan_messages_summary_model['error_messages'] = [terraform_log_analyzer_error_message_model]
        action_job_plan_messages_summary_model['sucess_message'] = ['testString']
        action_job_plan_messages_summary_model['update_message'] = ['testString']
        action_job_plan_messages_summary_model['destroy_message'] = ['testString']

        terraform_log_analyzer_success_message_model = {}  # TerraformLogAnalyzerSuccessMessage
        terraform_log_analyzer_success_message_model['resource_type'] = 'testString'
        terraform_log_analyzer_success_message_model['time-taken'] = 'testString'
        terraform_log_analyzer_success_message_model['id'] = 'testString'

        action_job_apply_messages_summary_model = {}  # ActionJobApplyMessagesSummary
        action_job_apply_messages_summary_model['error_messages'] = [terraform_log_analyzer_error_message_model]
        action_job_apply_messages_summary_model['sucess_message'] = [terraform_log_analyzer_success_message_model]

        action_job_destroy_messages_summary_model = {}  # ActionJobDestroyMessagesSummary
        action_job_destroy_messages_summary_model['error_messages'] = [terraform_log_analyzer_error_message_model]

        action_job_summary_model = {}  # ActionJobSummary
        action_job_summary_model['plan_summary'] = action_job_plan_summary_model
        action_job_summary_model['apply_summary'] = action_job_apply_summary_model
        action_job_summary_model['destroy_summary'] = action_job_destroy_summary_model
        action_job_summary_model['message_summary'] = action_job_message_summary_model
        action_job_summary_model['plan_messages'] = action_job_plan_messages_summary_model
        action_job_summary_model['apply_messages'] = action_job_apply_messages_summary_model
        action_job_summary_model['destroy_messages'] = action_job_destroy_messages_summary_model

        # Construct a json representation of a ActionJobWithIdAndSummary model
        action_job_with_id_and_summary_model_json = {}
        action_job_with_id_and_summary_model_json['id'] = 'testString'
        action_job_with_id_and_summary_model_json['summary'] = action_job_summary_model

        # Construct a model instance of ActionJobWithIdAndSummary by calling from_dict on the json representation
        action_job_with_id_and_summary_model = ActionJobWithIdAndSummary.from_dict(action_job_with_id_and_summary_model_json)
        assert action_job_with_id_and_summary_model != False

        # Construct a model instance of ActionJobWithIdAndSummary by calling from_dict on the json representation
        action_job_with_id_and_summary_model_dict = ActionJobWithIdAndSummary.from_dict(action_job_with_id_and_summary_model_json).__dict__
        action_job_with_id_and_summary_model2 = ActionJobWithIdAndSummary(**action_job_with_id_and_summary_model_dict)

        # Verify the model instances are equivalent
        assert action_job_with_id_and_summary_model == action_job_with_id_and_summary_model2

        # Convert model instance back to dict and verify no loss of data
        action_job_with_id_and_summary_model_json2 = action_job_with_id_and_summary_model.to_dict()
        assert action_job_with_id_and_summary_model_json2 == action_job_with_id_and_summary_model_json


class TestModel_CodeRiskAnalyzerLogsSummary:
    """
    Test Class for CodeRiskAnalyzerLogsSummary
    """

    def test_code_risk_analyzer_logs_summary_serialization(self):
        """
        Test serialization/deserialization for CodeRiskAnalyzerLogsSummary
        """

        # Construct a json representation of a CodeRiskAnalyzerLogsSummary model
        code_risk_analyzer_logs_summary_model_json = {}
        code_risk_analyzer_logs_summary_model_json['total'] = 'testString'
        code_risk_analyzer_logs_summary_model_json['passed'] = 'testString'
        code_risk_analyzer_logs_summary_model_json['failed'] = 'testString'
        code_risk_analyzer_logs_summary_model_json['skipped'] = 'testString'

        # Construct a model instance of CodeRiskAnalyzerLogsSummary by calling from_dict on the json representation
        code_risk_analyzer_logs_summary_model = CodeRiskAnalyzerLogsSummary.from_dict(code_risk_analyzer_logs_summary_model_json)
        assert code_risk_analyzer_logs_summary_model != False

        # Construct a model instance of CodeRiskAnalyzerLogsSummary by calling from_dict on the json representation
        code_risk_analyzer_logs_summary_model_dict = CodeRiskAnalyzerLogsSummary.from_dict(code_risk_analyzer_logs_summary_model_json).__dict__
        code_risk_analyzer_logs_summary_model2 = CodeRiskAnalyzerLogsSummary(**code_risk_analyzer_logs_summary_model_dict)

        # Verify the model instances are equivalent
        assert code_risk_analyzer_logs_summary_model == code_risk_analyzer_logs_summary_model2

        # Convert model instance back to dict and verify no loss of data
        code_risk_analyzer_logs_summary_model_json2 = code_risk_analyzer_logs_summary_model.to_dict()
        assert code_risk_analyzer_logs_summary_model_json2 == code_risk_analyzer_logs_summary_model_json


class TestModel_CumulativeNeedsAttention:
    """
    Test Class for CumulativeNeedsAttention
    """

    def test_cumulative_needs_attention_serialization(self):
        """
        Test serialization/deserialization for CumulativeNeedsAttention
        """

        # Construct a json representation of a CumulativeNeedsAttention model
        cumulative_needs_attention_model_json = {}
        cumulative_needs_attention_model_json['event'] = 'testString'
        cumulative_needs_attention_model_json['event_id'] = 'testString'
        cumulative_needs_attention_model_json['config_id'] = 'testString'
        cumulative_needs_attention_model_json['config_version'] = 38

        # Construct a model instance of CumulativeNeedsAttention by calling from_dict on the json representation
        cumulative_needs_attention_model = CumulativeNeedsAttention.from_dict(cumulative_needs_attention_model_json)
        assert cumulative_needs_attention_model != False

        # Construct a model instance of CumulativeNeedsAttention by calling from_dict on the json representation
        cumulative_needs_attention_model_dict = CumulativeNeedsAttention.from_dict(cumulative_needs_attention_model_json).__dict__
        cumulative_needs_attention_model2 = CumulativeNeedsAttention(**cumulative_needs_attention_model_dict)

        # Verify the model instances are equivalent
        assert cumulative_needs_attention_model == cumulative_needs_attention_model2

        # Convert model instance back to dict and verify no loss of data
        cumulative_needs_attention_model_json2 = cumulative_needs_attention_model.to_dict()
        assert cumulative_needs_attention_model_json2 == cumulative_needs_attention_model_json


class TestModel_Environment:
    """
    Test Class for Environment
    """

    def test_environment_serialization(self):
        """
        Test serialization/deserialization for Environment
        """

        # Construct dict forms of any model objects needed in order to build this model.

        project_definition_reference_model = {}  # ProjectDefinitionReference
        project_definition_reference_model['name'] = 'testString'

        project_reference_model = {}  # ProjectReference
        project_reference_model['id'] = 'testString'
        project_reference_model['definition'] = project_definition_reference_model
        project_reference_model['crn'] = 'crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::'
        project_reference_model['href'] = 'testString'

        project_config_auth_model = {}  # ProjectConfigAuth
        project_config_auth_model['trusted_profile_id'] = 'testString'
        project_config_auth_model['method'] = 'api_key'
        project_config_auth_model['api_key'] = 'testString'

        input_variable_model = {}  # InputVariable
        input_variable_model['foo'] = 'testString'

        project_compliance_profile_model = {}  # ProjectComplianceProfile
        project_compliance_profile_model['id'] = 'testString'
        project_compliance_profile_model['instance_id'] = 'testString'
        project_compliance_profile_model['instance_location'] = 'testString'
        project_compliance_profile_model['attachment_id'] = 'testString'
        project_compliance_profile_model['profile_name'] = 'testString'

        environment_definition_required_properties_model = {}  # EnvironmentDefinitionRequiredProperties
        environment_definition_required_properties_model['name'] = 'testString'
        environment_definition_required_properties_model['description'] = 'testString'
        environment_definition_required_properties_model['authorizations'] = project_config_auth_model
        environment_definition_required_properties_model['inputs'] = input_variable_model
        environment_definition_required_properties_model['compliance_profile'] = project_compliance_profile_model

        # Construct a json representation of a Environment model
        environment_model_json = {}
        environment_model_json['id'] = 'testString'
        environment_model_json['project'] = project_reference_model
        environment_model_json['created_at'] = '2019-01-01T12:00:00Z'
        environment_model_json['target_account'] = 'testString'
        environment_model_json['modified_at'] = '2019-01-01T12:00:00Z'
        environment_model_json['definition'] = environment_definition_required_properties_model

        # Construct a model instance of Environment by calling from_dict on the json representation
        environment_model = Environment.from_dict(environment_model_json)
        assert environment_model != False

        # Construct a model instance of Environment by calling from_dict on the json representation
        environment_model_dict = Environment.from_dict(environment_model_json).__dict__
        environment_model2 = Environment(**environment_model_dict)

        # Verify the model instances are equivalent
        assert environment_model == environment_model2

        # Convert model instance back to dict and verify no loss of data
        environment_model_json2 = environment_model.to_dict()
        assert environment_model_json2 == environment_model_json


class TestModel_EnvironmentCollection:
    """
    Test Class for EnvironmentCollection
    """

    def test_environment_collection_serialization(self):
        """
        Test serialization/deserialization for EnvironmentCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        project_definition_reference_model = {}  # ProjectDefinitionReference
        project_definition_reference_model['name'] = 'testString'

        project_reference_model = {}  # ProjectReference
        project_reference_model['id'] = 'testString'
        project_reference_model['definition'] = project_definition_reference_model
        project_reference_model['crn'] = 'crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::'
        project_reference_model['href'] = 'testString'

        project_config_auth_model = {}  # ProjectConfigAuth
        project_config_auth_model['trusted_profile_id'] = 'testString'
        project_config_auth_model['method'] = 'api_key'
        project_config_auth_model['api_key'] = 'testString'

        input_variable_model = {}  # InputVariable
        input_variable_model['foo'] = 'testString'

        project_compliance_profile_model = {}  # ProjectComplianceProfile
        project_compliance_profile_model['id'] = 'testString'
        project_compliance_profile_model['instance_id'] = 'testString'
        project_compliance_profile_model['instance_location'] = 'testString'
        project_compliance_profile_model['attachment_id'] = 'testString'
        project_compliance_profile_model['profile_name'] = 'testString'

        environment_definition_required_properties_model = {}  # EnvironmentDefinitionRequiredProperties
        environment_definition_required_properties_model['name'] = 'testString'
        environment_definition_required_properties_model['description'] = 'testString'
        environment_definition_required_properties_model['authorizations'] = project_config_auth_model
        environment_definition_required_properties_model['inputs'] = input_variable_model
        environment_definition_required_properties_model['compliance_profile'] = project_compliance_profile_model

        environment_model = {}  # Environment
        environment_model['id'] = 'testString'
        environment_model['project'] = project_reference_model
        environment_model['created_at'] = '2019-01-01T12:00:00Z'
        environment_model['target_account'] = 'testString'
        environment_model['modified_at'] = '2019-01-01T12:00:00Z'
        environment_model['definition'] = environment_definition_required_properties_model

        # Construct a json representation of a EnvironmentCollection model
        environment_collection_model_json = {}
        environment_collection_model_json['environments'] = [environment_model]

        # Construct a model instance of EnvironmentCollection by calling from_dict on the json representation
        environment_collection_model = EnvironmentCollection.from_dict(environment_collection_model_json)
        assert environment_collection_model != False

        # Construct a model instance of EnvironmentCollection by calling from_dict on the json representation
        environment_collection_model_dict = EnvironmentCollection.from_dict(environment_collection_model_json).__dict__
        environment_collection_model2 = EnvironmentCollection(**environment_collection_model_dict)

        # Verify the model instances are equivalent
        assert environment_collection_model == environment_collection_model2

        # Convert model instance back to dict and verify no loss of data
        environment_collection_model_json2 = environment_collection_model.to_dict()
        assert environment_collection_model_json2 == environment_collection_model_json


class TestModel_EnvironmentDefinitionNameDescription:
    """
    Test Class for EnvironmentDefinitionNameDescription
    """

    def test_environment_definition_name_description_serialization(self):
        """
        Test serialization/deserialization for EnvironmentDefinitionNameDescription
        """

        # Construct a json representation of a EnvironmentDefinitionNameDescription model
        environment_definition_name_description_model_json = {}
        environment_definition_name_description_model_json['name'] = 'testString'
        environment_definition_name_description_model_json['description'] = 'testString'

        # Construct a model instance of EnvironmentDefinitionNameDescription by calling from_dict on the json representation
        environment_definition_name_description_model = EnvironmentDefinitionNameDescription.from_dict(environment_definition_name_description_model_json)
        assert environment_definition_name_description_model != False

        # Construct a model instance of EnvironmentDefinitionNameDescription by calling from_dict on the json representation
        environment_definition_name_description_model_dict = EnvironmentDefinitionNameDescription.from_dict(environment_definition_name_description_model_json).__dict__
        environment_definition_name_description_model2 = EnvironmentDefinitionNameDescription(**environment_definition_name_description_model_dict)

        # Verify the model instances are equivalent
        assert environment_definition_name_description_model == environment_definition_name_description_model2

        # Convert model instance back to dict and verify no loss of data
        environment_definition_name_description_model_json2 = environment_definition_name_description_model.to_dict()
        assert environment_definition_name_description_model_json2 == environment_definition_name_description_model_json


class TestModel_EnvironmentDefinitionProperties:
    """
    Test Class for EnvironmentDefinitionProperties
    """

    def test_environment_definition_properties_serialization(self):
        """
        Test serialization/deserialization for EnvironmentDefinitionProperties
        """

        # Construct dict forms of any model objects needed in order to build this model.

        project_config_auth_model = {}  # ProjectConfigAuth
        project_config_auth_model['trusted_profile_id'] = 'testString'
        project_config_auth_model['method'] = 'api_key'
        project_config_auth_model['api_key'] = 'testString'

        input_variable_model = {}  # InputVariable
        input_variable_model['foo'] = 'testString'

        project_compliance_profile_model = {}  # ProjectComplianceProfile
        project_compliance_profile_model['id'] = 'testString'
        project_compliance_profile_model['instance_id'] = 'testString'
        project_compliance_profile_model['instance_location'] = 'testString'
        project_compliance_profile_model['attachment_id'] = 'testString'
        project_compliance_profile_model['profile_name'] = 'testString'

        # Construct a json representation of a EnvironmentDefinitionProperties model
        environment_definition_properties_model_json = {}
        environment_definition_properties_model_json['name'] = 'testString'
        environment_definition_properties_model_json['description'] = 'testString'
        environment_definition_properties_model_json['authorizations'] = project_config_auth_model
        environment_definition_properties_model_json['inputs'] = input_variable_model
        environment_definition_properties_model_json['compliance_profile'] = project_compliance_profile_model

        # Construct a model instance of EnvironmentDefinitionProperties by calling from_dict on the json representation
        environment_definition_properties_model = EnvironmentDefinitionProperties.from_dict(environment_definition_properties_model_json)
        assert environment_definition_properties_model != False

        # Construct a model instance of EnvironmentDefinitionProperties by calling from_dict on the json representation
        environment_definition_properties_model_dict = EnvironmentDefinitionProperties.from_dict(environment_definition_properties_model_json).__dict__
        environment_definition_properties_model2 = EnvironmentDefinitionProperties(**environment_definition_properties_model_dict)

        # Verify the model instances are equivalent
        assert environment_definition_properties_model == environment_definition_properties_model2

        # Convert model instance back to dict and verify no loss of data
        environment_definition_properties_model_json2 = environment_definition_properties_model.to_dict()
        assert environment_definition_properties_model_json2 == environment_definition_properties_model_json


class TestModel_EnvironmentDefinitionRequiredProperties:
    """
    Test Class for EnvironmentDefinitionRequiredProperties
    """

    def test_environment_definition_required_properties_serialization(self):
        """
        Test serialization/deserialization for EnvironmentDefinitionRequiredProperties
        """

        # Construct dict forms of any model objects needed in order to build this model.

        project_config_auth_model = {}  # ProjectConfigAuth
        project_config_auth_model['trusted_profile_id'] = 'testString'
        project_config_auth_model['method'] = 'api_key'
        project_config_auth_model['api_key'] = 'testString'

        input_variable_model = {}  # InputVariable
        input_variable_model['foo'] = 'testString'

        project_compliance_profile_model = {}  # ProjectComplianceProfile
        project_compliance_profile_model['id'] = 'testString'
        project_compliance_profile_model['instance_id'] = 'testString'
        project_compliance_profile_model['instance_location'] = 'testString'
        project_compliance_profile_model['attachment_id'] = 'testString'
        project_compliance_profile_model['profile_name'] = 'testString'

        # Construct a json representation of a EnvironmentDefinitionRequiredProperties model
        environment_definition_required_properties_model_json = {}
        environment_definition_required_properties_model_json['name'] = 'testString'
        environment_definition_required_properties_model_json['description'] = 'testString'
        environment_definition_required_properties_model_json['authorizations'] = project_config_auth_model
        environment_definition_required_properties_model_json['inputs'] = input_variable_model
        environment_definition_required_properties_model_json['compliance_profile'] = project_compliance_profile_model

        # Construct a model instance of EnvironmentDefinitionRequiredProperties by calling from_dict on the json representation
        environment_definition_required_properties_model = EnvironmentDefinitionRequiredProperties.from_dict(environment_definition_required_properties_model_json)
        assert environment_definition_required_properties_model != False

        # Construct a model instance of EnvironmentDefinitionRequiredProperties by calling from_dict on the json representation
        environment_definition_required_properties_model_dict = EnvironmentDefinitionRequiredProperties.from_dict(environment_definition_required_properties_model_json).__dict__
        environment_definition_required_properties_model2 = EnvironmentDefinitionRequiredProperties(**environment_definition_required_properties_model_dict)

        # Verify the model instances are equivalent
        assert environment_definition_required_properties_model == environment_definition_required_properties_model2

        # Convert model instance back to dict and verify no loss of data
        environment_definition_required_properties_model_json2 = environment_definition_required_properties_model.to_dict()
        assert environment_definition_required_properties_model_json2 == environment_definition_required_properties_model_json


class TestModel_EnvironmentDeleteResponse:
    """
    Test Class for EnvironmentDeleteResponse
    """

    def test_environment_delete_response_serialization(self):
        """
        Test serialization/deserialization for EnvironmentDeleteResponse
        """

        # Construct a json representation of a EnvironmentDeleteResponse model
        environment_delete_response_model_json = {}
        environment_delete_response_model_json['id'] = 'testString'

        # Construct a model instance of EnvironmentDeleteResponse by calling from_dict on the json representation
        environment_delete_response_model = EnvironmentDeleteResponse.from_dict(environment_delete_response_model_json)
        assert environment_delete_response_model != False

        # Construct a model instance of EnvironmentDeleteResponse by calling from_dict on the json representation
        environment_delete_response_model_dict = EnvironmentDeleteResponse.from_dict(environment_delete_response_model_json).__dict__
        environment_delete_response_model2 = EnvironmentDeleteResponse(**environment_delete_response_model_dict)

        # Verify the model instances are equivalent
        assert environment_delete_response_model == environment_delete_response_model2

        # Convert model instance back to dict and verify no loss of data
        environment_delete_response_model_json2 = environment_delete_response_model.to_dict()
        assert environment_delete_response_model_json2 == environment_delete_response_model_json


class TestModel_InputVariable:
    """
    Test Class for InputVariable
    """

    def test_input_variable_serialization(self):
        """
        Test serialization/deserialization for InputVariable
        """

        # Construct a json representation of a InputVariable model
        input_variable_model_json = {}
        input_variable_model_json['foo'] = 'testString'

        # Construct a model instance of InputVariable by calling from_dict on the json representation
        input_variable_model = InputVariable.from_dict(input_variable_model_json)
        assert input_variable_model != False

        # Construct a model instance of InputVariable by calling from_dict on the json representation
        input_variable_model_dict = InputVariable.from_dict(input_variable_model_json).__dict__
        input_variable_model2 = InputVariable(**input_variable_model_dict)

        # Verify the model instances are equivalent
        assert input_variable_model == input_variable_model2

        # Convert model instance back to dict and verify no loss of data
        input_variable_model_json2 = input_variable_model.to_dict()
        assert input_variable_model_json2 == input_variable_model_json

        # Test get_properties and set_properties methods.
        input_variable_model.set_properties({})
        actual_dict = input_variable_model.get_properties()
        assert actual_dict == {}

        expected_dict = {'foo': 'testString'}
        input_variable_model.set_properties(expected_dict)
        actual_dict = input_variable_model.get_properties()
        assert actual_dict == expected_dict


class TestModel_LastActionWithSummary:
    """
    Test Class for LastActionWithSummary
    """

    def test_last_action_with_summary_serialization(self):
        """
        Test serialization/deserialization for LastActionWithSummary
        """

        # Construct dict forms of any model objects needed in order to build this model.

        pre_post_action_job_with_id_and_summary_model = {}  # PrePostActionJobWithIdAndSummary
        pre_post_action_job_with_id_and_summary_model['id'] = 'testString'
        pre_post_action_job_with_id_and_summary_model['summary'] = {'anyKey': 'anyValue'}

        action_job_plan_summary_model = {}  # ActionJobPlanSummary
        action_job_plan_summary_model['add'] = 38
        action_job_plan_summary_model['failed'] = 38
        action_job_plan_summary_model['update'] = 38
        action_job_plan_summary_model['destroy'] = 38
        action_job_plan_summary_model['add_resources'] = ['testString']
        action_job_plan_summary_model['failed_resources'] = ['testString']
        action_job_plan_summary_model['updated_resources'] = ['testString']
        action_job_plan_summary_model['destroy_resources'] = ['testString']

        action_job_apply_summary_model = {}  # ActionJobApplySummary
        action_job_apply_summary_model['success'] = 38
        action_job_apply_summary_model['failed'] = 38
        action_job_apply_summary_model['success_resources'] = ['testString']
        action_job_apply_summary_model['failed_resources'] = ['testString']

        action_job_destroy_summary_resources_model = {}  # ActionJobDestroySummaryResources
        action_job_destroy_summary_resources_model['success'] = ['testString']
        action_job_destroy_summary_resources_model['failed'] = ['testString']
        action_job_destroy_summary_resources_model['tainted'] = ['testString']

        action_job_destroy_summary_model = {}  # ActionJobDestroySummary
        action_job_destroy_summary_model['success'] = 38
        action_job_destroy_summary_model['failed'] = 38
        action_job_destroy_summary_model['tainted'] = 38
        action_job_destroy_summary_model['resources'] = action_job_destroy_summary_resources_model

        action_job_message_summary_model = {}  # ActionJobMessageSummary
        action_job_message_summary_model['info'] = 38
        action_job_message_summary_model['debug'] = 38
        action_job_message_summary_model['error'] = 38

        terraform_log_analyzer_error_message_model = {}  # TerraformLogAnalyzerErrorMessage
        terraform_log_analyzer_error_message_model['foo'] = 'testString'

        action_job_plan_messages_summary_model = {}  # ActionJobPlanMessagesSummary
        action_job_plan_messages_summary_model['error_messages'] = [terraform_log_analyzer_error_message_model]
        action_job_plan_messages_summary_model['sucess_message'] = ['testString']
        action_job_plan_messages_summary_model['update_message'] = ['testString']
        action_job_plan_messages_summary_model['destroy_message'] = ['testString']

        terraform_log_analyzer_success_message_model = {}  # TerraformLogAnalyzerSuccessMessage
        terraform_log_analyzer_success_message_model['resource_type'] = 'testString'
        terraform_log_analyzer_success_message_model['time-taken'] = 'testString'
        terraform_log_analyzer_success_message_model['id'] = 'testString'

        action_job_apply_messages_summary_model = {}  # ActionJobApplyMessagesSummary
        action_job_apply_messages_summary_model['error_messages'] = [terraform_log_analyzer_error_message_model]
        action_job_apply_messages_summary_model['sucess_message'] = [terraform_log_analyzer_success_message_model]

        action_job_destroy_messages_summary_model = {}  # ActionJobDestroyMessagesSummary
        action_job_destroy_messages_summary_model['error_messages'] = [terraform_log_analyzer_error_message_model]

        action_job_summary_model = {}  # ActionJobSummary
        action_job_summary_model['plan_summary'] = action_job_plan_summary_model
        action_job_summary_model['apply_summary'] = action_job_apply_summary_model
        action_job_summary_model['destroy_summary'] = action_job_destroy_summary_model
        action_job_summary_model['message_summary'] = action_job_message_summary_model
        action_job_summary_model['plan_messages'] = action_job_plan_messages_summary_model
        action_job_summary_model['apply_messages'] = action_job_apply_messages_summary_model
        action_job_summary_model['destroy_messages'] = action_job_destroy_messages_summary_model

        action_job_with_id_and_summary_model = {}  # ActionJobWithIdAndSummary
        action_job_with_id_and_summary_model['id'] = 'testString'
        action_job_with_id_and_summary_model['summary'] = action_job_summary_model

        # Construct a json representation of a LastActionWithSummary model
        last_action_with_summary_model_json = {}
        last_action_with_summary_model_json['href'] = 'testString'
        last_action_with_summary_model_json['result'] = 'failed'
        last_action_with_summary_model_json['pre_job'] = pre_post_action_job_with_id_and_summary_model
        last_action_with_summary_model_json['post_job'] = pre_post_action_job_with_id_and_summary_model
        last_action_with_summary_model_json['job'] = action_job_with_id_and_summary_model

        # Construct a model instance of LastActionWithSummary by calling from_dict on the json representation
        last_action_with_summary_model = LastActionWithSummary.from_dict(last_action_with_summary_model_json)
        assert last_action_with_summary_model != False

        # Construct a model instance of LastActionWithSummary by calling from_dict on the json representation
        last_action_with_summary_model_dict = LastActionWithSummary.from_dict(last_action_with_summary_model_json).__dict__
        last_action_with_summary_model2 = LastActionWithSummary(**last_action_with_summary_model_dict)

        # Verify the model instances are equivalent
        assert last_action_with_summary_model == last_action_with_summary_model2

        # Convert model instance back to dict and verify no loss of data
        last_action_with_summary_model_json2 = last_action_with_summary_model.to_dict()
        assert last_action_with_summary_model_json2 == last_action_with_summary_model_json


class TestModel_LastValidatedActionWithSummary:
    """
    Test Class for LastValidatedActionWithSummary
    """

    def test_last_validated_action_with_summary_serialization(self):
        """
        Test serialization/deserialization for LastValidatedActionWithSummary
        """

        # Construct dict forms of any model objects needed in order to build this model.

        pre_post_action_job_with_id_and_summary_model = {}  # PrePostActionJobWithIdAndSummary
        pre_post_action_job_with_id_and_summary_model['id'] = 'testString'
        pre_post_action_job_with_id_and_summary_model['summary'] = {'anyKey': 'anyValue'}

        action_job_plan_summary_model = {}  # ActionJobPlanSummary
        action_job_plan_summary_model['add'] = 38
        action_job_plan_summary_model['failed'] = 38
        action_job_plan_summary_model['update'] = 38
        action_job_plan_summary_model['destroy'] = 38
        action_job_plan_summary_model['add_resources'] = ['testString']
        action_job_plan_summary_model['failed_resources'] = ['testString']
        action_job_plan_summary_model['updated_resources'] = ['testString']
        action_job_plan_summary_model['destroy_resources'] = ['testString']

        action_job_apply_summary_model = {}  # ActionJobApplySummary
        action_job_apply_summary_model['success'] = 38
        action_job_apply_summary_model['failed'] = 38
        action_job_apply_summary_model['success_resources'] = ['testString']
        action_job_apply_summary_model['failed_resources'] = ['testString']

        action_job_destroy_summary_resources_model = {}  # ActionJobDestroySummaryResources
        action_job_destroy_summary_resources_model['success'] = ['testString']
        action_job_destroy_summary_resources_model['failed'] = ['testString']
        action_job_destroy_summary_resources_model['tainted'] = ['testString']

        action_job_destroy_summary_model = {}  # ActionJobDestroySummary
        action_job_destroy_summary_model['success'] = 38
        action_job_destroy_summary_model['failed'] = 38
        action_job_destroy_summary_model['tainted'] = 38
        action_job_destroy_summary_model['resources'] = action_job_destroy_summary_resources_model

        action_job_message_summary_model = {}  # ActionJobMessageSummary
        action_job_message_summary_model['info'] = 38
        action_job_message_summary_model['debug'] = 38
        action_job_message_summary_model['error'] = 38

        terraform_log_analyzer_error_message_model = {}  # TerraformLogAnalyzerErrorMessage
        terraform_log_analyzer_error_message_model['foo'] = 'testString'

        action_job_plan_messages_summary_model = {}  # ActionJobPlanMessagesSummary
        action_job_plan_messages_summary_model['error_messages'] = [terraform_log_analyzer_error_message_model]
        action_job_plan_messages_summary_model['sucess_message'] = ['testString']
        action_job_plan_messages_summary_model['update_message'] = ['testString']
        action_job_plan_messages_summary_model['destroy_message'] = ['testString']

        terraform_log_analyzer_success_message_model = {}  # TerraformLogAnalyzerSuccessMessage
        terraform_log_analyzer_success_message_model['resource_type'] = 'testString'
        terraform_log_analyzer_success_message_model['time-taken'] = 'testString'
        terraform_log_analyzer_success_message_model['id'] = 'testString'

        action_job_apply_messages_summary_model = {}  # ActionJobApplyMessagesSummary
        action_job_apply_messages_summary_model['error_messages'] = [terraform_log_analyzer_error_message_model]
        action_job_apply_messages_summary_model['sucess_message'] = [terraform_log_analyzer_success_message_model]

        action_job_destroy_messages_summary_model = {}  # ActionJobDestroyMessagesSummary
        action_job_destroy_messages_summary_model['error_messages'] = [terraform_log_analyzer_error_message_model]

        action_job_summary_model = {}  # ActionJobSummary
        action_job_summary_model['plan_summary'] = action_job_plan_summary_model
        action_job_summary_model['apply_summary'] = action_job_apply_summary_model
        action_job_summary_model['destroy_summary'] = action_job_destroy_summary_model
        action_job_summary_model['message_summary'] = action_job_message_summary_model
        action_job_summary_model['plan_messages'] = action_job_plan_messages_summary_model
        action_job_summary_model['apply_messages'] = action_job_apply_messages_summary_model
        action_job_summary_model['destroy_messages'] = action_job_destroy_messages_summary_model

        action_job_with_id_and_summary_model = {}  # ActionJobWithIdAndSummary
        action_job_with_id_and_summary_model['id'] = 'testString'
        action_job_with_id_and_summary_model['summary'] = action_job_summary_model

        project_config_metadata_cost_estimate_model = {}  # ProjectConfigMetadataCostEstimate
        project_config_metadata_cost_estimate_model['version'] = 'testString'
        project_config_metadata_cost_estimate_model['currency'] = 'USD'
        project_config_metadata_cost_estimate_model['totalHourlyCost'] = 'testString'
        project_config_metadata_cost_estimate_model['totalMonthlyCost'] = 'testString'
        project_config_metadata_cost_estimate_model['pastTotalHourlyCost'] = 'testString'
        project_config_metadata_cost_estimate_model['pastTotalMonthlyCost'] = 'testString'
        project_config_metadata_cost_estimate_model['diffTotalHourlyCost'] = 'testString'
        project_config_metadata_cost_estimate_model['diffTotalMonthlyCost'] = 'testString'
        project_config_metadata_cost_estimate_model['timeGenerated'] = '2019-01-01T12:00:00Z'
        project_config_metadata_cost_estimate_model['user_id'] = 'testString'

        code_risk_analyzer_logs_summary_model = {}  # CodeRiskAnalyzerLogsSummary
        code_risk_analyzer_logs_summary_model['total'] = 'testString'
        code_risk_analyzer_logs_summary_model['passed'] = 'testString'
        code_risk_analyzer_logs_summary_model['failed'] = 'testString'
        code_risk_analyzer_logs_summary_model['skipped'] = 'testString'

        project_config_metadata_code_risk_analyzer_logs_model = {}  # ProjectConfigMetadataCodeRiskAnalyzerLogs
        project_config_metadata_code_risk_analyzer_logs_model['cra_version'] = 'testString'
        project_config_metadata_code_risk_analyzer_logs_model['schema_version'] = 'testString'
        project_config_metadata_code_risk_analyzer_logs_model['status'] = 'passed'
        project_config_metadata_code_risk_analyzer_logs_model['summary'] = code_risk_analyzer_logs_summary_model
        project_config_metadata_code_risk_analyzer_logs_model['timestamp'] = '2019-01-01T12:00:00Z'

        # Construct a json representation of a LastValidatedActionWithSummary model
        last_validated_action_with_summary_model_json = {}
        last_validated_action_with_summary_model_json['href'] = 'testString'
        last_validated_action_with_summary_model_json['result'] = 'failed'
        last_validated_action_with_summary_model_json['pre_job'] = pre_post_action_job_with_id_and_summary_model
        last_validated_action_with_summary_model_json['post_job'] = pre_post_action_job_with_id_and_summary_model
        last_validated_action_with_summary_model_json['job'] = action_job_with_id_and_summary_model
        last_validated_action_with_summary_model_json['cost_estimate'] = project_config_metadata_cost_estimate_model
        last_validated_action_with_summary_model_json['cra_logs'] = project_config_metadata_code_risk_analyzer_logs_model

        # Construct a model instance of LastValidatedActionWithSummary by calling from_dict on the json representation
        last_validated_action_with_summary_model = LastValidatedActionWithSummary.from_dict(last_validated_action_with_summary_model_json)
        assert last_validated_action_with_summary_model != False

        # Construct a model instance of LastValidatedActionWithSummary by calling from_dict on the json representation
        last_validated_action_with_summary_model_dict = LastValidatedActionWithSummary.from_dict(last_validated_action_with_summary_model_json).__dict__
        last_validated_action_with_summary_model2 = LastValidatedActionWithSummary(**last_validated_action_with_summary_model_dict)

        # Verify the model instances are equivalent
        assert last_validated_action_with_summary_model == last_validated_action_with_summary_model2

        # Convert model instance back to dict and verify no loss of data
        last_validated_action_with_summary_model_json2 = last_validated_action_with_summary_model.to_dict()
        assert last_validated_action_with_summary_model_json2 == last_validated_action_with_summary_model_json


class TestModel_OutputValue:
    """
    Test Class for OutputValue
    """

    def test_output_value_serialization(self):
        """
        Test serialization/deserialization for OutputValue
        """

        # Construct a json representation of a OutputValue model
        output_value_model_json = {}
        output_value_model_json['name'] = 'testString'
        output_value_model_json['description'] = 'testString'
        output_value_model_json['value'] = 'testString'

        # Construct a model instance of OutputValue by calling from_dict on the json representation
        output_value_model = OutputValue.from_dict(output_value_model_json)
        assert output_value_model != False

        # Construct a model instance of OutputValue by calling from_dict on the json representation
        output_value_model_dict = OutputValue.from_dict(output_value_model_json).__dict__
        output_value_model2 = OutputValue(**output_value_model_dict)

        # Verify the model instances are equivalent
        assert output_value_model == output_value_model2

        # Convert model instance back to dict and verify no loss of data
        output_value_model_json2 = output_value_model.to_dict()
        assert output_value_model_json2 == output_value_model_json


class TestModel_PaginationLink:
    """
    Test Class for PaginationLink
    """

    def test_pagination_link_serialization(self):
        """
        Test serialization/deserialization for PaginationLink
        """

        # Construct a json representation of a PaginationLink model
        pagination_link_model_json = {}
        pagination_link_model_json['href'] = 'testString'

        # Construct a model instance of PaginationLink by calling from_dict on the json representation
        pagination_link_model = PaginationLink.from_dict(pagination_link_model_json)
        assert pagination_link_model != False

        # Construct a model instance of PaginationLink by calling from_dict on the json representation
        pagination_link_model_dict = PaginationLink.from_dict(pagination_link_model_json).__dict__
        pagination_link_model2 = PaginationLink(**pagination_link_model_dict)

        # Verify the model instances are equivalent
        assert pagination_link_model == pagination_link_model2

        # Convert model instance back to dict and verify no loss of data
        pagination_link_model_json2 = pagination_link_model.to_dict()
        assert pagination_link_model_json2 == pagination_link_model_json


class TestModel_PrePostActionJobWithIdAndSummary:
    """
    Test Class for PrePostActionJobWithIdAndSummary
    """

    def test_pre_post_action_job_with_id_and_summary_serialization(self):
        """
        Test serialization/deserialization for PrePostActionJobWithIdAndSummary
        """

        # Construct a json representation of a PrePostActionJobWithIdAndSummary model
        pre_post_action_job_with_id_and_summary_model_json = {}
        pre_post_action_job_with_id_and_summary_model_json['id'] = 'testString'
        pre_post_action_job_with_id_and_summary_model_json['summary'] = {'anyKey': 'anyValue'}

        # Construct a model instance of PrePostActionJobWithIdAndSummary by calling from_dict on the json representation
        pre_post_action_job_with_id_and_summary_model = PrePostActionJobWithIdAndSummary.from_dict(pre_post_action_job_with_id_and_summary_model_json)
        assert pre_post_action_job_with_id_and_summary_model != False

        # Construct a model instance of PrePostActionJobWithIdAndSummary by calling from_dict on the json representation
        pre_post_action_job_with_id_and_summary_model_dict = PrePostActionJobWithIdAndSummary.from_dict(pre_post_action_job_with_id_and_summary_model_json).__dict__
        pre_post_action_job_with_id_and_summary_model2 = PrePostActionJobWithIdAndSummary(**pre_post_action_job_with_id_and_summary_model_dict)

        # Verify the model instances are equivalent
        assert pre_post_action_job_with_id_and_summary_model == pre_post_action_job_with_id_and_summary_model2

        # Convert model instance back to dict and verify no loss of data
        pre_post_action_job_with_id_and_summary_model_json2 = pre_post_action_job_with_id_and_summary_model.to_dict()
        assert pre_post_action_job_with_id_and_summary_model_json2 == pre_post_action_job_with_id_and_summary_model_json


class TestModel_Project:
    """
    Test Class for Project
    """

    def test_project_serialization(self):
        """
        Test serialization/deserialization for Project
        """

        # Construct dict forms of any model objects needed in order to build this model.

        cumulative_needs_attention_model = {}  # CumulativeNeedsAttention
        cumulative_needs_attention_model['event'] = 'testString'
        cumulative_needs_attention_model['event_id'] = 'testString'
        cumulative_needs_attention_model['config_id'] = 'testString'
        cumulative_needs_attention_model['config_version'] = 38

        project_config_version_summary_model = {}  # ProjectConfigVersionSummary
        project_config_version_summary_model['state'] = 'approved'
        project_config_version_summary_model['version'] = 38
        project_config_version_summary_model['href'] = 'testString'

        project_config_definition_name_description_model = {}  # ProjectConfigDefinitionNameDescription
        project_config_definition_name_description_model['name'] = 'testString'
        project_config_definition_name_description_model['description'] = 'testString'

        project_definition_reference_model = {}  # ProjectDefinitionReference
        project_definition_reference_model['name'] = 'testString'

        project_reference_model = {}  # ProjectReference
        project_reference_model['id'] = 'testString'
        project_reference_model['definition'] = project_definition_reference_model
        project_reference_model['crn'] = 'crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::'
        project_reference_model['href'] = 'testString'

        project_config_summary_model = {}  # ProjectConfigSummary
        project_config_summary_model['approved_version'] = project_config_version_summary_model
        project_config_summary_model['deployed_version'] = project_config_version_summary_model
        project_config_summary_model['id'] = 'testString'
        project_config_summary_model['version'] = 38
        project_config_summary_model['state'] = 'approved'
        project_config_summary_model['created_at'] = '2019-01-01T12:00:00Z'
        project_config_summary_model['modified_at'] = '2019-01-01T12:00:00Z'
        project_config_summary_model['href'] = 'testString'
        project_config_summary_model['definition'] = project_config_definition_name_description_model
        project_config_summary_model['project'] = project_reference_model

        environment_definition_name_description_model = {}  # EnvironmentDefinitionNameDescription
        environment_definition_name_description_model['name'] = 'testString'
        environment_definition_name_description_model['description'] = 'testString'

        project_environment_summary_model = {}  # ProjectEnvironmentSummary
        project_environment_summary_model['id'] = 'testString'
        project_environment_summary_model['project'] = project_reference_model
        project_environment_summary_model['created_at'] = '2019-01-01T12:00:00Z'
        project_environment_summary_model['href'] = 'testString'
        project_environment_summary_model['definition'] = environment_definition_name_description_model

        project_definition_properties_model = {}  # ProjectDefinitionProperties
        project_definition_properties_model['name'] = 'testString'
        project_definition_properties_model['description'] = 'testString'
        project_definition_properties_model['destroy_on_delete'] = True

        # Construct a json representation of a Project model
        project_model_json = {}
        project_model_json['crn'] = 'crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::'
        project_model_json['created_at'] = '2019-01-01T12:00:00Z'
        project_model_json['cumulative_needs_attention_view'] = [cumulative_needs_attention_model]
        project_model_json['cumulative_needs_attention_view_error'] = False
        project_model_json['id'] = 'testString'
        project_model_json['location'] = 'testString'
        project_model_json['resource_group_id'] = 'testString'
        project_model_json['state'] = 'ready'
        project_model_json['resource_group'] = 'testString'
        project_model_json['event_notifications_crn'] = 'testString'
        project_model_json['configs'] = [project_config_summary_model]
        project_model_json['environments'] = [project_environment_summary_model]
        project_model_json['definition'] = project_definition_properties_model

        # Construct a model instance of Project by calling from_dict on the json representation
        project_model = Project.from_dict(project_model_json)
        assert project_model != False

        # Construct a model instance of Project by calling from_dict on the json representation
        project_model_dict = Project.from_dict(project_model_json).__dict__
        project_model2 = Project(**project_model_dict)

        # Verify the model instances are equivalent
        assert project_model == project_model2

        # Convert model instance back to dict and verify no loss of data
        project_model_json2 = project_model.to_dict()
        assert project_model_json2 == project_model_json


class TestModel_ProjectCollection:
    """
    Test Class for ProjectCollection
    """

    def test_project_collection_serialization(self):
        """
        Test serialization/deserialization for ProjectCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        pagination_link_model = {}  # PaginationLink
        pagination_link_model['href'] = 'testString'

        cumulative_needs_attention_model = {}  # CumulativeNeedsAttention
        cumulative_needs_attention_model['event'] = 'testString'
        cumulative_needs_attention_model['event_id'] = 'testString'
        cumulative_needs_attention_model['config_id'] = 'testString'
        cumulative_needs_attention_model['config_version'] = 38

        project_definition_properties_model = {}  # ProjectDefinitionProperties
        project_definition_properties_model['name'] = 'testString'
        project_definition_properties_model['description'] = 'testString'
        project_definition_properties_model['destroy_on_delete'] = True

        project_summary_model = {}  # ProjectSummary
        project_summary_model['crn'] = 'crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::'
        project_summary_model['created_at'] = '2019-01-01T12:00:00Z'
        project_summary_model['cumulative_needs_attention_view'] = [cumulative_needs_attention_model]
        project_summary_model['cumulative_needs_attention_view_error'] = False
        project_summary_model['id'] = 'testString'
        project_summary_model['location'] = 'testString'
        project_summary_model['resource_group_id'] = 'testString'
        project_summary_model['state'] = 'ready'
        project_summary_model['definition'] = project_definition_properties_model

        # Construct a json representation of a ProjectCollection model
        project_collection_model_json = {}
        project_collection_model_json['limit'] = 10
        project_collection_model_json['total_count'] = 0
        project_collection_model_json['first'] = pagination_link_model
        project_collection_model_json['last'] = pagination_link_model
        project_collection_model_json['previous'] = pagination_link_model
        project_collection_model_json['next'] = pagination_link_model
        project_collection_model_json['projects'] = [project_summary_model]

        # Construct a model instance of ProjectCollection by calling from_dict on the json representation
        project_collection_model = ProjectCollection.from_dict(project_collection_model_json)
        assert project_collection_model != False

        # Construct a model instance of ProjectCollection by calling from_dict on the json representation
        project_collection_model_dict = ProjectCollection.from_dict(project_collection_model_json).__dict__
        project_collection_model2 = ProjectCollection(**project_collection_model_dict)

        # Verify the model instances are equivalent
        assert project_collection_model == project_collection_model2

        # Convert model instance back to dict and verify no loss of data
        project_collection_model_json2 = project_collection_model.to_dict()
        assert project_collection_model_json2 == project_collection_model_json


class TestModel_ProjectComplianceProfile:
    """
    Test Class for ProjectComplianceProfile
    """

    def test_project_compliance_profile_serialization(self):
        """
        Test serialization/deserialization for ProjectComplianceProfile
        """

        # Construct a json representation of a ProjectComplianceProfile model
        project_compliance_profile_model_json = {}
        project_compliance_profile_model_json['id'] = 'testString'
        project_compliance_profile_model_json['instance_id'] = 'testString'
        project_compliance_profile_model_json['instance_location'] = 'testString'
        project_compliance_profile_model_json['attachment_id'] = 'testString'
        project_compliance_profile_model_json['profile_name'] = 'testString'

        # Construct a model instance of ProjectComplianceProfile by calling from_dict on the json representation
        project_compliance_profile_model = ProjectComplianceProfile.from_dict(project_compliance_profile_model_json)
        assert project_compliance_profile_model != False

        # Construct a model instance of ProjectComplianceProfile by calling from_dict on the json representation
        project_compliance_profile_model_dict = ProjectComplianceProfile.from_dict(project_compliance_profile_model_json).__dict__
        project_compliance_profile_model2 = ProjectComplianceProfile(**project_compliance_profile_model_dict)

        # Verify the model instances are equivalent
        assert project_compliance_profile_model == project_compliance_profile_model2

        # Convert model instance back to dict and verify no loss of data
        project_compliance_profile_model_json2 = project_compliance_profile_model.to_dict()
        assert project_compliance_profile_model_json2 == project_compliance_profile_model_json


class TestModel_ProjectConfig:
    """
    Test Class for ProjectConfig
    """

    def test_project_config_serialization(self):
        """
        Test serialization/deserialization for ProjectConfig
        """

        # Construct dict forms of any model objects needed in order to build this model.

        project_config_metadata_last_approved_model = {}  # ProjectConfigMetadataLastApproved
        project_config_metadata_last_approved_model['at'] = '2019-01-01T12:00:00Z'
        project_config_metadata_last_approved_model['comment'] = 'testString'
        project_config_metadata_last_approved_model['is_forced'] = True
        project_config_metadata_last_approved_model['user_id'] = 'testString'

        pre_post_action_job_with_id_and_summary_model = {}  # PrePostActionJobWithIdAndSummary
        pre_post_action_job_with_id_and_summary_model['id'] = 'testString'
        pre_post_action_job_with_id_and_summary_model['summary'] = {'anyKey': 'anyValue'}

        action_job_plan_summary_model = {}  # ActionJobPlanSummary
        action_job_plan_summary_model['add'] = 38
        action_job_plan_summary_model['failed'] = 38
        action_job_plan_summary_model['update'] = 38
        action_job_plan_summary_model['destroy'] = 38
        action_job_plan_summary_model['add_resources'] = ['testString']
        action_job_plan_summary_model['failed_resources'] = ['testString']
        action_job_plan_summary_model['updated_resources'] = ['testString']
        action_job_plan_summary_model['destroy_resources'] = ['testString']

        action_job_apply_summary_model = {}  # ActionJobApplySummary
        action_job_apply_summary_model['success'] = 38
        action_job_apply_summary_model['failed'] = 38
        action_job_apply_summary_model['success_resources'] = ['testString']
        action_job_apply_summary_model['failed_resources'] = ['testString']

        action_job_destroy_summary_resources_model = {}  # ActionJobDestroySummaryResources
        action_job_destroy_summary_resources_model['success'] = ['testString']
        action_job_destroy_summary_resources_model['failed'] = ['testString']
        action_job_destroy_summary_resources_model['tainted'] = ['testString']

        action_job_destroy_summary_model = {}  # ActionJobDestroySummary
        action_job_destroy_summary_model['success'] = 38
        action_job_destroy_summary_model['failed'] = 38
        action_job_destroy_summary_model['tainted'] = 38
        action_job_destroy_summary_model['resources'] = action_job_destroy_summary_resources_model

        action_job_message_summary_model = {}  # ActionJobMessageSummary
        action_job_message_summary_model['info'] = 38
        action_job_message_summary_model['debug'] = 38
        action_job_message_summary_model['error'] = 38

        terraform_log_analyzer_error_message_model = {}  # TerraformLogAnalyzerErrorMessage
        terraform_log_analyzer_error_message_model['foo'] = 'testString'

        action_job_plan_messages_summary_model = {}  # ActionJobPlanMessagesSummary
        action_job_plan_messages_summary_model['error_messages'] = [terraform_log_analyzer_error_message_model]
        action_job_plan_messages_summary_model['sucess_message'] = ['testString']
        action_job_plan_messages_summary_model['update_message'] = ['testString']
        action_job_plan_messages_summary_model['destroy_message'] = ['testString']

        terraform_log_analyzer_success_message_model = {}  # TerraformLogAnalyzerSuccessMessage
        terraform_log_analyzer_success_message_model['resource_type'] = 'testString'
        terraform_log_analyzer_success_message_model['time-taken'] = 'testString'
        terraform_log_analyzer_success_message_model['id'] = 'testString'

        action_job_apply_messages_summary_model = {}  # ActionJobApplyMessagesSummary
        action_job_apply_messages_summary_model['error_messages'] = [terraform_log_analyzer_error_message_model]
        action_job_apply_messages_summary_model['sucess_message'] = [terraform_log_analyzer_success_message_model]

        action_job_destroy_messages_summary_model = {}  # ActionJobDestroyMessagesSummary
        action_job_destroy_messages_summary_model['error_messages'] = [terraform_log_analyzer_error_message_model]

        action_job_summary_model = {}  # ActionJobSummary
        action_job_summary_model['plan_summary'] = action_job_plan_summary_model
        action_job_summary_model['apply_summary'] = action_job_apply_summary_model
        action_job_summary_model['destroy_summary'] = action_job_destroy_summary_model
        action_job_summary_model['message_summary'] = action_job_message_summary_model
        action_job_summary_model['plan_messages'] = action_job_plan_messages_summary_model
        action_job_summary_model['apply_messages'] = action_job_apply_messages_summary_model
        action_job_summary_model['destroy_messages'] = action_job_destroy_messages_summary_model

        action_job_with_id_and_summary_model = {}  # ActionJobWithIdAndSummary
        action_job_with_id_and_summary_model['id'] = 'testString'
        action_job_with_id_and_summary_model['summary'] = action_job_summary_model

        project_config_metadata_cost_estimate_model = {}  # ProjectConfigMetadataCostEstimate
        project_config_metadata_cost_estimate_model['version'] = 'testString'
        project_config_metadata_cost_estimate_model['currency'] = 'USD'
        project_config_metadata_cost_estimate_model['totalHourlyCost'] = 'testString'
        project_config_metadata_cost_estimate_model['totalMonthlyCost'] = 'testString'
        project_config_metadata_cost_estimate_model['pastTotalHourlyCost'] = 'testString'
        project_config_metadata_cost_estimate_model['pastTotalMonthlyCost'] = 'testString'
        project_config_metadata_cost_estimate_model['diffTotalHourlyCost'] = 'testString'
        project_config_metadata_cost_estimate_model['diffTotalMonthlyCost'] = 'testString'
        project_config_metadata_cost_estimate_model['timeGenerated'] = '2019-01-01T12:00:00Z'
        project_config_metadata_cost_estimate_model['user_id'] = 'testString'

        code_risk_analyzer_logs_summary_model = {}  # CodeRiskAnalyzerLogsSummary
        code_risk_analyzer_logs_summary_model['total'] = 'testString'
        code_risk_analyzer_logs_summary_model['passed'] = 'testString'
        code_risk_analyzer_logs_summary_model['failed'] = 'testString'
        code_risk_analyzer_logs_summary_model['skipped'] = 'testString'

        project_config_metadata_code_risk_analyzer_logs_model = {}  # ProjectConfigMetadataCodeRiskAnalyzerLogs
        project_config_metadata_code_risk_analyzer_logs_model['cra_version'] = 'testString'
        project_config_metadata_code_risk_analyzer_logs_model['schema_version'] = 'testString'
        project_config_metadata_code_risk_analyzer_logs_model['status'] = 'passed'
        project_config_metadata_code_risk_analyzer_logs_model['summary'] = code_risk_analyzer_logs_summary_model
        project_config_metadata_code_risk_analyzer_logs_model['timestamp'] = '2019-01-01T12:00:00Z'

        last_validated_action_with_summary_model = {}  # LastValidatedActionWithSummary
        last_validated_action_with_summary_model['href'] = 'testString'
        last_validated_action_with_summary_model['result'] = 'failed'
        last_validated_action_with_summary_model['pre_job'] = pre_post_action_job_with_id_and_summary_model
        last_validated_action_with_summary_model['post_job'] = pre_post_action_job_with_id_and_summary_model
        last_validated_action_with_summary_model['job'] = action_job_with_id_and_summary_model
        last_validated_action_with_summary_model['cost_estimate'] = project_config_metadata_cost_estimate_model
        last_validated_action_with_summary_model['cra_logs'] = project_config_metadata_code_risk_analyzer_logs_model

        last_action_with_summary_model = {}  # LastActionWithSummary
        last_action_with_summary_model['href'] = 'testString'
        last_action_with_summary_model['result'] = 'failed'
        last_action_with_summary_model['pre_job'] = pre_post_action_job_with_id_and_summary_model
        last_action_with_summary_model['post_job'] = pre_post_action_job_with_id_and_summary_model
        last_action_with_summary_model['job'] = action_job_with_id_and_summary_model

        output_value_model = {}  # OutputValue
        output_value_model['name'] = 'testString'
        output_value_model['description'] = 'testString'
        output_value_model['value'] = 'testString'

        project_definition_reference_model = {}  # ProjectDefinitionReference
        project_definition_reference_model['name'] = 'testString'

        project_reference_model = {}  # ProjectReference
        project_reference_model['id'] = 'testString'
        project_reference_model['definition'] = project_definition_reference_model
        project_reference_model['crn'] = 'crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::'
        project_reference_model['href'] = 'testString'

        schematics_workspace_model = {}  # SchematicsWorkspace
        schematics_workspace_model['workspace_crn'] = 'testString'

        project_config_auth_model = {}  # ProjectConfigAuth
        project_config_auth_model['trusted_profile_id'] = 'testString'
        project_config_auth_model['method'] = 'api_key'
        project_config_auth_model['api_key'] = 'testString'

        project_compliance_profile_model = {}  # ProjectComplianceProfile
        project_compliance_profile_model['id'] = 'testString'
        project_compliance_profile_model['instance_id'] = 'testString'
        project_compliance_profile_model['instance_location'] = 'testString'
        project_compliance_profile_model['attachment_id'] = 'testString'
        project_compliance_profile_model['profile_name'] = 'testString'

        input_variable_model = {}  # InputVariable
        input_variable_model['foo'] = 'testString'

        project_config_setting_model = {}  # ProjectConfigSetting
        project_config_setting_model['foo'] = 'testString'

        project_config_response_definition_model = {}  # ProjectConfigResponseDefinition
        project_config_response_definition_model['name'] = 'testString'
        project_config_response_definition_model['description'] = 'testString'
        project_config_response_definition_model['environment'] = 'testString'
        project_config_response_definition_model['authorizations'] = project_config_auth_model
        project_config_response_definition_model['compliance_profile'] = project_compliance_profile_model
        project_config_response_definition_model['locator_id'] = 'testString'
        project_config_response_definition_model['inputs'] = input_variable_model
        project_config_response_definition_model['settings'] = project_config_setting_model
        project_config_response_definition_model['type'] = 'terraform_template'

        project_config_version_summary_model = {}  # ProjectConfigVersionSummary
        project_config_version_summary_model['state'] = 'approved'
        project_config_version_summary_model['version'] = 38
        project_config_version_summary_model['href'] = 'testString'

        # Construct a json representation of a ProjectConfig model
        project_config_model_json = {}
        project_config_model_json['id'] = 'testString'
        project_config_model_json['version'] = 38
        project_config_model_json['is_draft'] = True
        project_config_model_json['needs_attention_state'] = []
        project_config_model_json['created_at'] = '2019-01-01T12:00:00Z'
        project_config_model_json['modified_at'] = '2019-01-01T12:00:00Z'
        project_config_model_json['last_approved'] = project_config_metadata_last_approved_model
        project_config_model_json['last_saved_at'] = '2019-01-01T12:00:00Z'
        project_config_model_json['last_validated'] = last_validated_action_with_summary_model
        project_config_model_json['last_deployed'] = last_action_with_summary_model
        project_config_model_json['last_undeployed'] = last_action_with_summary_model
        project_config_model_json['outputs'] = [output_value_model]
        project_config_model_json['project'] = project_reference_model
        project_config_model_json['references'] = {'anyKey': 'anyValue'}
        project_config_model_json['schematics'] = schematics_workspace_model
        project_config_model_json['state'] = 'approved'
        project_config_model_json['update_available'] = True
        project_config_model_json['definition'] = project_config_response_definition_model
        project_config_model_json['approved_version'] = project_config_version_summary_model
        project_config_model_json['deployed_version'] = project_config_version_summary_model

        # Construct a model instance of ProjectConfig by calling from_dict on the json representation
        project_config_model = ProjectConfig.from_dict(project_config_model_json)
        assert project_config_model != False

        # Construct a model instance of ProjectConfig by calling from_dict on the json representation
        project_config_model_dict = ProjectConfig.from_dict(project_config_model_json).__dict__
        project_config_model2 = ProjectConfig(**project_config_model_dict)

        # Verify the model instances are equivalent
        assert project_config_model == project_config_model2

        # Convert model instance back to dict and verify no loss of data
        project_config_model_json2 = project_config_model.to_dict()
        assert project_config_model_json2 == project_config_model_json


class TestModel_ProjectConfigAuth:
    """
    Test Class for ProjectConfigAuth
    """

    def test_project_config_auth_serialization(self):
        """
        Test serialization/deserialization for ProjectConfigAuth
        """

        # Construct a json representation of a ProjectConfigAuth model
        project_config_auth_model_json = {}
        project_config_auth_model_json['trusted_profile_id'] = 'testString'
        project_config_auth_model_json['method'] = 'api_key'
        project_config_auth_model_json['api_key'] = 'testString'

        # Construct a model instance of ProjectConfigAuth by calling from_dict on the json representation
        project_config_auth_model = ProjectConfigAuth.from_dict(project_config_auth_model_json)
        assert project_config_auth_model != False

        # Construct a model instance of ProjectConfigAuth by calling from_dict on the json representation
        project_config_auth_model_dict = ProjectConfigAuth.from_dict(project_config_auth_model_json).__dict__
        project_config_auth_model2 = ProjectConfigAuth(**project_config_auth_model_dict)

        # Verify the model instances are equivalent
        assert project_config_auth_model == project_config_auth_model2

        # Convert model instance back to dict and verify no loss of data
        project_config_auth_model_json2 = project_config_auth_model.to_dict()
        assert project_config_auth_model_json2 == project_config_auth_model_json


class TestModel_ProjectConfigCollection:
    """
    Test Class for ProjectConfigCollection
    """

    def test_project_config_collection_serialization(self):
        """
        Test serialization/deserialization for ProjectConfigCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        project_config_version_summary_model = {}  # ProjectConfigVersionSummary
        project_config_version_summary_model['state'] = 'approved'
        project_config_version_summary_model['version'] = 38
        project_config_version_summary_model['href'] = 'testString'

        project_config_definition_name_description_model = {}  # ProjectConfigDefinitionNameDescription
        project_config_definition_name_description_model['name'] = 'testString'
        project_config_definition_name_description_model['description'] = 'testString'

        project_definition_reference_model = {}  # ProjectDefinitionReference
        project_definition_reference_model['name'] = 'testString'

        project_reference_model = {}  # ProjectReference
        project_reference_model['id'] = 'testString'
        project_reference_model['definition'] = project_definition_reference_model
        project_reference_model['crn'] = 'crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::'
        project_reference_model['href'] = 'testString'

        project_config_summary_model = {}  # ProjectConfigSummary
        project_config_summary_model['approved_version'] = project_config_version_summary_model
        project_config_summary_model['deployed_version'] = project_config_version_summary_model
        project_config_summary_model['id'] = 'testString'
        project_config_summary_model['version'] = 38
        project_config_summary_model['state'] = 'approved'
        project_config_summary_model['created_at'] = '2019-01-01T12:00:00Z'
        project_config_summary_model['modified_at'] = '2019-01-01T12:00:00Z'
        project_config_summary_model['href'] = 'testString'
        project_config_summary_model['definition'] = project_config_definition_name_description_model
        project_config_summary_model['project'] = project_reference_model

        # Construct a json representation of a ProjectConfigCollection model
        project_config_collection_model_json = {}
        project_config_collection_model_json['configs'] = [project_config_summary_model]

        # Construct a model instance of ProjectConfigCollection by calling from_dict on the json representation
        project_config_collection_model = ProjectConfigCollection.from_dict(project_config_collection_model_json)
        assert project_config_collection_model != False

        # Construct a model instance of ProjectConfigCollection by calling from_dict on the json representation
        project_config_collection_model_dict = ProjectConfigCollection.from_dict(project_config_collection_model_json).__dict__
        project_config_collection_model2 = ProjectConfigCollection(**project_config_collection_model_dict)

        # Verify the model instances are equivalent
        assert project_config_collection_model == project_config_collection_model2

        # Convert model instance back to dict and verify no loss of data
        project_config_collection_model_json2 = project_config_collection_model.to_dict()
        assert project_config_collection_model_json2 == project_config_collection_model_json


class TestModel_ProjectConfigDefinitionNameDescription:
    """
    Test Class for ProjectConfigDefinitionNameDescription
    """

    def test_project_config_definition_name_description_serialization(self):
        """
        Test serialization/deserialization for ProjectConfigDefinitionNameDescription
        """

        # Construct a json representation of a ProjectConfigDefinitionNameDescription model
        project_config_definition_name_description_model_json = {}
        project_config_definition_name_description_model_json['name'] = 'testString'
        project_config_definition_name_description_model_json['description'] = 'testString'

        # Construct a model instance of ProjectConfigDefinitionNameDescription by calling from_dict on the json representation
        project_config_definition_name_description_model = ProjectConfigDefinitionNameDescription.from_dict(project_config_definition_name_description_model_json)
        assert project_config_definition_name_description_model != False

        # Construct a model instance of ProjectConfigDefinitionNameDescription by calling from_dict on the json representation
        project_config_definition_name_description_model_dict = ProjectConfigDefinitionNameDescription.from_dict(project_config_definition_name_description_model_json).__dict__
        project_config_definition_name_description_model2 = ProjectConfigDefinitionNameDescription(**project_config_definition_name_description_model_dict)

        # Verify the model instances are equivalent
        assert project_config_definition_name_description_model == project_config_definition_name_description_model2

        # Convert model instance back to dict and verify no loss of data
        project_config_definition_name_description_model_json2 = project_config_definition_name_description_model.to_dict()
        assert project_config_definition_name_description_model_json2 == project_config_definition_name_description_model_json


class TestModel_ProjectConfigDelete:
    """
    Test Class for ProjectConfigDelete
    """

    def test_project_config_delete_serialization(self):
        """
        Test serialization/deserialization for ProjectConfigDelete
        """

        # Construct a json representation of a ProjectConfigDelete model
        project_config_delete_model_json = {}
        project_config_delete_model_json['id'] = 'testString'

        # Construct a model instance of ProjectConfigDelete by calling from_dict on the json representation
        project_config_delete_model = ProjectConfigDelete.from_dict(project_config_delete_model_json)
        assert project_config_delete_model != False

        # Construct a model instance of ProjectConfigDelete by calling from_dict on the json representation
        project_config_delete_model_dict = ProjectConfigDelete.from_dict(project_config_delete_model_json).__dict__
        project_config_delete_model2 = ProjectConfigDelete(**project_config_delete_model_dict)

        # Verify the model instances are equivalent
        assert project_config_delete_model == project_config_delete_model2

        # Convert model instance back to dict and verify no loss of data
        project_config_delete_model_json2 = project_config_delete_model.to_dict()
        assert project_config_delete_model_json2 == project_config_delete_model_json


class TestModel_ProjectConfigMetadataCodeRiskAnalyzerLogs:
    """
    Test Class for ProjectConfigMetadataCodeRiskAnalyzerLogs
    """

    def test_project_config_metadata_code_risk_analyzer_logs_serialization(self):
        """
        Test serialization/deserialization for ProjectConfigMetadataCodeRiskAnalyzerLogs
        """

        # Construct dict forms of any model objects needed in order to build this model.

        code_risk_analyzer_logs_summary_model = {}  # CodeRiskAnalyzerLogsSummary
        code_risk_analyzer_logs_summary_model['total'] = 'testString'
        code_risk_analyzer_logs_summary_model['passed'] = 'testString'
        code_risk_analyzer_logs_summary_model['failed'] = 'testString'
        code_risk_analyzer_logs_summary_model['skipped'] = 'testString'

        # Construct a json representation of a ProjectConfigMetadataCodeRiskAnalyzerLogs model
        project_config_metadata_code_risk_analyzer_logs_model_json = {}
        project_config_metadata_code_risk_analyzer_logs_model_json['cra_version'] = 'testString'
        project_config_metadata_code_risk_analyzer_logs_model_json['schema_version'] = 'testString'
        project_config_metadata_code_risk_analyzer_logs_model_json['status'] = 'passed'
        project_config_metadata_code_risk_analyzer_logs_model_json['summary'] = code_risk_analyzer_logs_summary_model
        project_config_metadata_code_risk_analyzer_logs_model_json['timestamp'] = '2019-01-01T12:00:00Z'

        # Construct a model instance of ProjectConfigMetadataCodeRiskAnalyzerLogs by calling from_dict on the json representation
        project_config_metadata_code_risk_analyzer_logs_model = ProjectConfigMetadataCodeRiskAnalyzerLogs.from_dict(project_config_metadata_code_risk_analyzer_logs_model_json)
        assert project_config_metadata_code_risk_analyzer_logs_model != False

        # Construct a model instance of ProjectConfigMetadataCodeRiskAnalyzerLogs by calling from_dict on the json representation
        project_config_metadata_code_risk_analyzer_logs_model_dict = ProjectConfigMetadataCodeRiskAnalyzerLogs.from_dict(project_config_metadata_code_risk_analyzer_logs_model_json).__dict__
        project_config_metadata_code_risk_analyzer_logs_model2 = ProjectConfigMetadataCodeRiskAnalyzerLogs(**project_config_metadata_code_risk_analyzer_logs_model_dict)

        # Verify the model instances are equivalent
        assert project_config_metadata_code_risk_analyzer_logs_model == project_config_metadata_code_risk_analyzer_logs_model2

        # Convert model instance back to dict and verify no loss of data
        project_config_metadata_code_risk_analyzer_logs_model_json2 = project_config_metadata_code_risk_analyzer_logs_model.to_dict()
        assert project_config_metadata_code_risk_analyzer_logs_model_json2 == project_config_metadata_code_risk_analyzer_logs_model_json


class TestModel_ProjectConfigMetadataCostEstimate:
    """
    Test Class for ProjectConfigMetadataCostEstimate
    """

    def test_project_config_metadata_cost_estimate_serialization(self):
        """
        Test serialization/deserialization for ProjectConfigMetadataCostEstimate
        """

        # Construct a json representation of a ProjectConfigMetadataCostEstimate model
        project_config_metadata_cost_estimate_model_json = {}
        project_config_metadata_cost_estimate_model_json['version'] = 'testString'
        project_config_metadata_cost_estimate_model_json['currency'] = 'USD'
        project_config_metadata_cost_estimate_model_json['totalHourlyCost'] = 'testString'
        project_config_metadata_cost_estimate_model_json['totalMonthlyCost'] = 'testString'
        project_config_metadata_cost_estimate_model_json['pastTotalHourlyCost'] = 'testString'
        project_config_metadata_cost_estimate_model_json['pastTotalMonthlyCost'] = 'testString'
        project_config_metadata_cost_estimate_model_json['diffTotalHourlyCost'] = 'testString'
        project_config_metadata_cost_estimate_model_json['diffTotalMonthlyCost'] = 'testString'
        project_config_metadata_cost_estimate_model_json['timeGenerated'] = '2019-01-01T12:00:00Z'
        project_config_metadata_cost_estimate_model_json['user_id'] = 'testString'

        # Construct a model instance of ProjectConfigMetadataCostEstimate by calling from_dict on the json representation
        project_config_metadata_cost_estimate_model = ProjectConfigMetadataCostEstimate.from_dict(project_config_metadata_cost_estimate_model_json)
        assert project_config_metadata_cost_estimate_model != False

        # Construct a model instance of ProjectConfigMetadataCostEstimate by calling from_dict on the json representation
        project_config_metadata_cost_estimate_model_dict = ProjectConfigMetadataCostEstimate.from_dict(project_config_metadata_cost_estimate_model_json).__dict__
        project_config_metadata_cost_estimate_model2 = ProjectConfigMetadataCostEstimate(**project_config_metadata_cost_estimate_model_dict)

        # Verify the model instances are equivalent
        assert project_config_metadata_cost_estimate_model == project_config_metadata_cost_estimate_model2

        # Convert model instance back to dict and verify no loss of data
        project_config_metadata_cost_estimate_model_json2 = project_config_metadata_cost_estimate_model.to_dict()
        assert project_config_metadata_cost_estimate_model_json2 == project_config_metadata_cost_estimate_model_json


class TestModel_ProjectConfigMetadataLastApproved:
    """
    Test Class for ProjectConfigMetadataLastApproved
    """

    def test_project_config_metadata_last_approved_serialization(self):
        """
        Test serialization/deserialization for ProjectConfigMetadataLastApproved
        """

        # Construct a json representation of a ProjectConfigMetadataLastApproved model
        project_config_metadata_last_approved_model_json = {}
        project_config_metadata_last_approved_model_json['at'] = '2019-01-01T12:00:00Z'
        project_config_metadata_last_approved_model_json['comment'] = 'testString'
        project_config_metadata_last_approved_model_json['is_forced'] = True
        project_config_metadata_last_approved_model_json['user_id'] = 'testString'

        # Construct a model instance of ProjectConfigMetadataLastApproved by calling from_dict on the json representation
        project_config_metadata_last_approved_model = ProjectConfigMetadataLastApproved.from_dict(project_config_metadata_last_approved_model_json)
        assert project_config_metadata_last_approved_model != False

        # Construct a model instance of ProjectConfigMetadataLastApproved by calling from_dict on the json representation
        project_config_metadata_last_approved_model_dict = ProjectConfigMetadataLastApproved.from_dict(project_config_metadata_last_approved_model_json).__dict__
        project_config_metadata_last_approved_model2 = ProjectConfigMetadataLastApproved(**project_config_metadata_last_approved_model_dict)

        # Verify the model instances are equivalent
        assert project_config_metadata_last_approved_model == project_config_metadata_last_approved_model2

        # Convert model instance back to dict and verify no loss of data
        project_config_metadata_last_approved_model_json2 = project_config_metadata_last_approved_model.to_dict()
        assert project_config_metadata_last_approved_model_json2 == project_config_metadata_last_approved_model_json


class TestModel_ProjectConfigPatchDefinitionBlock:
    """
    Test Class for ProjectConfigPatchDefinitionBlock
    """

    def test_project_config_patch_definition_block_serialization(self):
        """
        Test serialization/deserialization for ProjectConfigPatchDefinitionBlock
        """

        # Construct dict forms of any model objects needed in order to build this model.

        project_config_auth_model = {}  # ProjectConfigAuth
        project_config_auth_model['trusted_profile_id'] = 'testString'
        project_config_auth_model['method'] = 'api_key'
        project_config_auth_model['api_key'] = 'testString'

        project_compliance_profile_model = {}  # ProjectComplianceProfile
        project_compliance_profile_model['id'] = 'testString'
        project_compliance_profile_model['instance_id'] = 'testString'
        project_compliance_profile_model['instance_location'] = 'testString'
        project_compliance_profile_model['attachment_id'] = 'testString'
        project_compliance_profile_model['profile_name'] = 'testString'

        input_variable_model = {}  # InputVariable
        input_variable_model['foo'] = 'testString'

        project_config_setting_model = {}  # ProjectConfigSetting
        project_config_setting_model['foo'] = 'testString'

        # Construct a json representation of a ProjectConfigPatchDefinitionBlock model
        project_config_patch_definition_block_model_json = {}
        project_config_patch_definition_block_model_json['name'] = 'testString'
        project_config_patch_definition_block_model_json['description'] = 'testString'
        project_config_patch_definition_block_model_json['environment'] = 'testString'
        project_config_patch_definition_block_model_json['authorizations'] = project_config_auth_model
        project_config_patch_definition_block_model_json['compliance_profile'] = project_compliance_profile_model
        project_config_patch_definition_block_model_json['locator_id'] = 'testString'
        project_config_patch_definition_block_model_json['inputs'] = input_variable_model
        project_config_patch_definition_block_model_json['settings'] = project_config_setting_model

        # Construct a model instance of ProjectConfigPatchDefinitionBlock by calling from_dict on the json representation
        project_config_patch_definition_block_model = ProjectConfigPatchDefinitionBlock.from_dict(project_config_patch_definition_block_model_json)
        assert project_config_patch_definition_block_model != False

        # Construct a model instance of ProjectConfigPatchDefinitionBlock by calling from_dict on the json representation
        project_config_patch_definition_block_model_dict = ProjectConfigPatchDefinitionBlock.from_dict(project_config_patch_definition_block_model_json).__dict__
        project_config_patch_definition_block_model2 = ProjectConfigPatchDefinitionBlock(**project_config_patch_definition_block_model_dict)

        # Verify the model instances are equivalent
        assert project_config_patch_definition_block_model == project_config_patch_definition_block_model2

        # Convert model instance back to dict and verify no loss of data
        project_config_patch_definition_block_model_json2 = project_config_patch_definition_block_model.to_dict()
        assert project_config_patch_definition_block_model_json2 == project_config_patch_definition_block_model_json


class TestModel_ProjectConfigPrototype:
    """
    Test Class for ProjectConfigPrototype
    """

    def test_project_config_prototype_serialization(self):
        """
        Test serialization/deserialization for ProjectConfigPrototype
        """

        # Construct dict forms of any model objects needed in order to build this model.

        project_config_auth_model = {}  # ProjectConfigAuth
        project_config_auth_model['trusted_profile_id'] = 'testString'
        project_config_auth_model['method'] = 'api_key'
        project_config_auth_model['api_key'] = 'testString'

        project_compliance_profile_model = {}  # ProjectComplianceProfile
        project_compliance_profile_model['id'] = 'testString'
        project_compliance_profile_model['instance_id'] = 'testString'
        project_compliance_profile_model['instance_location'] = 'testString'
        project_compliance_profile_model['attachment_id'] = 'testString'
        project_compliance_profile_model['profile_name'] = 'testString'

        input_variable_model = {}  # InputVariable
        input_variable_model['foo'] = 'testString'

        project_config_setting_model = {}  # ProjectConfigSetting
        project_config_setting_model['foo'] = 'testString'

        project_config_prototype_definition_block_model = {}  # ProjectConfigPrototypeDefinitionBlock
        project_config_prototype_definition_block_model['name'] = 'testString'
        project_config_prototype_definition_block_model['description'] = 'testString'
        project_config_prototype_definition_block_model['environment'] = 'testString'
        project_config_prototype_definition_block_model['authorizations'] = project_config_auth_model
        project_config_prototype_definition_block_model['compliance_profile'] = project_compliance_profile_model
        project_config_prototype_definition_block_model['locator_id'] = 'testString'
        project_config_prototype_definition_block_model['inputs'] = input_variable_model
        project_config_prototype_definition_block_model['settings'] = project_config_setting_model

        schematics_workspace_model = {}  # SchematicsWorkspace
        schematics_workspace_model['workspace_crn'] = 'testString'

        # Construct a json representation of a ProjectConfigPrototype model
        project_config_prototype_model_json = {}
        project_config_prototype_model_json['definition'] = project_config_prototype_definition_block_model
        project_config_prototype_model_json['schematics'] = schematics_workspace_model

        # Construct a model instance of ProjectConfigPrototype by calling from_dict on the json representation
        project_config_prototype_model = ProjectConfigPrototype.from_dict(project_config_prototype_model_json)
        assert project_config_prototype_model != False

        # Construct a model instance of ProjectConfigPrototype by calling from_dict on the json representation
        project_config_prototype_model_dict = ProjectConfigPrototype.from_dict(project_config_prototype_model_json).__dict__
        project_config_prototype_model2 = ProjectConfigPrototype(**project_config_prototype_model_dict)

        # Verify the model instances are equivalent
        assert project_config_prototype_model == project_config_prototype_model2

        # Convert model instance back to dict and verify no loss of data
        project_config_prototype_model_json2 = project_config_prototype_model.to_dict()
        assert project_config_prototype_model_json2 == project_config_prototype_model_json


class TestModel_ProjectConfigPrototypeDefinitionBlock:
    """
    Test Class for ProjectConfigPrototypeDefinitionBlock
    """

    def test_project_config_prototype_definition_block_serialization(self):
        """
        Test serialization/deserialization for ProjectConfigPrototypeDefinitionBlock
        """

        # Construct dict forms of any model objects needed in order to build this model.

        project_config_auth_model = {}  # ProjectConfigAuth
        project_config_auth_model['trusted_profile_id'] = 'testString'
        project_config_auth_model['method'] = 'api_key'
        project_config_auth_model['api_key'] = 'testString'

        project_compliance_profile_model = {}  # ProjectComplianceProfile
        project_compliance_profile_model['id'] = 'testString'
        project_compliance_profile_model['instance_id'] = 'testString'
        project_compliance_profile_model['instance_location'] = 'testString'
        project_compliance_profile_model['attachment_id'] = 'testString'
        project_compliance_profile_model['profile_name'] = 'testString'

        input_variable_model = {}  # InputVariable
        input_variable_model['foo'] = 'testString'

        project_config_setting_model = {}  # ProjectConfigSetting
        project_config_setting_model['foo'] = 'testString'

        # Construct a json representation of a ProjectConfigPrototypeDefinitionBlock model
        project_config_prototype_definition_block_model_json = {}
        project_config_prototype_definition_block_model_json['name'] = 'testString'
        project_config_prototype_definition_block_model_json['description'] = 'testString'
        project_config_prototype_definition_block_model_json['environment'] = 'testString'
        project_config_prototype_definition_block_model_json['authorizations'] = project_config_auth_model
        project_config_prototype_definition_block_model_json['compliance_profile'] = project_compliance_profile_model
        project_config_prototype_definition_block_model_json['locator_id'] = 'testString'
        project_config_prototype_definition_block_model_json['inputs'] = input_variable_model
        project_config_prototype_definition_block_model_json['settings'] = project_config_setting_model

        # Construct a model instance of ProjectConfigPrototypeDefinitionBlock by calling from_dict on the json representation
        project_config_prototype_definition_block_model = ProjectConfigPrototypeDefinitionBlock.from_dict(project_config_prototype_definition_block_model_json)
        assert project_config_prototype_definition_block_model != False

        # Construct a model instance of ProjectConfigPrototypeDefinitionBlock by calling from_dict on the json representation
        project_config_prototype_definition_block_model_dict = ProjectConfigPrototypeDefinitionBlock.from_dict(project_config_prototype_definition_block_model_json).__dict__
        project_config_prototype_definition_block_model2 = ProjectConfigPrototypeDefinitionBlock(**project_config_prototype_definition_block_model_dict)

        # Verify the model instances are equivalent
        assert project_config_prototype_definition_block_model == project_config_prototype_definition_block_model2

        # Convert model instance back to dict and verify no loss of data
        project_config_prototype_definition_block_model_json2 = project_config_prototype_definition_block_model.to_dict()
        assert project_config_prototype_definition_block_model_json2 == project_config_prototype_definition_block_model_json


class TestModel_ProjectConfigResource:
    """
    Test Class for ProjectConfigResource
    """

    def test_project_config_resource_serialization(self):
        """
        Test serialization/deserialization for ProjectConfigResource
        """

        # Construct a json representation of a ProjectConfigResource model
        project_config_resource_model_json = {}
        project_config_resource_model_json['resource_crn'] = 'crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::'
        project_config_resource_model_json['resource_name'] = 'testString'
        project_config_resource_model_json['resource_type'] = 'testString'
        project_config_resource_model_json['resource_tainted'] = True
        project_config_resource_model_json['resource_group_name'] = 'testString'

        # Construct a model instance of ProjectConfigResource by calling from_dict on the json representation
        project_config_resource_model = ProjectConfigResource.from_dict(project_config_resource_model_json)
        assert project_config_resource_model != False

        # Construct a model instance of ProjectConfigResource by calling from_dict on the json representation
        project_config_resource_model_dict = ProjectConfigResource.from_dict(project_config_resource_model_json).__dict__
        project_config_resource_model2 = ProjectConfigResource(**project_config_resource_model_dict)

        # Verify the model instances are equivalent
        assert project_config_resource_model == project_config_resource_model2

        # Convert model instance back to dict and verify no loss of data
        project_config_resource_model_json2 = project_config_resource_model.to_dict()
        assert project_config_resource_model_json2 == project_config_resource_model_json


class TestModel_ProjectConfigResourceCollection:
    """
    Test Class for ProjectConfigResourceCollection
    """

    def test_project_config_resource_collection_serialization(self):
        """
        Test serialization/deserialization for ProjectConfigResourceCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        project_config_resource_model = {}  # ProjectConfigResource
        project_config_resource_model['resource_crn'] = 'crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::'
        project_config_resource_model['resource_name'] = 'testString'
        project_config_resource_model['resource_type'] = 'testString'
        project_config_resource_model['resource_tainted'] = True
        project_config_resource_model['resource_group_name'] = 'testString'

        # Construct a json representation of a ProjectConfigResourceCollection model
        project_config_resource_collection_model_json = {}
        project_config_resource_collection_model_json['resources'] = [project_config_resource_model]
        project_config_resource_collection_model_json['resources_count'] = 38

        # Construct a model instance of ProjectConfigResourceCollection by calling from_dict on the json representation
        project_config_resource_collection_model = ProjectConfigResourceCollection.from_dict(project_config_resource_collection_model_json)
        assert project_config_resource_collection_model != False

        # Construct a model instance of ProjectConfigResourceCollection by calling from_dict on the json representation
        project_config_resource_collection_model_dict = ProjectConfigResourceCollection.from_dict(project_config_resource_collection_model_json).__dict__
        project_config_resource_collection_model2 = ProjectConfigResourceCollection(**project_config_resource_collection_model_dict)

        # Verify the model instances are equivalent
        assert project_config_resource_collection_model == project_config_resource_collection_model2

        # Convert model instance back to dict and verify no loss of data
        project_config_resource_collection_model_json2 = project_config_resource_collection_model.to_dict()
        assert project_config_resource_collection_model_json2 == project_config_resource_collection_model_json


class TestModel_ProjectConfigResponseDefinition:
    """
    Test Class for ProjectConfigResponseDefinition
    """

    def test_project_config_response_definition_serialization(self):
        """
        Test serialization/deserialization for ProjectConfigResponseDefinition
        """

        # Construct dict forms of any model objects needed in order to build this model.

        project_config_auth_model = {}  # ProjectConfigAuth
        project_config_auth_model['trusted_profile_id'] = 'testString'
        project_config_auth_model['method'] = 'api_key'
        project_config_auth_model['api_key'] = 'testString'

        project_compliance_profile_model = {}  # ProjectComplianceProfile
        project_compliance_profile_model['id'] = 'testString'
        project_compliance_profile_model['instance_id'] = 'testString'
        project_compliance_profile_model['instance_location'] = 'testString'
        project_compliance_profile_model['attachment_id'] = 'testString'
        project_compliance_profile_model['profile_name'] = 'testString'

        input_variable_model = {}  # InputVariable
        input_variable_model['foo'] = 'testString'

        project_config_setting_model = {}  # ProjectConfigSetting
        project_config_setting_model['foo'] = 'testString'

        # Construct a json representation of a ProjectConfigResponseDefinition model
        project_config_response_definition_model_json = {}
        project_config_response_definition_model_json['name'] = 'testString'
        project_config_response_definition_model_json['description'] = 'testString'
        project_config_response_definition_model_json['environment'] = 'testString'
        project_config_response_definition_model_json['authorizations'] = project_config_auth_model
        project_config_response_definition_model_json['compliance_profile'] = project_compliance_profile_model
        project_config_response_definition_model_json['locator_id'] = 'testString'
        project_config_response_definition_model_json['inputs'] = input_variable_model
        project_config_response_definition_model_json['settings'] = project_config_setting_model
        project_config_response_definition_model_json['type'] = 'terraform_template'

        # Construct a model instance of ProjectConfigResponseDefinition by calling from_dict on the json representation
        project_config_response_definition_model = ProjectConfigResponseDefinition.from_dict(project_config_response_definition_model_json)
        assert project_config_response_definition_model != False

        # Construct a model instance of ProjectConfigResponseDefinition by calling from_dict on the json representation
        project_config_response_definition_model_dict = ProjectConfigResponseDefinition.from_dict(project_config_response_definition_model_json).__dict__
        project_config_response_definition_model2 = ProjectConfigResponseDefinition(**project_config_response_definition_model_dict)

        # Verify the model instances are equivalent
        assert project_config_response_definition_model == project_config_response_definition_model2

        # Convert model instance back to dict and verify no loss of data
        project_config_response_definition_model_json2 = project_config_response_definition_model.to_dict()
        assert project_config_response_definition_model_json2 == project_config_response_definition_model_json


class TestModel_ProjectConfigSetting:
    """
    Test Class for ProjectConfigSetting
    """

    def test_project_config_setting_serialization(self):
        """
        Test serialization/deserialization for ProjectConfigSetting
        """

        # Construct a json representation of a ProjectConfigSetting model
        project_config_setting_model_json = {}
        project_config_setting_model_json['foo'] = 'testString'

        # Construct a model instance of ProjectConfigSetting by calling from_dict on the json representation
        project_config_setting_model = ProjectConfigSetting.from_dict(project_config_setting_model_json)
        assert project_config_setting_model != False

        # Construct a model instance of ProjectConfigSetting by calling from_dict on the json representation
        project_config_setting_model_dict = ProjectConfigSetting.from_dict(project_config_setting_model_json).__dict__
        project_config_setting_model2 = ProjectConfigSetting(**project_config_setting_model_dict)

        # Verify the model instances are equivalent
        assert project_config_setting_model == project_config_setting_model2

        # Convert model instance back to dict and verify no loss of data
        project_config_setting_model_json2 = project_config_setting_model.to_dict()
        assert project_config_setting_model_json2 == project_config_setting_model_json

        # Test get_properties and set_properties methods.
        project_config_setting_model.set_properties({})
        actual_dict = project_config_setting_model.get_properties()
        assert actual_dict == {}

        expected_dict = {'foo': 'testString'}
        project_config_setting_model.set_properties(expected_dict)
        actual_dict = project_config_setting_model.get_properties()
        assert actual_dict == expected_dict


class TestModel_ProjectConfigSummary:
    """
    Test Class for ProjectConfigSummary
    """

    def test_project_config_summary_serialization(self):
        """
        Test serialization/deserialization for ProjectConfigSummary
        """

        # Construct dict forms of any model objects needed in order to build this model.

        project_config_version_summary_model = {}  # ProjectConfigVersionSummary
        project_config_version_summary_model['state'] = 'approved'
        project_config_version_summary_model['version'] = 38
        project_config_version_summary_model['href'] = 'testString'

        project_config_definition_name_description_model = {}  # ProjectConfigDefinitionNameDescription
        project_config_definition_name_description_model['name'] = 'testString'
        project_config_definition_name_description_model['description'] = 'testString'

        project_definition_reference_model = {}  # ProjectDefinitionReference
        project_definition_reference_model['name'] = 'testString'

        project_reference_model = {}  # ProjectReference
        project_reference_model['id'] = 'testString'
        project_reference_model['definition'] = project_definition_reference_model
        project_reference_model['crn'] = 'crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::'
        project_reference_model['href'] = 'testString'

        # Construct a json representation of a ProjectConfigSummary model
        project_config_summary_model_json = {}
        project_config_summary_model_json['approved_version'] = project_config_version_summary_model
        project_config_summary_model_json['deployed_version'] = project_config_version_summary_model
        project_config_summary_model_json['id'] = 'testString'
        project_config_summary_model_json['version'] = 38
        project_config_summary_model_json['state'] = 'approved'
        project_config_summary_model_json['created_at'] = '2019-01-01T12:00:00Z'
        project_config_summary_model_json['modified_at'] = '2019-01-01T12:00:00Z'
        project_config_summary_model_json['href'] = 'testString'
        project_config_summary_model_json['definition'] = project_config_definition_name_description_model
        project_config_summary_model_json['project'] = project_reference_model

        # Construct a model instance of ProjectConfigSummary by calling from_dict on the json representation
        project_config_summary_model = ProjectConfigSummary.from_dict(project_config_summary_model_json)
        assert project_config_summary_model != False

        # Construct a model instance of ProjectConfigSummary by calling from_dict on the json representation
        project_config_summary_model_dict = ProjectConfigSummary.from_dict(project_config_summary_model_json).__dict__
        project_config_summary_model2 = ProjectConfigSummary(**project_config_summary_model_dict)

        # Verify the model instances are equivalent
        assert project_config_summary_model == project_config_summary_model2

        # Convert model instance back to dict and verify no loss of data
        project_config_summary_model_json2 = project_config_summary_model.to_dict()
        assert project_config_summary_model_json2 == project_config_summary_model_json


class TestModel_ProjectConfigVersion:
    """
    Test Class for ProjectConfigVersion
    """

    def test_project_config_version_serialization(self):
        """
        Test serialization/deserialization for ProjectConfigVersion
        """

        # Construct dict forms of any model objects needed in order to build this model.

        project_config_metadata_last_approved_model = {}  # ProjectConfigMetadataLastApproved
        project_config_metadata_last_approved_model['at'] = '2019-01-01T12:00:00Z'
        project_config_metadata_last_approved_model['comment'] = 'testString'
        project_config_metadata_last_approved_model['is_forced'] = True
        project_config_metadata_last_approved_model['user_id'] = 'testString'

        pre_post_action_job_with_id_and_summary_model = {}  # PrePostActionJobWithIdAndSummary
        pre_post_action_job_with_id_and_summary_model['id'] = 'testString'
        pre_post_action_job_with_id_and_summary_model['summary'] = {'anyKey': 'anyValue'}

        action_job_plan_summary_model = {}  # ActionJobPlanSummary
        action_job_plan_summary_model['add'] = 38
        action_job_plan_summary_model['failed'] = 38
        action_job_plan_summary_model['update'] = 38
        action_job_plan_summary_model['destroy'] = 38
        action_job_plan_summary_model['add_resources'] = ['testString']
        action_job_plan_summary_model['failed_resources'] = ['testString']
        action_job_plan_summary_model['updated_resources'] = ['testString']
        action_job_plan_summary_model['destroy_resources'] = ['testString']

        action_job_apply_summary_model = {}  # ActionJobApplySummary
        action_job_apply_summary_model['success'] = 38
        action_job_apply_summary_model['failed'] = 38
        action_job_apply_summary_model['success_resources'] = ['testString']
        action_job_apply_summary_model['failed_resources'] = ['testString']

        action_job_destroy_summary_resources_model = {}  # ActionJobDestroySummaryResources
        action_job_destroy_summary_resources_model['success'] = ['testString']
        action_job_destroy_summary_resources_model['failed'] = ['testString']
        action_job_destroy_summary_resources_model['tainted'] = ['testString']

        action_job_destroy_summary_model = {}  # ActionJobDestroySummary
        action_job_destroy_summary_model['success'] = 38
        action_job_destroy_summary_model['failed'] = 38
        action_job_destroy_summary_model['tainted'] = 38
        action_job_destroy_summary_model['resources'] = action_job_destroy_summary_resources_model

        action_job_message_summary_model = {}  # ActionJobMessageSummary
        action_job_message_summary_model['info'] = 38
        action_job_message_summary_model['debug'] = 38
        action_job_message_summary_model['error'] = 38

        terraform_log_analyzer_error_message_model = {}  # TerraformLogAnalyzerErrorMessage
        terraform_log_analyzer_error_message_model['foo'] = 'testString'

        action_job_plan_messages_summary_model = {}  # ActionJobPlanMessagesSummary
        action_job_plan_messages_summary_model['error_messages'] = [terraform_log_analyzer_error_message_model]
        action_job_plan_messages_summary_model['sucess_message'] = ['testString']
        action_job_plan_messages_summary_model['update_message'] = ['testString']
        action_job_plan_messages_summary_model['destroy_message'] = ['testString']

        terraform_log_analyzer_success_message_model = {}  # TerraformLogAnalyzerSuccessMessage
        terraform_log_analyzer_success_message_model['resource_type'] = 'testString'
        terraform_log_analyzer_success_message_model['time-taken'] = 'testString'
        terraform_log_analyzer_success_message_model['id'] = 'testString'

        action_job_apply_messages_summary_model = {}  # ActionJobApplyMessagesSummary
        action_job_apply_messages_summary_model['error_messages'] = [terraform_log_analyzer_error_message_model]
        action_job_apply_messages_summary_model['sucess_message'] = [terraform_log_analyzer_success_message_model]

        action_job_destroy_messages_summary_model = {}  # ActionJobDestroyMessagesSummary
        action_job_destroy_messages_summary_model['error_messages'] = [terraform_log_analyzer_error_message_model]

        action_job_summary_model = {}  # ActionJobSummary
        action_job_summary_model['plan_summary'] = action_job_plan_summary_model
        action_job_summary_model['apply_summary'] = action_job_apply_summary_model
        action_job_summary_model['destroy_summary'] = action_job_destroy_summary_model
        action_job_summary_model['message_summary'] = action_job_message_summary_model
        action_job_summary_model['plan_messages'] = action_job_plan_messages_summary_model
        action_job_summary_model['apply_messages'] = action_job_apply_messages_summary_model
        action_job_summary_model['destroy_messages'] = action_job_destroy_messages_summary_model

        action_job_with_id_and_summary_model = {}  # ActionJobWithIdAndSummary
        action_job_with_id_and_summary_model['id'] = 'testString'
        action_job_with_id_and_summary_model['summary'] = action_job_summary_model

        project_config_metadata_cost_estimate_model = {}  # ProjectConfigMetadataCostEstimate
        project_config_metadata_cost_estimate_model['version'] = 'testString'
        project_config_metadata_cost_estimate_model['currency'] = 'USD'
        project_config_metadata_cost_estimate_model['totalHourlyCost'] = 'testString'
        project_config_metadata_cost_estimate_model['totalMonthlyCost'] = 'testString'
        project_config_metadata_cost_estimate_model['pastTotalHourlyCost'] = 'testString'
        project_config_metadata_cost_estimate_model['pastTotalMonthlyCost'] = 'testString'
        project_config_metadata_cost_estimate_model['diffTotalHourlyCost'] = 'testString'
        project_config_metadata_cost_estimate_model['diffTotalMonthlyCost'] = 'testString'
        project_config_metadata_cost_estimate_model['timeGenerated'] = '2019-01-01T12:00:00Z'
        project_config_metadata_cost_estimate_model['user_id'] = 'testString'

        code_risk_analyzer_logs_summary_model = {}  # CodeRiskAnalyzerLogsSummary
        code_risk_analyzer_logs_summary_model['total'] = 'testString'
        code_risk_analyzer_logs_summary_model['passed'] = 'testString'
        code_risk_analyzer_logs_summary_model['failed'] = 'testString'
        code_risk_analyzer_logs_summary_model['skipped'] = 'testString'

        project_config_metadata_code_risk_analyzer_logs_model = {}  # ProjectConfigMetadataCodeRiskAnalyzerLogs
        project_config_metadata_code_risk_analyzer_logs_model['cra_version'] = 'testString'
        project_config_metadata_code_risk_analyzer_logs_model['schema_version'] = 'testString'
        project_config_metadata_code_risk_analyzer_logs_model['status'] = 'passed'
        project_config_metadata_code_risk_analyzer_logs_model['summary'] = code_risk_analyzer_logs_summary_model
        project_config_metadata_code_risk_analyzer_logs_model['timestamp'] = '2019-01-01T12:00:00Z'

        last_validated_action_with_summary_model = {}  # LastValidatedActionWithSummary
        last_validated_action_with_summary_model['href'] = 'testString'
        last_validated_action_with_summary_model['result'] = 'failed'
        last_validated_action_with_summary_model['pre_job'] = pre_post_action_job_with_id_and_summary_model
        last_validated_action_with_summary_model['post_job'] = pre_post_action_job_with_id_and_summary_model
        last_validated_action_with_summary_model['job'] = action_job_with_id_and_summary_model
        last_validated_action_with_summary_model['cost_estimate'] = project_config_metadata_cost_estimate_model
        last_validated_action_with_summary_model['cra_logs'] = project_config_metadata_code_risk_analyzer_logs_model

        last_action_with_summary_model = {}  # LastActionWithSummary
        last_action_with_summary_model['href'] = 'testString'
        last_action_with_summary_model['result'] = 'failed'
        last_action_with_summary_model['pre_job'] = pre_post_action_job_with_id_and_summary_model
        last_action_with_summary_model['post_job'] = pre_post_action_job_with_id_and_summary_model
        last_action_with_summary_model['job'] = action_job_with_id_and_summary_model

        output_value_model = {}  # OutputValue
        output_value_model['name'] = 'testString'
        output_value_model['description'] = 'testString'
        output_value_model['value'] = 'testString'

        project_definition_reference_model = {}  # ProjectDefinitionReference
        project_definition_reference_model['name'] = 'testString'

        project_reference_model = {}  # ProjectReference
        project_reference_model['id'] = 'testString'
        project_reference_model['definition'] = project_definition_reference_model
        project_reference_model['crn'] = 'crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::'
        project_reference_model['href'] = 'testString'

        schematics_workspace_model = {}  # SchematicsWorkspace
        schematics_workspace_model['workspace_crn'] = 'testString'

        project_config_auth_model = {}  # ProjectConfigAuth
        project_config_auth_model['trusted_profile_id'] = 'testString'
        project_config_auth_model['method'] = 'api_key'
        project_config_auth_model['api_key'] = 'testString'

        project_compliance_profile_model = {}  # ProjectComplianceProfile
        project_compliance_profile_model['id'] = 'testString'
        project_compliance_profile_model['instance_id'] = 'testString'
        project_compliance_profile_model['instance_location'] = 'testString'
        project_compliance_profile_model['attachment_id'] = 'testString'
        project_compliance_profile_model['profile_name'] = 'testString'

        input_variable_model = {}  # InputVariable
        input_variable_model['foo'] = 'testString'

        project_config_setting_model = {}  # ProjectConfigSetting
        project_config_setting_model['foo'] = 'testString'

        project_config_response_definition_model = {}  # ProjectConfigResponseDefinition
        project_config_response_definition_model['name'] = 'testString'
        project_config_response_definition_model['description'] = 'testString'
        project_config_response_definition_model['environment'] = 'testString'
        project_config_response_definition_model['authorizations'] = project_config_auth_model
        project_config_response_definition_model['compliance_profile'] = project_compliance_profile_model
        project_config_response_definition_model['locator_id'] = 'testString'
        project_config_response_definition_model['inputs'] = input_variable_model
        project_config_response_definition_model['settings'] = project_config_setting_model
        project_config_response_definition_model['type'] = 'terraform_template'

        # Construct a json representation of a ProjectConfigVersion model
        project_config_version_model_json = {}
        project_config_version_model_json['id'] = 'testString'
        project_config_version_model_json['version'] = 38
        project_config_version_model_json['is_draft'] = True
        project_config_version_model_json['needs_attention_state'] = []
        project_config_version_model_json['created_at'] = '2019-01-01T12:00:00Z'
        project_config_version_model_json['modified_at'] = '2019-01-01T12:00:00Z'
        project_config_version_model_json['last_approved'] = project_config_metadata_last_approved_model
        project_config_version_model_json['last_saved_at'] = '2019-01-01T12:00:00Z'
        project_config_version_model_json['last_validated'] = last_validated_action_with_summary_model
        project_config_version_model_json['last_deployed'] = last_action_with_summary_model
        project_config_version_model_json['last_undeployed'] = last_action_with_summary_model
        project_config_version_model_json['outputs'] = [output_value_model]
        project_config_version_model_json['project'] = project_reference_model
        project_config_version_model_json['references'] = {'anyKey': 'anyValue'}
        project_config_version_model_json['schematics'] = schematics_workspace_model
        project_config_version_model_json['state'] = 'approved'
        project_config_version_model_json['update_available'] = True
        project_config_version_model_json['definition'] = project_config_response_definition_model

        # Construct a model instance of ProjectConfigVersion by calling from_dict on the json representation
        project_config_version_model = ProjectConfigVersion.from_dict(project_config_version_model_json)
        assert project_config_version_model != False

        # Construct a model instance of ProjectConfigVersion by calling from_dict on the json representation
        project_config_version_model_dict = ProjectConfigVersion.from_dict(project_config_version_model_json).__dict__
        project_config_version_model2 = ProjectConfigVersion(**project_config_version_model_dict)

        # Verify the model instances are equivalent
        assert project_config_version_model == project_config_version_model2

        # Convert model instance back to dict and verify no loss of data
        project_config_version_model_json2 = project_config_version_model.to_dict()
        assert project_config_version_model_json2 == project_config_version_model_json


class TestModel_ProjectConfigVersionSummary:
    """
    Test Class for ProjectConfigVersionSummary
    """

    def test_project_config_version_summary_serialization(self):
        """
        Test serialization/deserialization for ProjectConfigVersionSummary
        """

        # Construct a json representation of a ProjectConfigVersionSummary model
        project_config_version_summary_model_json = {}
        project_config_version_summary_model_json['state'] = 'approved'
        project_config_version_summary_model_json['version'] = 38
        project_config_version_summary_model_json['href'] = 'testString'

        # Construct a model instance of ProjectConfigVersionSummary by calling from_dict on the json representation
        project_config_version_summary_model = ProjectConfigVersionSummary.from_dict(project_config_version_summary_model_json)
        assert project_config_version_summary_model != False

        # Construct a model instance of ProjectConfigVersionSummary by calling from_dict on the json representation
        project_config_version_summary_model_dict = ProjectConfigVersionSummary.from_dict(project_config_version_summary_model_json).__dict__
        project_config_version_summary_model2 = ProjectConfigVersionSummary(**project_config_version_summary_model_dict)

        # Verify the model instances are equivalent
        assert project_config_version_summary_model == project_config_version_summary_model2

        # Convert model instance back to dict and verify no loss of data
        project_config_version_summary_model_json2 = project_config_version_summary_model.to_dict()
        assert project_config_version_summary_model_json2 == project_config_version_summary_model_json


class TestModel_ProjectConfigVersionSummaryCollection:
    """
    Test Class for ProjectConfigVersionSummaryCollection
    """

    def test_project_config_version_summary_collection_serialization(self):
        """
        Test serialization/deserialization for ProjectConfigVersionSummaryCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        project_config_version_summary_model = {}  # ProjectConfigVersionSummary
        project_config_version_summary_model['state'] = 'approved'
        project_config_version_summary_model['version'] = 38
        project_config_version_summary_model['href'] = 'testString'

        # Construct a json representation of a ProjectConfigVersionSummaryCollection model
        project_config_version_summary_collection_model_json = {}
        project_config_version_summary_collection_model_json['versions'] = [project_config_version_summary_model]

        # Construct a model instance of ProjectConfigVersionSummaryCollection by calling from_dict on the json representation
        project_config_version_summary_collection_model = ProjectConfigVersionSummaryCollection.from_dict(project_config_version_summary_collection_model_json)
        assert project_config_version_summary_collection_model != False

        # Construct a model instance of ProjectConfigVersionSummaryCollection by calling from_dict on the json representation
        project_config_version_summary_collection_model_dict = ProjectConfigVersionSummaryCollection.from_dict(project_config_version_summary_collection_model_json).__dict__
        project_config_version_summary_collection_model2 = ProjectConfigVersionSummaryCollection(**project_config_version_summary_collection_model_dict)

        # Verify the model instances are equivalent
        assert project_config_version_summary_collection_model == project_config_version_summary_collection_model2

        # Convert model instance back to dict and verify no loss of data
        project_config_version_summary_collection_model_json2 = project_config_version_summary_collection_model.to_dict()
        assert project_config_version_summary_collection_model_json2 == project_config_version_summary_collection_model_json


class TestModel_ProjectDefinitionProperties:
    """
    Test Class for ProjectDefinitionProperties
    """

    def test_project_definition_properties_serialization(self):
        """
        Test serialization/deserialization for ProjectDefinitionProperties
        """

        # Construct a json representation of a ProjectDefinitionProperties model
        project_definition_properties_model_json = {}
        project_definition_properties_model_json['name'] = 'testString'
        project_definition_properties_model_json['description'] = 'testString'
        project_definition_properties_model_json['destroy_on_delete'] = True

        # Construct a model instance of ProjectDefinitionProperties by calling from_dict on the json representation
        project_definition_properties_model = ProjectDefinitionProperties.from_dict(project_definition_properties_model_json)
        assert project_definition_properties_model != False

        # Construct a model instance of ProjectDefinitionProperties by calling from_dict on the json representation
        project_definition_properties_model_dict = ProjectDefinitionProperties.from_dict(project_definition_properties_model_json).__dict__
        project_definition_properties_model2 = ProjectDefinitionProperties(**project_definition_properties_model_dict)

        # Verify the model instances are equivalent
        assert project_definition_properties_model == project_definition_properties_model2

        # Convert model instance back to dict and verify no loss of data
        project_definition_properties_model_json2 = project_definition_properties_model.to_dict()
        assert project_definition_properties_model_json2 == project_definition_properties_model_json


class TestModel_ProjectDefinitionReference:
    """
    Test Class for ProjectDefinitionReference
    """

    def test_project_definition_reference_serialization(self):
        """
        Test serialization/deserialization for ProjectDefinitionReference
        """

        # Construct a json representation of a ProjectDefinitionReference model
        project_definition_reference_model_json = {}
        project_definition_reference_model_json['name'] = 'testString'

        # Construct a model instance of ProjectDefinitionReference by calling from_dict on the json representation
        project_definition_reference_model = ProjectDefinitionReference.from_dict(project_definition_reference_model_json)
        assert project_definition_reference_model != False

        # Construct a model instance of ProjectDefinitionReference by calling from_dict on the json representation
        project_definition_reference_model_dict = ProjectDefinitionReference.from_dict(project_definition_reference_model_json).__dict__
        project_definition_reference_model2 = ProjectDefinitionReference(**project_definition_reference_model_dict)

        # Verify the model instances are equivalent
        assert project_definition_reference_model == project_definition_reference_model2

        # Convert model instance back to dict and verify no loss of data
        project_definition_reference_model_json2 = project_definition_reference_model.to_dict()
        assert project_definition_reference_model_json2 == project_definition_reference_model_json


class TestModel_ProjectEnvironmentSummary:
    """
    Test Class for ProjectEnvironmentSummary
    """

    def test_project_environment_summary_serialization(self):
        """
        Test serialization/deserialization for ProjectEnvironmentSummary
        """

        # Construct dict forms of any model objects needed in order to build this model.

        project_definition_reference_model = {}  # ProjectDefinitionReference
        project_definition_reference_model['name'] = 'testString'

        project_reference_model = {}  # ProjectReference
        project_reference_model['id'] = 'testString'
        project_reference_model['definition'] = project_definition_reference_model
        project_reference_model['crn'] = 'crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::'
        project_reference_model['href'] = 'testString'

        environment_definition_name_description_model = {}  # EnvironmentDefinitionNameDescription
        environment_definition_name_description_model['name'] = 'testString'
        environment_definition_name_description_model['description'] = 'testString'

        # Construct a json representation of a ProjectEnvironmentSummary model
        project_environment_summary_model_json = {}
        project_environment_summary_model_json['id'] = 'testString'
        project_environment_summary_model_json['project'] = project_reference_model
        project_environment_summary_model_json['created_at'] = '2019-01-01T12:00:00Z'
        project_environment_summary_model_json['href'] = 'testString'
        project_environment_summary_model_json['definition'] = environment_definition_name_description_model

        # Construct a model instance of ProjectEnvironmentSummary by calling from_dict on the json representation
        project_environment_summary_model = ProjectEnvironmentSummary.from_dict(project_environment_summary_model_json)
        assert project_environment_summary_model != False

        # Construct a model instance of ProjectEnvironmentSummary by calling from_dict on the json representation
        project_environment_summary_model_dict = ProjectEnvironmentSummary.from_dict(project_environment_summary_model_json).__dict__
        project_environment_summary_model2 = ProjectEnvironmentSummary(**project_environment_summary_model_dict)

        # Verify the model instances are equivalent
        assert project_environment_summary_model == project_environment_summary_model2

        # Convert model instance back to dict and verify no loss of data
        project_environment_summary_model_json2 = project_environment_summary_model.to_dict()
        assert project_environment_summary_model_json2 == project_environment_summary_model_json


class TestModel_ProjectPatchDefinitionBlock:
    """
    Test Class for ProjectPatchDefinitionBlock
    """

    def test_project_patch_definition_block_serialization(self):
        """
        Test serialization/deserialization for ProjectPatchDefinitionBlock
        """

        # Construct a json representation of a ProjectPatchDefinitionBlock model
        project_patch_definition_block_model_json = {}
        project_patch_definition_block_model_json['name'] = 'testString'
        project_patch_definition_block_model_json['description'] = 'testString'
        project_patch_definition_block_model_json['destroy_on_delete'] = True

        # Construct a model instance of ProjectPatchDefinitionBlock by calling from_dict on the json representation
        project_patch_definition_block_model = ProjectPatchDefinitionBlock.from_dict(project_patch_definition_block_model_json)
        assert project_patch_definition_block_model != False

        # Construct a model instance of ProjectPatchDefinitionBlock by calling from_dict on the json representation
        project_patch_definition_block_model_dict = ProjectPatchDefinitionBlock.from_dict(project_patch_definition_block_model_json).__dict__
        project_patch_definition_block_model2 = ProjectPatchDefinitionBlock(**project_patch_definition_block_model_dict)

        # Verify the model instances are equivalent
        assert project_patch_definition_block_model == project_patch_definition_block_model2

        # Convert model instance back to dict and verify no loss of data
        project_patch_definition_block_model_json2 = project_patch_definition_block_model.to_dict()
        assert project_patch_definition_block_model_json2 == project_patch_definition_block_model_json


class TestModel_ProjectPrototypeDefinition:
    """
    Test Class for ProjectPrototypeDefinition
    """

    def test_project_prototype_definition_serialization(self):
        """
        Test serialization/deserialization for ProjectPrototypeDefinition
        """

        # Construct a json representation of a ProjectPrototypeDefinition model
        project_prototype_definition_model_json = {}
        project_prototype_definition_model_json['name'] = 'testString'
        project_prototype_definition_model_json['description'] = 'testString'
        project_prototype_definition_model_json['destroy_on_delete'] = True

        # Construct a model instance of ProjectPrototypeDefinition by calling from_dict on the json representation
        project_prototype_definition_model = ProjectPrototypeDefinition.from_dict(project_prototype_definition_model_json)
        assert project_prototype_definition_model != False

        # Construct a model instance of ProjectPrototypeDefinition by calling from_dict on the json representation
        project_prototype_definition_model_dict = ProjectPrototypeDefinition.from_dict(project_prototype_definition_model_json).__dict__
        project_prototype_definition_model2 = ProjectPrototypeDefinition(**project_prototype_definition_model_dict)

        # Verify the model instances are equivalent
        assert project_prototype_definition_model == project_prototype_definition_model2

        # Convert model instance back to dict and verify no loss of data
        project_prototype_definition_model_json2 = project_prototype_definition_model.to_dict()
        assert project_prototype_definition_model_json2 == project_prototype_definition_model_json


class TestModel_ProjectReference:
    """
    Test Class for ProjectReference
    """

    def test_project_reference_serialization(self):
        """
        Test serialization/deserialization for ProjectReference
        """

        # Construct dict forms of any model objects needed in order to build this model.

        project_definition_reference_model = {}  # ProjectDefinitionReference
        project_definition_reference_model['name'] = 'testString'

        # Construct a json representation of a ProjectReference model
        project_reference_model_json = {}
        project_reference_model_json['id'] = 'testString'
        project_reference_model_json['definition'] = project_definition_reference_model
        project_reference_model_json['crn'] = 'crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::'
        project_reference_model_json['href'] = 'testString'

        # Construct a model instance of ProjectReference by calling from_dict on the json representation
        project_reference_model = ProjectReference.from_dict(project_reference_model_json)
        assert project_reference_model != False

        # Construct a model instance of ProjectReference by calling from_dict on the json representation
        project_reference_model_dict = ProjectReference.from_dict(project_reference_model_json).__dict__
        project_reference_model2 = ProjectReference(**project_reference_model_dict)

        # Verify the model instances are equivalent
        assert project_reference_model == project_reference_model2

        # Convert model instance back to dict and verify no loss of data
        project_reference_model_json2 = project_reference_model.to_dict()
        assert project_reference_model_json2 == project_reference_model_json


class TestModel_ProjectSummary:
    """
    Test Class for ProjectSummary
    """

    def test_project_summary_serialization(self):
        """
        Test serialization/deserialization for ProjectSummary
        """

        # Construct dict forms of any model objects needed in order to build this model.

        cumulative_needs_attention_model = {}  # CumulativeNeedsAttention
        cumulative_needs_attention_model['event'] = 'testString'
        cumulative_needs_attention_model['event_id'] = 'testString'
        cumulative_needs_attention_model['config_id'] = 'testString'
        cumulative_needs_attention_model['config_version'] = 38

        project_definition_properties_model = {}  # ProjectDefinitionProperties
        project_definition_properties_model['name'] = 'testString'
        project_definition_properties_model['description'] = 'testString'
        project_definition_properties_model['destroy_on_delete'] = True

        # Construct a json representation of a ProjectSummary model
        project_summary_model_json = {}
        project_summary_model_json['crn'] = 'crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::'
        project_summary_model_json['created_at'] = '2019-01-01T12:00:00Z'
        project_summary_model_json['cumulative_needs_attention_view'] = [cumulative_needs_attention_model]
        project_summary_model_json['cumulative_needs_attention_view_error'] = False
        project_summary_model_json['id'] = 'testString'
        project_summary_model_json['location'] = 'testString'
        project_summary_model_json['resource_group_id'] = 'testString'
        project_summary_model_json['state'] = 'ready'
        project_summary_model_json['definition'] = project_definition_properties_model

        # Construct a model instance of ProjectSummary by calling from_dict on the json representation
        project_summary_model = ProjectSummary.from_dict(project_summary_model_json)
        assert project_summary_model != False

        # Construct a model instance of ProjectSummary by calling from_dict on the json representation
        project_summary_model_dict = ProjectSummary.from_dict(project_summary_model_json).__dict__
        project_summary_model2 = ProjectSummary(**project_summary_model_dict)

        # Verify the model instances are equivalent
        assert project_summary_model == project_summary_model2

        # Convert model instance back to dict and verify no loss of data
        project_summary_model_json2 = project_summary_model.to_dict()
        assert project_summary_model_json2 == project_summary_model_json


class TestModel_SchematicsWorkspace:
    """
    Test Class for SchematicsWorkspace
    """

    def test_schematics_workspace_serialization(self):
        """
        Test serialization/deserialization for SchematicsWorkspace
        """

        # Construct a json representation of a SchematicsWorkspace model
        schematics_workspace_model_json = {}
        schematics_workspace_model_json['workspace_crn'] = 'testString'

        # Construct a model instance of SchematicsWorkspace by calling from_dict on the json representation
        schematics_workspace_model = SchematicsWorkspace.from_dict(schematics_workspace_model_json)
        assert schematics_workspace_model != False

        # Construct a model instance of SchematicsWorkspace by calling from_dict on the json representation
        schematics_workspace_model_dict = SchematicsWorkspace.from_dict(schematics_workspace_model_json).__dict__
        schematics_workspace_model2 = SchematicsWorkspace(**schematics_workspace_model_dict)

        # Verify the model instances are equivalent
        assert schematics_workspace_model == schematics_workspace_model2

        # Convert model instance back to dict and verify no loss of data
        schematics_workspace_model_json2 = schematics_workspace_model.to_dict()
        assert schematics_workspace_model_json2 == schematics_workspace_model_json


class TestModel_TerraformLogAnalyzerErrorMessage:
    """
    Test Class for TerraformLogAnalyzerErrorMessage
    """

    def test_terraform_log_analyzer_error_message_serialization(self):
        """
        Test serialization/deserialization for TerraformLogAnalyzerErrorMessage
        """

        # Construct a json representation of a TerraformLogAnalyzerErrorMessage model
        terraform_log_analyzer_error_message_model_json = {}
        terraform_log_analyzer_error_message_model_json['foo'] = 'testString'

        # Construct a model instance of TerraformLogAnalyzerErrorMessage by calling from_dict on the json representation
        terraform_log_analyzer_error_message_model = TerraformLogAnalyzerErrorMessage.from_dict(terraform_log_analyzer_error_message_model_json)
        assert terraform_log_analyzer_error_message_model != False

        # Construct a model instance of TerraformLogAnalyzerErrorMessage by calling from_dict on the json representation
        terraform_log_analyzer_error_message_model_dict = TerraformLogAnalyzerErrorMessage.from_dict(terraform_log_analyzer_error_message_model_json).__dict__
        terraform_log_analyzer_error_message_model2 = TerraformLogAnalyzerErrorMessage(**terraform_log_analyzer_error_message_model_dict)

        # Verify the model instances are equivalent
        assert terraform_log_analyzer_error_message_model == terraform_log_analyzer_error_message_model2

        # Convert model instance back to dict and verify no loss of data
        terraform_log_analyzer_error_message_model_json2 = terraform_log_analyzer_error_message_model.to_dict()
        assert terraform_log_analyzer_error_message_model_json2 == terraform_log_analyzer_error_message_model_json

        # Test get_properties and set_properties methods.
        terraform_log_analyzer_error_message_model.set_properties({})
        actual_dict = terraform_log_analyzer_error_message_model.get_properties()
        assert actual_dict == {}

        expected_dict = {'foo': 'testString'}
        terraform_log_analyzer_error_message_model.set_properties(expected_dict)
        actual_dict = terraform_log_analyzer_error_message_model.get_properties()
        assert actual_dict == expected_dict


class TestModel_TerraformLogAnalyzerSuccessMessage:
    """
    Test Class for TerraformLogAnalyzerSuccessMessage
    """

    def test_terraform_log_analyzer_success_message_serialization(self):
        """
        Test serialization/deserialization for TerraformLogAnalyzerSuccessMessage
        """

        # Construct a json representation of a TerraformLogAnalyzerSuccessMessage model
        terraform_log_analyzer_success_message_model_json = {}
        terraform_log_analyzer_success_message_model_json['resource_type'] = 'testString'
        terraform_log_analyzer_success_message_model_json['time-taken'] = 'testString'
        terraform_log_analyzer_success_message_model_json['id'] = 'testString'

        # Construct a model instance of TerraformLogAnalyzerSuccessMessage by calling from_dict on the json representation
        terraform_log_analyzer_success_message_model = TerraformLogAnalyzerSuccessMessage.from_dict(terraform_log_analyzer_success_message_model_json)
        assert terraform_log_analyzer_success_message_model != False

        # Construct a model instance of TerraformLogAnalyzerSuccessMessage by calling from_dict on the json representation
        terraform_log_analyzer_success_message_model_dict = TerraformLogAnalyzerSuccessMessage.from_dict(terraform_log_analyzer_success_message_model_json).__dict__
        terraform_log_analyzer_success_message_model2 = TerraformLogAnalyzerSuccessMessage(**terraform_log_analyzer_success_message_model_dict)

        # Verify the model instances are equivalent
        assert terraform_log_analyzer_success_message_model == terraform_log_analyzer_success_message_model2

        # Convert model instance back to dict and verify no loss of data
        terraform_log_analyzer_success_message_model_json2 = terraform_log_analyzer_success_message_model.to_dict()
        assert terraform_log_analyzer_success_message_model_json2 == terraform_log_analyzer_success_message_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
