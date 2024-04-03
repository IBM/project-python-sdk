# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2024.
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
from ibm_project_sdk.project_v1 import *


_service = ProjectV1(authenticator=NoAuthAuthenticator())

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
    if not request_url.endswith('/'):
        return request_url
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
        mock_response = '{"crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::", "created_at": "2019-01-01T12:00:00.000Z", "cumulative_needs_attention_view": [{"event": "event", "event_id": "event_id", "config_id": "config_id", "config_version": 14}], "cumulative_needs_attention_view_error": false, "id": "id", "location": "location", "resource_group_id": "resource_group_id", "state": "ready", "href": "href", "resource_group": "resource_group", "event_notifications_crn": "event_notifications_crn", "configs": [{"approved_version": {"definition": {"environment_id": "environment_id", "locator_id": "locator_id"}, "state": "approved", "version": 7, "href": "href"}, "deployed_version": {"definition": {"environment_id": "environment_id", "locator_id": "locator_id"}, "state": "approved", "version": 7, "href": "href"}, "id": "id", "version": 7, "state": "approved", "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "href": "href", "definition": {"description": "description", "name": "name", "locator_id": "locator_id"}, "project": {"id": "id", "href": "href", "definition": {"name": "name"}, "crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::"}, "deployment_model": "project_deployed"}], "environments": [{"id": "id", "project": {"id": "id", "href": "href", "definition": {"name": "name"}, "crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::"}, "created_at": "2019-01-01T12:00:00.000Z", "href": "href", "definition": {"description": "description", "name": "name"}}], "definition": {"name": "name", "destroy_on_delete": false, "description": "description", "monitoring_enabled": false}}'
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
        project_prototype_definition_model['destroy_on_delete'] = True
        project_prototype_definition_model['description'] = 'A microservice to deploy on top of ACME infrastructure.'
        project_prototype_definition_model['monitoring_enabled'] = False

        # Construct a dict representation of a ProjectComplianceProfile model
        project_compliance_profile_model = {}
        project_compliance_profile_model['id'] = 'testString'
        project_compliance_profile_model['instance_id'] = 'testString'
        project_compliance_profile_model['instance_location'] = 'testString'
        project_compliance_profile_model['attachment_id'] = 'testString'
        project_compliance_profile_model['profile_name'] = 'testString'

        # Construct a dict representation of a ProjectConfigAuth model
        project_config_auth_model = {}
        project_config_auth_model['trusted_profile_id'] = 'testString'
        project_config_auth_model['method'] = 'api_key'
        project_config_auth_model['api_key'] = 'testString'

        # Construct a dict representation of a ProjectConfigDefinitionPrototypeDAConfigDefinitionPropertiesPrototype model
        project_config_definition_prototype_model = {}
        project_config_definition_prototype_model['compliance_profile'] = project_compliance_profile_model
        project_config_definition_prototype_model['locator_id'] = (
            '1082e7d2-5e2f-0a11-a3bc-f88a8e1931fc.018edf04-e772-4ca2-9785-03e8e03bef72-global'
        )
        project_config_definition_prototype_model['description'] = 'The stage account configuration.'
        project_config_definition_prototype_model['name'] = 'account-stage'
        project_config_definition_prototype_model['environment_id'] = 'testString'
        project_config_definition_prototype_model['authorizations'] = project_config_auth_model
        project_config_definition_prototype_model['inputs'] = {'anyKey': 'anyValue'}
        project_config_definition_prototype_model['settings'] = {'anyKey': 'anyValue'}

        # Construct a dict representation of a SchematicsWorkspace model
        schematics_workspace_model = {}
        schematics_workspace_model['workspace_crn'] = (
            'crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::'
        )

        # Construct a dict representation of a ProjectConfigPrototype model
        project_config_prototype_model = {}
        project_config_prototype_model['definition'] = project_config_definition_prototype_model
        project_config_prototype_model['schematics'] = schematics_workspace_model

        # Construct a dict representation of a EnvironmentDefinitionRequiredProperties model
        environment_definition_required_properties_model = {}
        environment_definition_required_properties_model['description'] = 'testString'
        environment_definition_required_properties_model['name'] = 'testString'
        environment_definition_required_properties_model['authorizations'] = project_config_auth_model
        environment_definition_required_properties_model['inputs'] = {'anyKey': 'anyValue'}
        environment_definition_required_properties_model['compliance_profile'] = project_compliance_profile_model

        # Construct a dict representation of a EnvironmentPrototype model
        environment_prototype_model = {}
        environment_prototype_model['definition'] = environment_definition_required_properties_model

        # Set up parameter values
        definition = project_prototype_definition_model
        location = 'us-south'
        resource_group = 'Default'
        configs = [project_config_prototype_model]
        environments = [environment_prototype_model]

        # Invoke method
        response = _service.create_project(
            definition,
            location,
            resource_group,
            configs=configs,
            environments=environments,
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
        assert req_body['environments'] == [environment_prototype_model]

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
        mock_response = '{"crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::", "created_at": "2019-01-01T12:00:00.000Z", "cumulative_needs_attention_view": [{"event": "event", "event_id": "event_id", "config_id": "config_id", "config_version": 14}], "cumulative_needs_attention_view_error": false, "id": "id", "location": "location", "resource_group_id": "resource_group_id", "state": "ready", "href": "href", "resource_group": "resource_group", "event_notifications_crn": "event_notifications_crn", "configs": [{"approved_version": {"definition": {"environment_id": "environment_id", "locator_id": "locator_id"}, "state": "approved", "version": 7, "href": "href"}, "deployed_version": {"definition": {"environment_id": "environment_id", "locator_id": "locator_id"}, "state": "approved", "version": 7, "href": "href"}, "id": "id", "version": 7, "state": "approved", "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "href": "href", "definition": {"description": "description", "name": "name", "locator_id": "locator_id"}, "project": {"id": "id", "href": "href", "definition": {"name": "name"}, "crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::"}, "deployment_model": "project_deployed"}], "environments": [{"id": "id", "project": {"id": "id", "href": "href", "definition": {"name": "name"}, "crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::"}, "created_at": "2019-01-01T12:00:00.000Z", "href": "href", "definition": {"description": "description", "name": "name"}}], "definition": {"name": "name", "destroy_on_delete": false, "description": "description", "monitoring_enabled": false}}'
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
        project_prototype_definition_model['destroy_on_delete'] = True
        project_prototype_definition_model['description'] = 'A microservice to deploy on top of ACME infrastructure.'
        project_prototype_definition_model['monitoring_enabled'] = False

        # Construct a dict representation of a ProjectComplianceProfile model
        project_compliance_profile_model = {}
        project_compliance_profile_model['id'] = 'testString'
        project_compliance_profile_model['instance_id'] = 'testString'
        project_compliance_profile_model['instance_location'] = 'testString'
        project_compliance_profile_model['attachment_id'] = 'testString'
        project_compliance_profile_model['profile_name'] = 'testString'

        # Construct a dict representation of a ProjectConfigAuth model
        project_config_auth_model = {}
        project_config_auth_model['trusted_profile_id'] = 'testString'
        project_config_auth_model['method'] = 'api_key'
        project_config_auth_model['api_key'] = 'testString'

        # Construct a dict representation of a ProjectConfigDefinitionPrototypeDAConfigDefinitionPropertiesPrototype model
        project_config_definition_prototype_model = {}
        project_config_definition_prototype_model['compliance_profile'] = project_compliance_profile_model
        project_config_definition_prototype_model['locator_id'] = (
            '1082e7d2-5e2f-0a11-a3bc-f88a8e1931fc.018edf04-e772-4ca2-9785-03e8e03bef72-global'
        )
        project_config_definition_prototype_model['description'] = 'The stage account configuration.'
        project_config_definition_prototype_model['name'] = 'account-stage'
        project_config_definition_prototype_model['environment_id'] = 'testString'
        project_config_definition_prototype_model['authorizations'] = project_config_auth_model
        project_config_definition_prototype_model['inputs'] = {'anyKey': 'anyValue'}
        project_config_definition_prototype_model['settings'] = {'anyKey': 'anyValue'}

        # Construct a dict representation of a SchematicsWorkspace model
        schematics_workspace_model = {}
        schematics_workspace_model['workspace_crn'] = (
            'crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::'
        )

        # Construct a dict representation of a ProjectConfigPrototype model
        project_config_prototype_model = {}
        project_config_prototype_model['definition'] = project_config_definition_prototype_model
        project_config_prototype_model['schematics'] = schematics_workspace_model

        # Construct a dict representation of a EnvironmentDefinitionRequiredProperties model
        environment_definition_required_properties_model = {}
        environment_definition_required_properties_model['description'] = 'testString'
        environment_definition_required_properties_model['name'] = 'testString'
        environment_definition_required_properties_model['authorizations'] = project_config_auth_model
        environment_definition_required_properties_model['inputs'] = {'anyKey': 'anyValue'}
        environment_definition_required_properties_model['compliance_profile'] = project_compliance_profile_model

        # Construct a dict representation of a EnvironmentPrototype model
        environment_prototype_model = {}
        environment_prototype_model['definition'] = environment_definition_required_properties_model

        # Set up parameter values
        definition = project_prototype_definition_model
        location = 'us-south'
        resource_group = 'Default'
        configs = [project_config_prototype_model]
        environments = [environment_prototype_model]

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
        mock_response = '{"limit": 10, "first": {"href": "href"}, "next": {"href": "href"}, "projects": [{"crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::", "created_at": "2019-01-01T12:00:00.000Z", "cumulative_needs_attention_view": [{"event": "event", "event_id": "event_id", "config_id": "config_id", "config_version": 14}], "cumulative_needs_attention_view_error": false, "id": "id", "location": "location", "resource_group_id": "resource_group_id", "state": "ready", "href": "href", "definition": {"name": "name", "destroy_on_delete": false, "description": "description", "monitoring_enabled": false}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        token = 'testString'
        limit = 10

        # Invoke method
        response = _service.list_projects(
            token=token,
            limit=limit,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'token={}'.format(token) in query_string
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
        mock_response = '{"limit": 10, "first": {"href": "href"}, "next": {"href": "href"}, "projects": [{"crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::", "created_at": "2019-01-01T12:00:00.000Z", "cumulative_needs_attention_view": [{"event": "event", "event_id": "event_id", "config_id": "config_id", "config_version": 14}], "cumulative_needs_attention_view_error": false, "id": "id", "location": "location", "resource_group_id": "resource_group_id", "state": "ready", "href": "href", "definition": {"name": "name", "destroy_on_delete": false, "description": "description", "monitoring_enabled": false}}]}'
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
        mock_response1 = '{"next":{"href":"https://myhost.com/somePath?token=1"},"projects":[{"crn":"crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::","created_at":"2019-01-01T12:00:00.000Z","cumulative_needs_attention_view":[{"event":"event","event_id":"event_id","config_id":"config_id","config_version":14}],"cumulative_needs_attention_view_error":false,"id":"id","location":"location","resource_group_id":"resource_group_id","state":"ready","href":"href","definition":{"name":"name","destroy_on_delete":false,"description":"description","monitoring_enabled":false}}],"total_count":2,"limit":1}'
        mock_response2 = '{"projects":[{"crn":"crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::","created_at":"2019-01-01T12:00:00.000Z","cumulative_needs_attention_view":[{"event":"event","event_id":"event_id","config_id":"config_id","config_version":14}],"cumulative_needs_attention_view_error":false,"id":"id","location":"location","resource_group_id":"resource_group_id","state":"ready","href":"href","definition":{"name":"name","destroy_on_delete":false,"description":"description","monitoring_enabled":false}}],"total_count":2,"limit":1}'
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
        mock_response1 = '{"next":{"href":"https://myhost.com/somePath?token=1"},"projects":[{"crn":"crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::","created_at":"2019-01-01T12:00:00.000Z","cumulative_needs_attention_view":[{"event":"event","event_id":"event_id","config_id":"config_id","config_version":14}],"cumulative_needs_attention_view_error":false,"id":"id","location":"location","resource_group_id":"resource_group_id","state":"ready","href":"href","definition":{"name":"name","destroy_on_delete":false,"description":"description","monitoring_enabled":false}}],"total_count":2,"limit":1}'
        mock_response2 = '{"projects":[{"crn":"crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::","created_at":"2019-01-01T12:00:00.000Z","cumulative_needs_attention_view":[{"event":"event","event_id":"event_id","config_id":"config_id","config_version":14}],"cumulative_needs_attention_view_error":false,"id":"id","location":"location","resource_group_id":"resource_group_id","state":"ready","href":"href","definition":{"name":"name","destroy_on_delete":false,"description":"description","monitoring_enabled":false}}],"total_count":2,"limit":1}'
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
        mock_response = '{"crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::", "created_at": "2019-01-01T12:00:00.000Z", "cumulative_needs_attention_view": [{"event": "event", "event_id": "event_id", "config_id": "config_id", "config_version": 14}], "cumulative_needs_attention_view_error": false, "id": "id", "location": "location", "resource_group_id": "resource_group_id", "state": "ready", "href": "href", "resource_group": "resource_group", "event_notifications_crn": "event_notifications_crn", "configs": [{"approved_version": {"definition": {"environment_id": "environment_id", "locator_id": "locator_id"}, "state": "approved", "version": 7, "href": "href"}, "deployed_version": {"definition": {"environment_id": "environment_id", "locator_id": "locator_id"}, "state": "approved", "version": 7, "href": "href"}, "id": "id", "version": 7, "state": "approved", "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "href": "href", "definition": {"description": "description", "name": "name", "locator_id": "locator_id"}, "project": {"id": "id", "href": "href", "definition": {"name": "name"}, "crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::"}, "deployment_model": "project_deployed"}], "environments": [{"id": "id", "project": {"id": "id", "href": "href", "definition": {"name": "name"}, "crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::"}, "created_at": "2019-01-01T12:00:00.000Z", "href": "href", "definition": {"description": "description", "name": "name"}}], "definition": {"name": "name", "destroy_on_delete": false, "description": "description", "monitoring_enabled": false}}'
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
        mock_response = '{"crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::", "created_at": "2019-01-01T12:00:00.000Z", "cumulative_needs_attention_view": [{"event": "event", "event_id": "event_id", "config_id": "config_id", "config_version": 14}], "cumulative_needs_attention_view_error": false, "id": "id", "location": "location", "resource_group_id": "resource_group_id", "state": "ready", "href": "href", "resource_group": "resource_group", "event_notifications_crn": "event_notifications_crn", "configs": [{"approved_version": {"definition": {"environment_id": "environment_id", "locator_id": "locator_id"}, "state": "approved", "version": 7, "href": "href"}, "deployed_version": {"definition": {"environment_id": "environment_id", "locator_id": "locator_id"}, "state": "approved", "version": 7, "href": "href"}, "id": "id", "version": 7, "state": "approved", "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "href": "href", "definition": {"description": "description", "name": "name", "locator_id": "locator_id"}, "project": {"id": "id", "href": "href", "definition": {"name": "name"}, "crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::"}, "deployment_model": "project_deployed"}], "environments": [{"id": "id", "project": {"id": "id", "href": "href", "definition": {"name": "name"}, "crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::"}, "created_at": "2019-01-01T12:00:00.000Z", "href": "href", "definition": {"description": "description", "name": "name"}}], "definition": {"name": "name", "destroy_on_delete": false, "description": "description", "monitoring_enabled": false}}'
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
        mock_response = '{"crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::", "created_at": "2019-01-01T12:00:00.000Z", "cumulative_needs_attention_view": [{"event": "event", "event_id": "event_id", "config_id": "config_id", "config_version": 14}], "cumulative_needs_attention_view_error": false, "id": "id", "location": "location", "resource_group_id": "resource_group_id", "state": "ready", "href": "href", "resource_group": "resource_group", "event_notifications_crn": "event_notifications_crn", "configs": [{"approved_version": {"definition": {"environment_id": "environment_id", "locator_id": "locator_id"}, "state": "approved", "version": 7, "href": "href"}, "deployed_version": {"definition": {"environment_id": "environment_id", "locator_id": "locator_id"}, "state": "approved", "version": 7, "href": "href"}, "id": "id", "version": 7, "state": "approved", "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "href": "href", "definition": {"description": "description", "name": "name", "locator_id": "locator_id"}, "project": {"id": "id", "href": "href", "definition": {"name": "name"}, "crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::"}, "deployment_model": "project_deployed"}], "environments": [{"id": "id", "project": {"id": "id", "href": "href", "definition": {"name": "name"}, "crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::"}, "created_at": "2019-01-01T12:00:00.000Z", "href": "href", "definition": {"description": "description", "name": "name"}}], "definition": {"name": "name", "destroy_on_delete": false, "description": "description", "monitoring_enabled": false}}'
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
        project_patch_definition_block_model['destroy_on_delete'] = True
        project_patch_definition_block_model['description'] = 'A microservice to deploy on top of ACME infrastructure.'
        project_patch_definition_block_model['monitoring_enabled'] = True

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
        mock_response = '{"crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::", "created_at": "2019-01-01T12:00:00.000Z", "cumulative_needs_attention_view": [{"event": "event", "event_id": "event_id", "config_id": "config_id", "config_version": 14}], "cumulative_needs_attention_view_error": false, "id": "id", "location": "location", "resource_group_id": "resource_group_id", "state": "ready", "href": "href", "resource_group": "resource_group", "event_notifications_crn": "event_notifications_crn", "configs": [{"approved_version": {"definition": {"environment_id": "environment_id", "locator_id": "locator_id"}, "state": "approved", "version": 7, "href": "href"}, "deployed_version": {"definition": {"environment_id": "environment_id", "locator_id": "locator_id"}, "state": "approved", "version": 7, "href": "href"}, "id": "id", "version": 7, "state": "approved", "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "href": "href", "definition": {"description": "description", "name": "name", "locator_id": "locator_id"}, "project": {"id": "id", "href": "href", "definition": {"name": "name"}, "crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::"}, "deployment_model": "project_deployed"}], "environments": [{"id": "id", "project": {"id": "id", "href": "href", "definition": {"name": "name"}, "crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::"}, "created_at": "2019-01-01T12:00:00.000Z", "href": "href", "definition": {"description": "description", "name": "name"}}], "definition": {"name": "name", "destroy_on_delete": false, "description": "description", "monitoring_enabled": false}}'
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
        project_patch_definition_block_model['destroy_on_delete'] = True
        project_patch_definition_block_model['description'] = 'A microservice to deploy on top of ACME infrastructure.'
        project_patch_definition_block_model['monitoring_enabled'] = True

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
        mock_response = '{"id": "id"}'
        responses.add(
            responses.DELETE,
            url,
            body=mock_response,
            content_type='application/json',
            status=202,
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
        assert response.status_code == 202

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
        mock_response = '{"id": "id"}'
        responses.add(
            responses.DELETE,
            url,
            body=mock_response,
            content_type='application/json',
            status=202,
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
        mock_response = '{"id": "id", "project": {"id": "id", "href": "href", "definition": {"name": "name"}, "crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::"}, "created_at": "2019-01-01T12:00:00.000Z", "target_account": "target_account", "modified_at": "2019-01-01T12:00:00.000Z", "href": "href", "definition": {"description": "description", "name": "name", "authorizations": {"trusted_profile_id": "trusted_profile_id", "method": "api_key", "api_key": "api_key"}, "inputs": {"anyKey": "anyValue"}, "compliance_profile": {"id": "id", "instance_id": "instance_id", "instance_location": "instance_location", "attachment_id": "attachment_id", "profile_name": "profile_name"}}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a ProjectConfigAuth model
        project_config_auth_model = {}
        project_config_auth_model['trusted_profile_id'] = 'Profile-9ac10c5c-195c-41ef-b465-68a6b6dg5f12'
        project_config_auth_model['method'] = 'trusted_profile'
        project_config_auth_model['api_key'] = 'testString'

        # Construct a dict representation of a ProjectComplianceProfile model
        project_compliance_profile_model = {}
        project_compliance_profile_model['id'] = 'some-profile-id'
        project_compliance_profile_model['instance_id'] = 'some-instance-id'
        project_compliance_profile_model['instance_location'] = 'us-south'
        project_compliance_profile_model['attachment_id'] = 'some-attachment-id'
        project_compliance_profile_model['profile_name'] = 'some-profile-name'

        # Construct a dict representation of a EnvironmentDefinitionRequiredProperties model
        environment_definition_required_properties_model = {}
        environment_definition_required_properties_model['description'] = 'The environment development.'
        environment_definition_required_properties_model['name'] = 'development'
        environment_definition_required_properties_model['authorizations'] = project_config_auth_model
        environment_definition_required_properties_model['inputs'] = {'resource_group': 'stage', 'region': 'us-south'}
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
        mock_response = '{"id": "id", "project": {"id": "id", "href": "href", "definition": {"name": "name"}, "crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::"}, "created_at": "2019-01-01T12:00:00.000Z", "target_account": "target_account", "modified_at": "2019-01-01T12:00:00.000Z", "href": "href", "definition": {"description": "description", "name": "name", "authorizations": {"trusted_profile_id": "trusted_profile_id", "method": "api_key", "api_key": "api_key"}, "inputs": {"anyKey": "anyValue"}, "compliance_profile": {"id": "id", "instance_id": "instance_id", "instance_location": "instance_location", "attachment_id": "attachment_id", "profile_name": "profile_name"}}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a ProjectConfigAuth model
        project_config_auth_model = {}
        project_config_auth_model['trusted_profile_id'] = 'Profile-9ac10c5c-195c-41ef-b465-68a6b6dg5f12'
        project_config_auth_model['method'] = 'trusted_profile'
        project_config_auth_model['api_key'] = 'testString'

        # Construct a dict representation of a ProjectComplianceProfile model
        project_compliance_profile_model = {}
        project_compliance_profile_model['id'] = 'some-profile-id'
        project_compliance_profile_model['instance_id'] = 'some-instance-id'
        project_compliance_profile_model['instance_location'] = 'us-south'
        project_compliance_profile_model['attachment_id'] = 'some-attachment-id'
        project_compliance_profile_model['profile_name'] = 'some-profile-name'

        # Construct a dict representation of a EnvironmentDefinitionRequiredProperties model
        environment_definition_required_properties_model = {}
        environment_definition_required_properties_model['description'] = 'The environment development.'
        environment_definition_required_properties_model['name'] = 'development'
        environment_definition_required_properties_model['authorizations'] = project_config_auth_model
        environment_definition_required_properties_model['inputs'] = {'resource_group': 'stage', 'region': 'us-south'}
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
        mock_response = '{"limit": 10, "first": {"href": "href"}, "next": {"href": "href"}, "environments": [{"id": "id", "project": {"id": "id", "href": "href", "definition": {"name": "name"}, "crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::"}, "created_at": "2019-01-01T12:00:00.000Z", "target_account": "target_account", "modified_at": "2019-01-01T12:00:00.000Z", "href": "href", "definition": {"description": "description", "name": "name", "authorizations": {"trusted_profile_id": "trusted_profile_id", "method": "api_key", "api_key": "api_key"}, "inputs": {"anyKey": "anyValue"}, "compliance_profile": {"id": "id", "instance_id": "instance_id", "instance_location": "instance_location", "attachment_id": "attachment_id", "profile_name": "profile_name"}}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = 'testString'
        token = 'testString'
        limit = 10

        # Invoke method
        response = _service.list_project_environments(
            project_id,
            token=token,
            limit=limit,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'token={}'.format(token) in query_string
        assert 'limit={}'.format(limit) in query_string

    def test_list_project_environments_all_params_with_retries(self):
        # Enable retries and run test_list_project_environments_all_params.
        _service.enable_retries()
        self.test_list_project_environments_all_params()

        # Disable retries and run test_list_project_environments_all_params.
        _service.disable_retries()
        self.test_list_project_environments_all_params()

    @responses.activate
    def test_list_project_environments_required_params(self):
        """
        test_list_project_environments_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/projects/testString/environments')
        mock_response = '{"limit": 10, "first": {"href": "href"}, "next": {"href": "href"}, "environments": [{"id": "id", "project": {"id": "id", "href": "href", "definition": {"name": "name"}, "crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::"}, "created_at": "2019-01-01T12:00:00.000Z", "target_account": "target_account", "modified_at": "2019-01-01T12:00:00.000Z", "href": "href", "definition": {"description": "description", "name": "name", "authorizations": {"trusted_profile_id": "trusted_profile_id", "method": "api_key", "api_key": "api_key"}, "inputs": {"anyKey": "anyValue"}, "compliance_profile": {"id": "id", "instance_id": "instance_id", "instance_location": "instance_location", "attachment_id": "attachment_id", "profile_name": "profile_name"}}}]}'
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

    def test_list_project_environments_required_params_with_retries(self):
        # Enable retries and run test_list_project_environments_required_params.
        _service.enable_retries()
        self.test_list_project_environments_required_params()

        # Disable retries and run test_list_project_environments_required_params.
        _service.disable_retries()
        self.test_list_project_environments_required_params()

    @responses.activate
    def test_list_project_environments_value_error(self):
        """
        test_list_project_environments_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/projects/testString/environments')
        mock_response = '{"limit": 10, "first": {"href": "href"}, "next": {"href": "href"}, "environments": [{"id": "id", "project": {"id": "id", "href": "href", "definition": {"name": "name"}, "crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::"}, "created_at": "2019-01-01T12:00:00.000Z", "target_account": "target_account", "modified_at": "2019-01-01T12:00:00.000Z", "href": "href", "definition": {"description": "description", "name": "name", "authorizations": {"trusted_profile_id": "trusted_profile_id", "method": "api_key", "api_key": "api_key"}, "inputs": {"anyKey": "anyValue"}, "compliance_profile": {"id": "id", "instance_id": "instance_id", "instance_location": "instance_location", "attachment_id": "attachment_id", "profile_name": "profile_name"}}}]}'
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

    @responses.activate
    def test_list_project_environments_with_pager_get_next(self):
        """
        test_list_project_environments_with_pager_get_next()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v1/projects/testString/environments')
        mock_response1 = '{"next":{"href":"https://myhost.com/somePath?token=1"},"environments":[{"id":"id","project":{"id":"id","href":"href","definition":{"name":"name"},"crn":"crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::"},"created_at":"2019-01-01T12:00:00.000Z","target_account":"target_account","modified_at":"2019-01-01T12:00:00.000Z","href":"href","definition":{"description":"description","name":"name","authorizations":{"trusted_profile_id":"trusted_profile_id","method":"api_key","api_key":"api_key"},"inputs":{"anyKey":"anyValue"},"compliance_profile":{"id":"id","instance_id":"instance_id","instance_location":"instance_location","attachment_id":"attachment_id","profile_name":"profile_name"}}}],"total_count":2,"limit":1}'
        mock_response2 = '{"environments":[{"id":"id","project":{"id":"id","href":"href","definition":{"name":"name"},"crn":"crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::"},"created_at":"2019-01-01T12:00:00.000Z","target_account":"target_account","modified_at":"2019-01-01T12:00:00.000Z","href":"href","definition":{"description":"description","name":"name","authorizations":{"trusted_profile_id":"trusted_profile_id","method":"api_key","api_key":"api_key"},"inputs":{"anyKey":"anyValue"},"compliance_profile":{"id":"id","instance_id":"instance_id","instance_location":"instance_location","attachment_id":"attachment_id","profile_name":"profile_name"}}}],"total_count":2,"limit":1}'
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
        pager = ProjectEnvironmentsPager(
            client=_service,
            project_id='testString',
            limit=10,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)
        assert len(all_results) == 2

    @responses.activate
    def test_list_project_environments_with_pager_get_all(self):
        """
        test_list_project_environments_with_pager_get_all()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v1/projects/testString/environments')
        mock_response1 = '{"next":{"href":"https://myhost.com/somePath?token=1"},"environments":[{"id":"id","project":{"id":"id","href":"href","definition":{"name":"name"},"crn":"crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::"},"created_at":"2019-01-01T12:00:00.000Z","target_account":"target_account","modified_at":"2019-01-01T12:00:00.000Z","href":"href","definition":{"description":"description","name":"name","authorizations":{"trusted_profile_id":"trusted_profile_id","method":"api_key","api_key":"api_key"},"inputs":{"anyKey":"anyValue"},"compliance_profile":{"id":"id","instance_id":"instance_id","instance_location":"instance_location","attachment_id":"attachment_id","profile_name":"profile_name"}}}],"total_count":2,"limit":1}'
        mock_response2 = '{"environments":[{"id":"id","project":{"id":"id","href":"href","definition":{"name":"name"},"crn":"crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::"},"created_at":"2019-01-01T12:00:00.000Z","target_account":"target_account","modified_at":"2019-01-01T12:00:00.000Z","href":"href","definition":{"description":"description","name":"name","authorizations":{"trusted_profile_id":"trusted_profile_id","method":"api_key","api_key":"api_key"},"inputs":{"anyKey":"anyValue"},"compliance_profile":{"id":"id","instance_id":"instance_id","instance_location":"instance_location","attachment_id":"attachment_id","profile_name":"profile_name"}}}],"total_count":2,"limit":1}'
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
        pager = ProjectEnvironmentsPager(
            client=_service,
            project_id='testString',
            limit=10,
        )
        all_results = pager.get_all()
        assert all_results is not None
        assert len(all_results) == 2


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
        mock_response = '{"id": "id", "project": {"id": "id", "href": "href", "definition": {"name": "name"}, "crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::"}, "created_at": "2019-01-01T12:00:00.000Z", "target_account": "target_account", "modified_at": "2019-01-01T12:00:00.000Z", "href": "href", "definition": {"description": "description", "name": "name", "authorizations": {"trusted_profile_id": "trusted_profile_id", "method": "api_key", "api_key": "api_key"}, "inputs": {"anyKey": "anyValue"}, "compliance_profile": {"id": "id", "instance_id": "instance_id", "instance_location": "instance_location", "attachment_id": "attachment_id", "profile_name": "profile_name"}}}'
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
        mock_response = '{"id": "id", "project": {"id": "id", "href": "href", "definition": {"name": "name"}, "crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::"}, "created_at": "2019-01-01T12:00:00.000Z", "target_account": "target_account", "modified_at": "2019-01-01T12:00:00.000Z", "href": "href", "definition": {"description": "description", "name": "name", "authorizations": {"trusted_profile_id": "trusted_profile_id", "method": "api_key", "api_key": "api_key"}, "inputs": {"anyKey": "anyValue"}, "compliance_profile": {"id": "id", "instance_id": "instance_id", "instance_location": "instance_location", "attachment_id": "attachment_id", "profile_name": "profile_name"}}}'
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
        mock_response = '{"id": "id", "project": {"id": "id", "href": "href", "definition": {"name": "name"}, "crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::"}, "created_at": "2019-01-01T12:00:00.000Z", "target_account": "target_account", "modified_at": "2019-01-01T12:00:00.000Z", "href": "href", "definition": {"description": "description", "name": "name", "authorizations": {"trusted_profile_id": "trusted_profile_id", "method": "api_key", "api_key": "api_key"}, "inputs": {"anyKey": "anyValue"}, "compliance_profile": {"id": "id", "instance_id": "instance_id", "instance_location": "instance_location", "attachment_id": "attachment_id", "profile_name": "profile_name"}}}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a ProjectConfigAuth model
        project_config_auth_model = {}
        project_config_auth_model['trusted_profile_id'] = 'Profile-9ac10c5c-195c-41ef-b465-68a6b6dg5f12'
        project_config_auth_model['method'] = 'trusted_profile'
        project_config_auth_model['api_key'] = 'testString'

        # Construct a dict representation of a ProjectComplianceProfile model
        project_compliance_profile_model = {}
        project_compliance_profile_model['id'] = 'some-profile-id'
        project_compliance_profile_model['instance_id'] = 'some-instance-id'
        project_compliance_profile_model['instance_location'] = 'us-south'
        project_compliance_profile_model['attachment_id'] = 'some-attachment-id'
        project_compliance_profile_model['profile_name'] = 'some-profile-name'

        # Construct a dict representation of a EnvironmentDefinitionPropertiesPatch model
        environment_definition_properties_patch_model = {}
        environment_definition_properties_patch_model['description'] = 'The environment development.'
        environment_definition_properties_patch_model['name'] = 'development'
        environment_definition_properties_patch_model['authorizations'] = project_config_auth_model
        environment_definition_properties_patch_model['inputs'] = {'resource_group': 'stage', 'region': 'us-south'}
        environment_definition_properties_patch_model['compliance_profile'] = project_compliance_profile_model

        # Set up parameter values
        project_id = 'testString'
        id = 'testString'
        definition = environment_definition_properties_patch_model

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
        assert req_body['definition'] == environment_definition_properties_patch_model

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
        mock_response = '{"id": "id", "project": {"id": "id", "href": "href", "definition": {"name": "name"}, "crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::"}, "created_at": "2019-01-01T12:00:00.000Z", "target_account": "target_account", "modified_at": "2019-01-01T12:00:00.000Z", "href": "href", "definition": {"description": "description", "name": "name", "authorizations": {"trusted_profile_id": "trusted_profile_id", "method": "api_key", "api_key": "api_key"}, "inputs": {"anyKey": "anyValue"}, "compliance_profile": {"id": "id", "instance_id": "instance_id", "instance_location": "instance_location", "attachment_id": "attachment_id", "profile_name": "profile_name"}}}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a ProjectConfigAuth model
        project_config_auth_model = {}
        project_config_auth_model['trusted_profile_id'] = 'Profile-9ac10c5c-195c-41ef-b465-68a6b6dg5f12'
        project_config_auth_model['method'] = 'trusted_profile'
        project_config_auth_model['api_key'] = 'testString'

        # Construct a dict representation of a ProjectComplianceProfile model
        project_compliance_profile_model = {}
        project_compliance_profile_model['id'] = 'some-profile-id'
        project_compliance_profile_model['instance_id'] = 'some-instance-id'
        project_compliance_profile_model['instance_location'] = 'us-south'
        project_compliance_profile_model['attachment_id'] = 'some-attachment-id'
        project_compliance_profile_model['profile_name'] = 'some-profile-name'

        # Construct a dict representation of a EnvironmentDefinitionPropertiesPatch model
        environment_definition_properties_patch_model = {}
        environment_definition_properties_patch_model['description'] = 'The environment development.'
        environment_definition_properties_patch_model['name'] = 'development'
        environment_definition_properties_patch_model['authorizations'] = project_config_auth_model
        environment_definition_properties_patch_model['inputs'] = {'resource_group': 'stage', 'region': 'us-south'}
        environment_definition_properties_patch_model['compliance_profile'] = project_compliance_profile_model

        # Set up parameter values
        project_id = 'testString'
        id = 'testString'
        definition = environment_definition_properties_patch_model

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
        mock_response = '{"id": "id", "version": 7, "is_draft": true, "needs_attention_state": [{"event_id": "event_id", "event": "event", "severity": "INFO", "action_url": "action_url", "target": "target", "triggered_by": "triggered_by", "timestamp": "timestamp"}], "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "last_approved": {"at": "2019-01-01T12:00:00.000Z", "comment": "comment", "is_forced": false, "user_id": "user_id"}, "last_saved_at": "2019-01-01T12:00:00.000Z", "last_validated": {"href": "href", "result": "failed", "job": {"id": "id", "summary": {"version": "version", "plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "success_messages": ["success_messages"], "update_messages": ["update_messages"], "destroy_messages": ["destroy_messages"]}, "apply_messages": {"error_messages": [{}], "success_messages": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}, "pre_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}, "post_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}, "cost_estimate": {"version": "version", "currency": "USD", "totalHourlyCost": "total_hourly_cost", "totalMonthlyCost": "total_monthly_cost", "pastTotalHourlyCost": "past_total_hourly_cost", "pastTotalMonthlyCost": "past_total_monthly_cost", "diffTotalHourlyCost": "diff_total_hourly_cost", "diffTotalMonthlyCost": "diff_total_monthly_cost", "timeGenerated": "2019-01-01T12:00:00.000Z", "user_id": "user_id"}, "cra_logs": {"cra_version": "2.0.4", "schema_version": "schema_version", "status": "passed", "summary": {"total": "total", "passed": "passed", "failed": "failed", "skipped": "skipped"}, "timestamp": "2019-01-01T12:00:00.000Z"}}, "last_deployed": {"href": "href", "result": "failed", "job": {"id": "id", "summary": {"version": "version", "plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "success_messages": ["success_messages"], "update_messages": ["update_messages"], "destroy_messages": ["destroy_messages"]}, "apply_messages": {"error_messages": [{}], "success_messages": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}, "pre_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}, "post_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}}, "last_undeployed": {"href": "href", "result": "failed", "job": {"id": "id", "summary": {"version": "version", "plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "success_messages": ["success_messages"], "update_messages": ["update_messages"], "destroy_messages": ["destroy_messages"]}, "apply_messages": {"error_messages": [{}], "success_messages": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}, "pre_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}, "post_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}}, "last_monitoring": {"href": "href", "result": "failed", "drift_detection": {"job": {"id": "id", "summary": {"version": "version", "plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "success_messages": ["success_messages"], "update_messages": ["update_messages"], "destroy_messages": ["destroy_messages"]}, "apply_messages": {"error_messages": [{}], "success_messages": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}}}, "outputs": [{"name": "name", "description": "description", "value": "anyValue"}], "project": {"id": "id", "href": "href", "definition": {"name": "name"}, "crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::"}, "references": {"anyKey": "anyValue"}, "schematics": {"workspace_crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::", "validate_pre_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "validate_post_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "deploy_pre_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "deploy_post_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "undeploy_pre_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "undeploy_post_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}}, "state": "approved", "update_available": true, "template": {"id": "id", "href": "href"}, "href": "href", "definition": {"compliance_profile": {"id": "id", "instance_id": "instance_id", "instance_location": "instance_location", "attachment_id": "attachment_id", "profile_name": "profile_name"}, "locator_id": "locator_id", "description": "description", "name": "name", "environment_id": "environment_id", "authorizations": {"trusted_profile_id": "trusted_profile_id", "method": "api_key", "api_key": "api_key"}, "inputs": {"anyKey": "anyValue"}, "settings": {"anyKey": "anyValue"}}, "approved_version": {"definition": {"environment_id": "environment_id", "locator_id": "locator_id"}, "state": "approved", "version": 7, "href": "href"}, "deployed_version": {"definition": {"environment_id": "environment_id", "locator_id": "locator_id"}, "state": "approved", "version": 7, "href": "href"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a ProjectComplianceProfile model
        project_compliance_profile_model = {}
        project_compliance_profile_model['id'] = 'testString'
        project_compliance_profile_model['instance_id'] = 'testString'
        project_compliance_profile_model['instance_location'] = 'testString'
        project_compliance_profile_model['attachment_id'] = 'testString'
        project_compliance_profile_model['profile_name'] = 'testString'

        # Construct a dict representation of a ProjectConfigAuth model
        project_config_auth_model = {}
        project_config_auth_model['trusted_profile_id'] = 'testString'
        project_config_auth_model['method'] = 'api_key'
        project_config_auth_model['api_key'] = 'testString'

        # Construct a dict representation of a ProjectConfigDefinitionPrototypeDAConfigDefinitionPropertiesPrototype model
        project_config_definition_prototype_model = {}
        project_config_definition_prototype_model['compliance_profile'] = project_compliance_profile_model
        project_config_definition_prototype_model['locator_id'] = (
            '1082e7d2-5e2f-0a11-a3bc-f88a8e1931fc.018edf04-e772-4ca2-9785-03e8e03bef72-global'
        )
        project_config_definition_prototype_model['description'] = 'The stage environment configuration.'
        project_config_definition_prototype_model['name'] = 'env-stage'
        project_config_definition_prototype_model['environment_id'] = 'testString'
        project_config_definition_prototype_model['authorizations'] = project_config_auth_model
        project_config_definition_prototype_model['inputs'] = {
            'account_id': 'account_id',
            'resource_group': 'stage',
            'access_tags': ['env:stage'],
            'logdna_name': 'LogDNA_stage_service',
            'sysdig_name': 'SysDig_stage_service',
        }
        project_config_definition_prototype_model['settings'] = {'anyKey': 'anyValue'}

        # Construct a dict representation of a SchematicsWorkspace model
        schematics_workspace_model = {}
        schematics_workspace_model['workspace_crn'] = (
            'crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::'
        )

        # Set up parameter values
        project_id = 'testString'
        definition = project_config_definition_prototype_model
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
        assert req_body['definition'] == project_config_definition_prototype_model
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
        mock_response = '{"id": "id", "version": 7, "is_draft": true, "needs_attention_state": [{"event_id": "event_id", "event": "event", "severity": "INFO", "action_url": "action_url", "target": "target", "triggered_by": "triggered_by", "timestamp": "timestamp"}], "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "last_approved": {"at": "2019-01-01T12:00:00.000Z", "comment": "comment", "is_forced": false, "user_id": "user_id"}, "last_saved_at": "2019-01-01T12:00:00.000Z", "last_validated": {"href": "href", "result": "failed", "job": {"id": "id", "summary": {"version": "version", "plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "success_messages": ["success_messages"], "update_messages": ["update_messages"], "destroy_messages": ["destroy_messages"]}, "apply_messages": {"error_messages": [{}], "success_messages": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}, "pre_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}, "post_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}, "cost_estimate": {"version": "version", "currency": "USD", "totalHourlyCost": "total_hourly_cost", "totalMonthlyCost": "total_monthly_cost", "pastTotalHourlyCost": "past_total_hourly_cost", "pastTotalMonthlyCost": "past_total_monthly_cost", "diffTotalHourlyCost": "diff_total_hourly_cost", "diffTotalMonthlyCost": "diff_total_monthly_cost", "timeGenerated": "2019-01-01T12:00:00.000Z", "user_id": "user_id"}, "cra_logs": {"cra_version": "2.0.4", "schema_version": "schema_version", "status": "passed", "summary": {"total": "total", "passed": "passed", "failed": "failed", "skipped": "skipped"}, "timestamp": "2019-01-01T12:00:00.000Z"}}, "last_deployed": {"href": "href", "result": "failed", "job": {"id": "id", "summary": {"version": "version", "plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "success_messages": ["success_messages"], "update_messages": ["update_messages"], "destroy_messages": ["destroy_messages"]}, "apply_messages": {"error_messages": [{}], "success_messages": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}, "pre_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}, "post_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}}, "last_undeployed": {"href": "href", "result": "failed", "job": {"id": "id", "summary": {"version": "version", "plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "success_messages": ["success_messages"], "update_messages": ["update_messages"], "destroy_messages": ["destroy_messages"]}, "apply_messages": {"error_messages": [{}], "success_messages": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}, "pre_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}, "post_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}}, "last_monitoring": {"href": "href", "result": "failed", "drift_detection": {"job": {"id": "id", "summary": {"version": "version", "plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "success_messages": ["success_messages"], "update_messages": ["update_messages"], "destroy_messages": ["destroy_messages"]}, "apply_messages": {"error_messages": [{}], "success_messages": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}}}, "outputs": [{"name": "name", "description": "description", "value": "anyValue"}], "project": {"id": "id", "href": "href", "definition": {"name": "name"}, "crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::"}, "references": {"anyKey": "anyValue"}, "schematics": {"workspace_crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::", "validate_pre_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "validate_post_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "deploy_pre_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "deploy_post_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "undeploy_pre_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "undeploy_post_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}}, "state": "approved", "update_available": true, "template": {"id": "id", "href": "href"}, "href": "href", "definition": {"compliance_profile": {"id": "id", "instance_id": "instance_id", "instance_location": "instance_location", "attachment_id": "attachment_id", "profile_name": "profile_name"}, "locator_id": "locator_id", "description": "description", "name": "name", "environment_id": "environment_id", "authorizations": {"trusted_profile_id": "trusted_profile_id", "method": "api_key", "api_key": "api_key"}, "inputs": {"anyKey": "anyValue"}, "settings": {"anyKey": "anyValue"}}, "approved_version": {"definition": {"environment_id": "environment_id", "locator_id": "locator_id"}, "state": "approved", "version": 7, "href": "href"}, "deployed_version": {"definition": {"environment_id": "environment_id", "locator_id": "locator_id"}, "state": "approved", "version": 7, "href": "href"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a ProjectComplianceProfile model
        project_compliance_profile_model = {}
        project_compliance_profile_model['id'] = 'testString'
        project_compliance_profile_model['instance_id'] = 'testString'
        project_compliance_profile_model['instance_location'] = 'testString'
        project_compliance_profile_model['attachment_id'] = 'testString'
        project_compliance_profile_model['profile_name'] = 'testString'

        # Construct a dict representation of a ProjectConfigAuth model
        project_config_auth_model = {}
        project_config_auth_model['trusted_profile_id'] = 'testString'
        project_config_auth_model['method'] = 'api_key'
        project_config_auth_model['api_key'] = 'testString'

        # Construct a dict representation of a ProjectConfigDefinitionPrototypeDAConfigDefinitionPropertiesPrototype model
        project_config_definition_prototype_model = {}
        project_config_definition_prototype_model['compliance_profile'] = project_compliance_profile_model
        project_config_definition_prototype_model['locator_id'] = (
            '1082e7d2-5e2f-0a11-a3bc-f88a8e1931fc.018edf04-e772-4ca2-9785-03e8e03bef72-global'
        )
        project_config_definition_prototype_model['description'] = 'The stage environment configuration.'
        project_config_definition_prototype_model['name'] = 'env-stage'
        project_config_definition_prototype_model['environment_id'] = 'testString'
        project_config_definition_prototype_model['authorizations'] = project_config_auth_model
        project_config_definition_prototype_model['inputs'] = {
            'account_id': 'account_id',
            'resource_group': 'stage',
            'access_tags': ['env:stage'],
            'logdna_name': 'LogDNA_stage_service',
            'sysdig_name': 'SysDig_stage_service',
        }
        project_config_definition_prototype_model['settings'] = {'anyKey': 'anyValue'}

        # Construct a dict representation of a SchematicsWorkspace model
        schematics_workspace_model = {}
        schematics_workspace_model['workspace_crn'] = (
            'crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::'
        )

        # Set up parameter values
        project_id = 'testString'
        definition = project_config_definition_prototype_model
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
        mock_response = '{"limit": 10, "first": {"href": "href"}, "next": {"href": "href"}, "configs": [{"approved_version": {"definition": {"environment_id": "environment_id", "locator_id": "locator_id"}, "state": "approved", "version": 7, "href": "href"}, "deployed_version": {"definition": {"environment_id": "environment_id", "locator_id": "locator_id"}, "state": "approved", "version": 7, "href": "href"}, "id": "id", "version": 7, "state": "approved", "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "href": "href", "definition": {"description": "description", "name": "name", "locator_id": "locator_id"}, "project": {"id": "id", "href": "href", "definition": {"name": "name"}, "crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::"}, "deployment_model": "project_deployed"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = 'testString'
        token = 'testString'
        limit = 10

        # Invoke method
        response = _service.list_configs(
            project_id,
            token=token,
            limit=limit,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'token={}'.format(token) in query_string
        assert 'limit={}'.format(limit) in query_string

    def test_list_configs_all_params_with_retries(self):
        # Enable retries and run test_list_configs_all_params.
        _service.enable_retries()
        self.test_list_configs_all_params()

        # Disable retries and run test_list_configs_all_params.
        _service.disable_retries()
        self.test_list_configs_all_params()

    @responses.activate
    def test_list_configs_required_params(self):
        """
        test_list_configs_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/projects/testString/configs')
        mock_response = '{"limit": 10, "first": {"href": "href"}, "next": {"href": "href"}, "configs": [{"approved_version": {"definition": {"environment_id": "environment_id", "locator_id": "locator_id"}, "state": "approved", "version": 7, "href": "href"}, "deployed_version": {"definition": {"environment_id": "environment_id", "locator_id": "locator_id"}, "state": "approved", "version": 7, "href": "href"}, "id": "id", "version": 7, "state": "approved", "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "href": "href", "definition": {"description": "description", "name": "name", "locator_id": "locator_id"}, "project": {"id": "id", "href": "href", "definition": {"name": "name"}, "crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::"}, "deployment_model": "project_deployed"}]}'
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

    def test_list_configs_required_params_with_retries(self):
        # Enable retries and run test_list_configs_required_params.
        _service.enable_retries()
        self.test_list_configs_required_params()

        # Disable retries and run test_list_configs_required_params.
        _service.disable_retries()
        self.test_list_configs_required_params()

    @responses.activate
    def test_list_configs_value_error(self):
        """
        test_list_configs_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/projects/testString/configs')
        mock_response = '{"limit": 10, "first": {"href": "href"}, "next": {"href": "href"}, "configs": [{"approved_version": {"definition": {"environment_id": "environment_id", "locator_id": "locator_id"}, "state": "approved", "version": 7, "href": "href"}, "deployed_version": {"definition": {"environment_id": "environment_id", "locator_id": "locator_id"}, "state": "approved", "version": 7, "href": "href"}, "id": "id", "version": 7, "state": "approved", "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "href": "href", "definition": {"description": "description", "name": "name", "locator_id": "locator_id"}, "project": {"id": "id", "href": "href", "definition": {"name": "name"}, "crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::"}, "deployment_model": "project_deployed"}]}'
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

    @responses.activate
    def test_list_configs_with_pager_get_next(self):
        """
        test_list_configs_with_pager_get_next()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v1/projects/testString/configs')
        mock_response1 = '{"next":{"href":"https://myhost.com/somePath?token=1"},"configs":[{"approved_version":{"definition":{"environment_id":"environment_id","locator_id":"locator_id"},"state":"approved","version":7,"href":"href"},"deployed_version":{"definition":{"environment_id":"environment_id","locator_id":"locator_id"},"state":"approved","version":7,"href":"href"},"id":"id","version":7,"state":"approved","created_at":"2019-01-01T12:00:00.000Z","modified_at":"2019-01-01T12:00:00.000Z","href":"href","definition":{"description":"description","name":"name","locator_id":"locator_id"},"project":{"id":"id","href":"href","definition":{"name":"name"},"crn":"crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::"},"deployment_model":"project_deployed"}],"total_count":2,"limit":1}'
        mock_response2 = '{"configs":[{"approved_version":{"definition":{"environment_id":"environment_id","locator_id":"locator_id"},"state":"approved","version":7,"href":"href"},"deployed_version":{"definition":{"environment_id":"environment_id","locator_id":"locator_id"},"state":"approved","version":7,"href":"href"},"id":"id","version":7,"state":"approved","created_at":"2019-01-01T12:00:00.000Z","modified_at":"2019-01-01T12:00:00.000Z","href":"href","definition":{"description":"description","name":"name","locator_id":"locator_id"},"project":{"id":"id","href":"href","definition":{"name":"name"},"crn":"crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::"},"deployment_model":"project_deployed"}],"total_count":2,"limit":1}'
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
        pager = ConfigsPager(
            client=_service,
            project_id='testString',
            limit=10,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)
        assert len(all_results) == 2

    @responses.activate
    def test_list_configs_with_pager_get_all(self):
        """
        test_list_configs_with_pager_get_all()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v1/projects/testString/configs')
        mock_response1 = '{"next":{"href":"https://myhost.com/somePath?token=1"},"configs":[{"approved_version":{"definition":{"environment_id":"environment_id","locator_id":"locator_id"},"state":"approved","version":7,"href":"href"},"deployed_version":{"definition":{"environment_id":"environment_id","locator_id":"locator_id"},"state":"approved","version":7,"href":"href"},"id":"id","version":7,"state":"approved","created_at":"2019-01-01T12:00:00.000Z","modified_at":"2019-01-01T12:00:00.000Z","href":"href","definition":{"description":"description","name":"name","locator_id":"locator_id"},"project":{"id":"id","href":"href","definition":{"name":"name"},"crn":"crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::"},"deployment_model":"project_deployed"}],"total_count":2,"limit":1}'
        mock_response2 = '{"configs":[{"approved_version":{"definition":{"environment_id":"environment_id","locator_id":"locator_id"},"state":"approved","version":7,"href":"href"},"deployed_version":{"definition":{"environment_id":"environment_id","locator_id":"locator_id"},"state":"approved","version":7,"href":"href"},"id":"id","version":7,"state":"approved","created_at":"2019-01-01T12:00:00.000Z","modified_at":"2019-01-01T12:00:00.000Z","href":"href","definition":{"description":"description","name":"name","locator_id":"locator_id"},"project":{"id":"id","href":"href","definition":{"name":"name"},"crn":"crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::"},"deployment_model":"project_deployed"}],"total_count":2,"limit":1}'
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
        pager = ConfigsPager(
            client=_service,
            project_id='testString',
            limit=10,
        )
        all_results = pager.get_all()
        assert all_results is not None
        assert len(all_results) == 2


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
        mock_response = '{"id": "id", "version": 7, "is_draft": true, "needs_attention_state": [{"event_id": "event_id", "event": "event", "severity": "INFO", "action_url": "action_url", "target": "target", "triggered_by": "triggered_by", "timestamp": "timestamp"}], "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "last_approved": {"at": "2019-01-01T12:00:00.000Z", "comment": "comment", "is_forced": false, "user_id": "user_id"}, "last_saved_at": "2019-01-01T12:00:00.000Z", "last_validated": {"href": "href", "result": "failed", "job": {"id": "id", "summary": {"version": "version", "plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "success_messages": ["success_messages"], "update_messages": ["update_messages"], "destroy_messages": ["destroy_messages"]}, "apply_messages": {"error_messages": [{}], "success_messages": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}, "pre_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}, "post_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}, "cost_estimate": {"version": "version", "currency": "USD", "totalHourlyCost": "total_hourly_cost", "totalMonthlyCost": "total_monthly_cost", "pastTotalHourlyCost": "past_total_hourly_cost", "pastTotalMonthlyCost": "past_total_monthly_cost", "diffTotalHourlyCost": "diff_total_hourly_cost", "diffTotalMonthlyCost": "diff_total_monthly_cost", "timeGenerated": "2019-01-01T12:00:00.000Z", "user_id": "user_id"}, "cra_logs": {"cra_version": "2.0.4", "schema_version": "schema_version", "status": "passed", "summary": {"total": "total", "passed": "passed", "failed": "failed", "skipped": "skipped"}, "timestamp": "2019-01-01T12:00:00.000Z"}}, "last_deployed": {"href": "href", "result": "failed", "job": {"id": "id", "summary": {"version": "version", "plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "success_messages": ["success_messages"], "update_messages": ["update_messages"], "destroy_messages": ["destroy_messages"]}, "apply_messages": {"error_messages": [{}], "success_messages": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}, "pre_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}, "post_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}}, "last_undeployed": {"href": "href", "result": "failed", "job": {"id": "id", "summary": {"version": "version", "plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "success_messages": ["success_messages"], "update_messages": ["update_messages"], "destroy_messages": ["destroy_messages"]}, "apply_messages": {"error_messages": [{}], "success_messages": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}, "pre_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}, "post_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}}, "last_monitoring": {"href": "href", "result": "failed", "drift_detection": {"job": {"id": "id", "summary": {"version": "version", "plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "success_messages": ["success_messages"], "update_messages": ["update_messages"], "destroy_messages": ["destroy_messages"]}, "apply_messages": {"error_messages": [{}], "success_messages": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}}}, "outputs": [{"name": "name", "description": "description", "value": "anyValue"}], "project": {"id": "id", "href": "href", "definition": {"name": "name"}, "crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::"}, "references": {"anyKey": "anyValue"}, "schematics": {"workspace_crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::", "validate_pre_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "validate_post_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "deploy_pre_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "deploy_post_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "undeploy_pre_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "undeploy_post_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}}, "state": "approved", "update_available": true, "template": {"id": "id", "href": "href"}, "href": "href", "definition": {"compliance_profile": {"id": "id", "instance_id": "instance_id", "instance_location": "instance_location", "attachment_id": "attachment_id", "profile_name": "profile_name"}, "locator_id": "locator_id", "description": "description", "name": "name", "environment_id": "environment_id", "authorizations": {"trusted_profile_id": "trusted_profile_id", "method": "api_key", "api_key": "api_key"}, "inputs": {"anyKey": "anyValue"}, "settings": {"anyKey": "anyValue"}}, "approved_version": {"definition": {"environment_id": "environment_id", "locator_id": "locator_id"}, "state": "approved", "version": 7, "href": "href"}, "deployed_version": {"definition": {"environment_id": "environment_id", "locator_id": "locator_id"}, "state": "approved", "version": 7, "href": "href"}}'
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
        mock_response = '{"id": "id", "version": 7, "is_draft": true, "needs_attention_state": [{"event_id": "event_id", "event": "event", "severity": "INFO", "action_url": "action_url", "target": "target", "triggered_by": "triggered_by", "timestamp": "timestamp"}], "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "last_approved": {"at": "2019-01-01T12:00:00.000Z", "comment": "comment", "is_forced": false, "user_id": "user_id"}, "last_saved_at": "2019-01-01T12:00:00.000Z", "last_validated": {"href": "href", "result": "failed", "job": {"id": "id", "summary": {"version": "version", "plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "success_messages": ["success_messages"], "update_messages": ["update_messages"], "destroy_messages": ["destroy_messages"]}, "apply_messages": {"error_messages": [{}], "success_messages": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}, "pre_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}, "post_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}, "cost_estimate": {"version": "version", "currency": "USD", "totalHourlyCost": "total_hourly_cost", "totalMonthlyCost": "total_monthly_cost", "pastTotalHourlyCost": "past_total_hourly_cost", "pastTotalMonthlyCost": "past_total_monthly_cost", "diffTotalHourlyCost": "diff_total_hourly_cost", "diffTotalMonthlyCost": "diff_total_monthly_cost", "timeGenerated": "2019-01-01T12:00:00.000Z", "user_id": "user_id"}, "cra_logs": {"cra_version": "2.0.4", "schema_version": "schema_version", "status": "passed", "summary": {"total": "total", "passed": "passed", "failed": "failed", "skipped": "skipped"}, "timestamp": "2019-01-01T12:00:00.000Z"}}, "last_deployed": {"href": "href", "result": "failed", "job": {"id": "id", "summary": {"version": "version", "plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "success_messages": ["success_messages"], "update_messages": ["update_messages"], "destroy_messages": ["destroy_messages"]}, "apply_messages": {"error_messages": [{}], "success_messages": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}, "pre_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}, "post_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}}, "last_undeployed": {"href": "href", "result": "failed", "job": {"id": "id", "summary": {"version": "version", "plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "success_messages": ["success_messages"], "update_messages": ["update_messages"], "destroy_messages": ["destroy_messages"]}, "apply_messages": {"error_messages": [{}], "success_messages": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}, "pre_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}, "post_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}}, "last_monitoring": {"href": "href", "result": "failed", "drift_detection": {"job": {"id": "id", "summary": {"version": "version", "plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "success_messages": ["success_messages"], "update_messages": ["update_messages"], "destroy_messages": ["destroy_messages"]}, "apply_messages": {"error_messages": [{}], "success_messages": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}}}, "outputs": [{"name": "name", "description": "description", "value": "anyValue"}], "project": {"id": "id", "href": "href", "definition": {"name": "name"}, "crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::"}, "references": {"anyKey": "anyValue"}, "schematics": {"workspace_crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::", "validate_pre_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "validate_post_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "deploy_pre_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "deploy_post_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "undeploy_pre_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "undeploy_post_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}}, "state": "approved", "update_available": true, "template": {"id": "id", "href": "href"}, "href": "href", "definition": {"compliance_profile": {"id": "id", "instance_id": "instance_id", "instance_location": "instance_location", "attachment_id": "attachment_id", "profile_name": "profile_name"}, "locator_id": "locator_id", "description": "description", "name": "name", "environment_id": "environment_id", "authorizations": {"trusted_profile_id": "trusted_profile_id", "method": "api_key", "api_key": "api_key"}, "inputs": {"anyKey": "anyValue"}, "settings": {"anyKey": "anyValue"}}, "approved_version": {"definition": {"environment_id": "environment_id", "locator_id": "locator_id"}, "state": "approved", "version": 7, "href": "href"}, "deployed_version": {"definition": {"environment_id": "environment_id", "locator_id": "locator_id"}, "state": "approved", "version": 7, "href": "href"}}'
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
        mock_response = '{"id": "id", "version": 7, "is_draft": true, "needs_attention_state": [{"event_id": "event_id", "event": "event", "severity": "INFO", "action_url": "action_url", "target": "target", "triggered_by": "triggered_by", "timestamp": "timestamp"}], "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "last_approved": {"at": "2019-01-01T12:00:00.000Z", "comment": "comment", "is_forced": false, "user_id": "user_id"}, "last_saved_at": "2019-01-01T12:00:00.000Z", "last_validated": {"href": "href", "result": "failed", "job": {"id": "id", "summary": {"version": "version", "plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "success_messages": ["success_messages"], "update_messages": ["update_messages"], "destroy_messages": ["destroy_messages"]}, "apply_messages": {"error_messages": [{}], "success_messages": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}, "pre_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}, "post_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}, "cost_estimate": {"version": "version", "currency": "USD", "totalHourlyCost": "total_hourly_cost", "totalMonthlyCost": "total_monthly_cost", "pastTotalHourlyCost": "past_total_hourly_cost", "pastTotalMonthlyCost": "past_total_monthly_cost", "diffTotalHourlyCost": "diff_total_hourly_cost", "diffTotalMonthlyCost": "diff_total_monthly_cost", "timeGenerated": "2019-01-01T12:00:00.000Z", "user_id": "user_id"}, "cra_logs": {"cra_version": "2.0.4", "schema_version": "schema_version", "status": "passed", "summary": {"total": "total", "passed": "passed", "failed": "failed", "skipped": "skipped"}, "timestamp": "2019-01-01T12:00:00.000Z"}}, "last_deployed": {"href": "href", "result": "failed", "job": {"id": "id", "summary": {"version": "version", "plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "success_messages": ["success_messages"], "update_messages": ["update_messages"], "destroy_messages": ["destroy_messages"]}, "apply_messages": {"error_messages": [{}], "success_messages": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}, "pre_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}, "post_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}}, "last_undeployed": {"href": "href", "result": "failed", "job": {"id": "id", "summary": {"version": "version", "plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "success_messages": ["success_messages"], "update_messages": ["update_messages"], "destroy_messages": ["destroy_messages"]}, "apply_messages": {"error_messages": [{}], "success_messages": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}, "pre_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}, "post_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}}, "last_monitoring": {"href": "href", "result": "failed", "drift_detection": {"job": {"id": "id", "summary": {"version": "version", "plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "success_messages": ["success_messages"], "update_messages": ["update_messages"], "destroy_messages": ["destroy_messages"]}, "apply_messages": {"error_messages": [{}], "success_messages": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}}}, "outputs": [{"name": "name", "description": "description", "value": "anyValue"}], "project": {"id": "id", "href": "href", "definition": {"name": "name"}, "crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::"}, "references": {"anyKey": "anyValue"}, "schematics": {"workspace_crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::", "validate_pre_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "validate_post_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "deploy_pre_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "deploy_post_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "undeploy_pre_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "undeploy_post_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}}, "state": "approved", "update_available": true, "template": {"id": "id", "href": "href"}, "href": "href", "definition": {"compliance_profile": {"id": "id", "instance_id": "instance_id", "instance_location": "instance_location", "attachment_id": "attachment_id", "profile_name": "profile_name"}, "locator_id": "locator_id", "description": "description", "name": "name", "environment_id": "environment_id", "authorizations": {"trusted_profile_id": "trusted_profile_id", "method": "api_key", "api_key": "api_key"}, "inputs": {"anyKey": "anyValue"}, "settings": {"anyKey": "anyValue"}}, "approved_version": {"definition": {"environment_id": "environment_id", "locator_id": "locator_id"}, "state": "approved", "version": 7, "href": "href"}, "deployed_version": {"definition": {"environment_id": "environment_id", "locator_id": "locator_id"}, "state": "approved", "version": 7, "href": "href"}}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a ProjectComplianceProfile model
        project_compliance_profile_model = {}
        project_compliance_profile_model['id'] = 'testString'
        project_compliance_profile_model['instance_id'] = 'testString'
        project_compliance_profile_model['instance_location'] = 'testString'
        project_compliance_profile_model['attachment_id'] = 'testString'
        project_compliance_profile_model['profile_name'] = 'testString'

        # Construct a dict representation of a ProjectConfigAuth model
        project_config_auth_model = {}
        project_config_auth_model['trusted_profile_id'] = 'testString'
        project_config_auth_model['method'] = 'api_key'
        project_config_auth_model['api_key'] = 'testString'

        # Construct a dict representation of a ProjectConfigDefinitionPatchDAConfigDefinitionPropertiesPatch model
        project_config_definition_patch_model = {}
        project_config_definition_patch_model['compliance_profile'] = project_compliance_profile_model
        project_config_definition_patch_model['locator_id'] = 'testString'
        project_config_definition_patch_model['description'] = 'testString'
        project_config_definition_patch_model['name'] = 'env-stage'
        project_config_definition_patch_model['environment_id'] = 'testString'
        project_config_definition_patch_model['authorizations'] = project_config_auth_model
        project_config_definition_patch_model['inputs'] = {
            'account_id': 'account_id',
            'resource_group': 'stage',
            'access_tags': ['env:stage'],
            'logdna_name': 'LogDNA_stage_service',
            'sysdig_name': 'SysDig_stage_service',
        }
        project_config_definition_patch_model['settings'] = {'anyKey': 'anyValue'}

        # Set up parameter values
        project_id = 'testString'
        id = 'testString'
        definition = project_config_definition_patch_model

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
        assert req_body['definition'] == project_config_definition_patch_model

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
        mock_response = '{"id": "id", "version": 7, "is_draft": true, "needs_attention_state": [{"event_id": "event_id", "event": "event", "severity": "INFO", "action_url": "action_url", "target": "target", "triggered_by": "triggered_by", "timestamp": "timestamp"}], "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "last_approved": {"at": "2019-01-01T12:00:00.000Z", "comment": "comment", "is_forced": false, "user_id": "user_id"}, "last_saved_at": "2019-01-01T12:00:00.000Z", "last_validated": {"href": "href", "result": "failed", "job": {"id": "id", "summary": {"version": "version", "plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "success_messages": ["success_messages"], "update_messages": ["update_messages"], "destroy_messages": ["destroy_messages"]}, "apply_messages": {"error_messages": [{}], "success_messages": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}, "pre_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}, "post_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}, "cost_estimate": {"version": "version", "currency": "USD", "totalHourlyCost": "total_hourly_cost", "totalMonthlyCost": "total_monthly_cost", "pastTotalHourlyCost": "past_total_hourly_cost", "pastTotalMonthlyCost": "past_total_monthly_cost", "diffTotalHourlyCost": "diff_total_hourly_cost", "diffTotalMonthlyCost": "diff_total_monthly_cost", "timeGenerated": "2019-01-01T12:00:00.000Z", "user_id": "user_id"}, "cra_logs": {"cra_version": "2.0.4", "schema_version": "schema_version", "status": "passed", "summary": {"total": "total", "passed": "passed", "failed": "failed", "skipped": "skipped"}, "timestamp": "2019-01-01T12:00:00.000Z"}}, "last_deployed": {"href": "href", "result": "failed", "job": {"id": "id", "summary": {"version": "version", "plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "success_messages": ["success_messages"], "update_messages": ["update_messages"], "destroy_messages": ["destroy_messages"]}, "apply_messages": {"error_messages": [{}], "success_messages": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}, "pre_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}, "post_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}}, "last_undeployed": {"href": "href", "result": "failed", "job": {"id": "id", "summary": {"version": "version", "plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "success_messages": ["success_messages"], "update_messages": ["update_messages"], "destroy_messages": ["destroy_messages"]}, "apply_messages": {"error_messages": [{}], "success_messages": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}, "pre_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}, "post_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}}, "last_monitoring": {"href": "href", "result": "failed", "drift_detection": {"job": {"id": "id", "summary": {"version": "version", "plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "success_messages": ["success_messages"], "update_messages": ["update_messages"], "destroy_messages": ["destroy_messages"]}, "apply_messages": {"error_messages": [{}], "success_messages": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}}}, "outputs": [{"name": "name", "description": "description", "value": "anyValue"}], "project": {"id": "id", "href": "href", "definition": {"name": "name"}, "crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::"}, "references": {"anyKey": "anyValue"}, "schematics": {"workspace_crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::", "validate_pre_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "validate_post_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "deploy_pre_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "deploy_post_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "undeploy_pre_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "undeploy_post_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}}, "state": "approved", "update_available": true, "template": {"id": "id", "href": "href"}, "href": "href", "definition": {"compliance_profile": {"id": "id", "instance_id": "instance_id", "instance_location": "instance_location", "attachment_id": "attachment_id", "profile_name": "profile_name"}, "locator_id": "locator_id", "description": "description", "name": "name", "environment_id": "environment_id", "authorizations": {"trusted_profile_id": "trusted_profile_id", "method": "api_key", "api_key": "api_key"}, "inputs": {"anyKey": "anyValue"}, "settings": {"anyKey": "anyValue"}}, "approved_version": {"definition": {"environment_id": "environment_id", "locator_id": "locator_id"}, "state": "approved", "version": 7, "href": "href"}, "deployed_version": {"definition": {"environment_id": "environment_id", "locator_id": "locator_id"}, "state": "approved", "version": 7, "href": "href"}}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a ProjectComplianceProfile model
        project_compliance_profile_model = {}
        project_compliance_profile_model['id'] = 'testString'
        project_compliance_profile_model['instance_id'] = 'testString'
        project_compliance_profile_model['instance_location'] = 'testString'
        project_compliance_profile_model['attachment_id'] = 'testString'
        project_compliance_profile_model['profile_name'] = 'testString'

        # Construct a dict representation of a ProjectConfigAuth model
        project_config_auth_model = {}
        project_config_auth_model['trusted_profile_id'] = 'testString'
        project_config_auth_model['method'] = 'api_key'
        project_config_auth_model['api_key'] = 'testString'

        # Construct a dict representation of a ProjectConfigDefinitionPatchDAConfigDefinitionPropertiesPatch model
        project_config_definition_patch_model = {}
        project_config_definition_patch_model['compliance_profile'] = project_compliance_profile_model
        project_config_definition_patch_model['locator_id'] = 'testString'
        project_config_definition_patch_model['description'] = 'testString'
        project_config_definition_patch_model['name'] = 'env-stage'
        project_config_definition_patch_model['environment_id'] = 'testString'
        project_config_definition_patch_model['authorizations'] = project_config_auth_model
        project_config_definition_patch_model['inputs'] = {
            'account_id': 'account_id',
            'resource_group': 'stage',
            'access_tags': ['env:stage'],
            'logdna_name': 'LogDNA_stage_service',
            'sysdig_name': 'SysDig_stage_service',
        }
        project_config_definition_patch_model['settings'] = {'anyKey': 'anyValue'}

        # Set up parameter values
        project_id = 'testString'
        id = 'testString'
        definition = project_config_definition_patch_model

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
        mock_response = '{"id": "id", "version": 7, "is_draft": true, "needs_attention_state": [{"event_id": "event_id", "event": "event", "severity": "INFO", "action_url": "action_url", "target": "target", "triggered_by": "triggered_by", "timestamp": "timestamp"}], "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "last_approved": {"at": "2019-01-01T12:00:00.000Z", "comment": "comment", "is_forced": false, "user_id": "user_id"}, "last_saved_at": "2019-01-01T12:00:00.000Z", "last_validated": {"href": "href", "result": "failed", "job": {"id": "id", "summary": {"version": "version", "plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "success_messages": ["success_messages"], "update_messages": ["update_messages"], "destroy_messages": ["destroy_messages"]}, "apply_messages": {"error_messages": [{}], "success_messages": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}, "pre_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}, "post_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}, "cost_estimate": {"version": "version", "currency": "USD", "totalHourlyCost": "total_hourly_cost", "totalMonthlyCost": "total_monthly_cost", "pastTotalHourlyCost": "past_total_hourly_cost", "pastTotalMonthlyCost": "past_total_monthly_cost", "diffTotalHourlyCost": "diff_total_hourly_cost", "diffTotalMonthlyCost": "diff_total_monthly_cost", "timeGenerated": "2019-01-01T12:00:00.000Z", "user_id": "user_id"}, "cra_logs": {"cra_version": "2.0.4", "schema_version": "schema_version", "status": "passed", "summary": {"total": "total", "passed": "passed", "failed": "failed", "skipped": "skipped"}, "timestamp": "2019-01-01T12:00:00.000Z"}}, "last_deployed": {"href": "href", "result": "failed", "job": {"id": "id", "summary": {"version": "version", "plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "success_messages": ["success_messages"], "update_messages": ["update_messages"], "destroy_messages": ["destroy_messages"]}, "apply_messages": {"error_messages": [{}], "success_messages": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}, "pre_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}, "post_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}}, "last_undeployed": {"href": "href", "result": "failed", "job": {"id": "id", "summary": {"version": "version", "plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "success_messages": ["success_messages"], "update_messages": ["update_messages"], "destroy_messages": ["destroy_messages"]}, "apply_messages": {"error_messages": [{}], "success_messages": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}, "pre_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}, "post_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}}, "last_monitoring": {"href": "href", "result": "failed", "drift_detection": {"job": {"id": "id", "summary": {"version": "version", "plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "success_messages": ["success_messages"], "update_messages": ["update_messages"], "destroy_messages": ["destroy_messages"]}, "apply_messages": {"error_messages": [{}], "success_messages": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}}}, "outputs": [{"name": "name", "description": "description", "value": "anyValue"}], "project": {"id": "id", "href": "href", "definition": {"name": "name"}, "crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::"}, "references": {"anyKey": "anyValue"}, "schematics": {"workspace_crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::", "validate_pre_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "validate_post_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "deploy_pre_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "deploy_post_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "undeploy_pre_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "undeploy_post_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}}, "state": "approved", "update_available": true, "template": {"id": "id", "href": "href"}, "href": "href", "definition": {"compliance_profile": {"id": "id", "instance_id": "instance_id", "instance_location": "instance_location", "attachment_id": "attachment_id", "profile_name": "profile_name"}, "locator_id": "locator_id", "description": "description", "name": "name", "environment_id": "environment_id", "authorizations": {"trusted_profile_id": "trusted_profile_id", "method": "api_key", "api_key": "api_key"}, "inputs": {"anyKey": "anyValue"}, "settings": {"anyKey": "anyValue"}}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = 'testString'
        id = 'testString'
        comment = 'Approving the changes'

        # Invoke method
        response = _service.force_approve(
            project_id,
            id,
            comment,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
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
        mock_response = '{"id": "id", "version": 7, "is_draft": true, "needs_attention_state": [{"event_id": "event_id", "event": "event", "severity": "INFO", "action_url": "action_url", "target": "target", "triggered_by": "triggered_by", "timestamp": "timestamp"}], "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "last_approved": {"at": "2019-01-01T12:00:00.000Z", "comment": "comment", "is_forced": false, "user_id": "user_id"}, "last_saved_at": "2019-01-01T12:00:00.000Z", "last_validated": {"href": "href", "result": "failed", "job": {"id": "id", "summary": {"version": "version", "plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "success_messages": ["success_messages"], "update_messages": ["update_messages"], "destroy_messages": ["destroy_messages"]}, "apply_messages": {"error_messages": [{}], "success_messages": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}, "pre_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}, "post_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}, "cost_estimate": {"version": "version", "currency": "USD", "totalHourlyCost": "total_hourly_cost", "totalMonthlyCost": "total_monthly_cost", "pastTotalHourlyCost": "past_total_hourly_cost", "pastTotalMonthlyCost": "past_total_monthly_cost", "diffTotalHourlyCost": "diff_total_hourly_cost", "diffTotalMonthlyCost": "diff_total_monthly_cost", "timeGenerated": "2019-01-01T12:00:00.000Z", "user_id": "user_id"}, "cra_logs": {"cra_version": "2.0.4", "schema_version": "schema_version", "status": "passed", "summary": {"total": "total", "passed": "passed", "failed": "failed", "skipped": "skipped"}, "timestamp": "2019-01-01T12:00:00.000Z"}}, "last_deployed": {"href": "href", "result": "failed", "job": {"id": "id", "summary": {"version": "version", "plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "success_messages": ["success_messages"], "update_messages": ["update_messages"], "destroy_messages": ["destroy_messages"]}, "apply_messages": {"error_messages": [{}], "success_messages": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}, "pre_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}, "post_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}}, "last_undeployed": {"href": "href", "result": "failed", "job": {"id": "id", "summary": {"version": "version", "plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "success_messages": ["success_messages"], "update_messages": ["update_messages"], "destroy_messages": ["destroy_messages"]}, "apply_messages": {"error_messages": [{}], "success_messages": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}, "pre_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}, "post_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}}, "last_monitoring": {"href": "href", "result": "failed", "drift_detection": {"job": {"id": "id", "summary": {"version": "version", "plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "success_messages": ["success_messages"], "update_messages": ["update_messages"], "destroy_messages": ["destroy_messages"]}, "apply_messages": {"error_messages": [{}], "success_messages": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}}}, "outputs": [{"name": "name", "description": "description", "value": "anyValue"}], "project": {"id": "id", "href": "href", "definition": {"name": "name"}, "crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::"}, "references": {"anyKey": "anyValue"}, "schematics": {"workspace_crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::", "validate_pre_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "validate_post_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "deploy_pre_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "deploy_post_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "undeploy_pre_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "undeploy_post_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}}, "state": "approved", "update_available": true, "template": {"id": "id", "href": "href"}, "href": "href", "definition": {"compliance_profile": {"id": "id", "instance_id": "instance_id", "instance_location": "instance_location", "attachment_id": "attachment_id", "profile_name": "profile_name"}, "locator_id": "locator_id", "description": "description", "name": "name", "environment_id": "environment_id", "authorizations": {"trusted_profile_id": "trusted_profile_id", "method": "api_key", "api_key": "api_key"}, "inputs": {"anyKey": "anyValue"}, "settings": {"anyKey": "anyValue"}}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = 'testString'
        id = 'testString'
        comment = 'Approving the changes'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "id": id,
            "comment": comment,
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
        mock_response = '{"id": "id", "version": 7, "is_draft": true, "needs_attention_state": [{"event_id": "event_id", "event": "event", "severity": "INFO", "action_url": "action_url", "target": "target", "triggered_by": "triggered_by", "timestamp": "timestamp"}], "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "last_approved": {"at": "2019-01-01T12:00:00.000Z", "comment": "comment", "is_forced": false, "user_id": "user_id"}, "last_saved_at": "2019-01-01T12:00:00.000Z", "last_validated": {"href": "href", "result": "failed", "job": {"id": "id", "summary": {"version": "version", "plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "success_messages": ["success_messages"], "update_messages": ["update_messages"], "destroy_messages": ["destroy_messages"]}, "apply_messages": {"error_messages": [{}], "success_messages": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}, "pre_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}, "post_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}, "cost_estimate": {"version": "version", "currency": "USD", "totalHourlyCost": "total_hourly_cost", "totalMonthlyCost": "total_monthly_cost", "pastTotalHourlyCost": "past_total_hourly_cost", "pastTotalMonthlyCost": "past_total_monthly_cost", "diffTotalHourlyCost": "diff_total_hourly_cost", "diffTotalMonthlyCost": "diff_total_monthly_cost", "timeGenerated": "2019-01-01T12:00:00.000Z", "user_id": "user_id"}, "cra_logs": {"cra_version": "2.0.4", "schema_version": "schema_version", "status": "passed", "summary": {"total": "total", "passed": "passed", "failed": "failed", "skipped": "skipped"}, "timestamp": "2019-01-01T12:00:00.000Z"}}, "last_deployed": {"href": "href", "result": "failed", "job": {"id": "id", "summary": {"version": "version", "plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "success_messages": ["success_messages"], "update_messages": ["update_messages"], "destroy_messages": ["destroy_messages"]}, "apply_messages": {"error_messages": [{}], "success_messages": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}, "pre_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}, "post_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}}, "last_undeployed": {"href": "href", "result": "failed", "job": {"id": "id", "summary": {"version": "version", "plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "success_messages": ["success_messages"], "update_messages": ["update_messages"], "destroy_messages": ["destroy_messages"]}, "apply_messages": {"error_messages": [{}], "success_messages": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}, "pre_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}, "post_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}}, "last_monitoring": {"href": "href", "result": "failed", "drift_detection": {"job": {"id": "id", "summary": {"version": "version", "plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "success_messages": ["success_messages"], "update_messages": ["update_messages"], "destroy_messages": ["destroy_messages"]}, "apply_messages": {"error_messages": [{}], "success_messages": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}}}, "outputs": [{"name": "name", "description": "description", "value": "anyValue"}], "project": {"id": "id", "href": "href", "definition": {"name": "name"}, "crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::"}, "references": {"anyKey": "anyValue"}, "schematics": {"workspace_crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::", "validate_pre_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "validate_post_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "deploy_pre_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "deploy_post_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "undeploy_pre_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "undeploy_post_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}}, "state": "approved", "update_available": true, "template": {"id": "id", "href": "href"}, "href": "href", "definition": {"compliance_profile": {"id": "id", "instance_id": "instance_id", "instance_location": "instance_location", "attachment_id": "attachment_id", "profile_name": "profile_name"}, "locator_id": "locator_id", "description": "description", "name": "name", "environment_id": "environment_id", "authorizations": {"trusted_profile_id": "trusted_profile_id", "method": "api_key", "api_key": "api_key"}, "inputs": {"anyKey": "anyValue"}, "settings": {"anyKey": "anyValue"}}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
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
        assert response.status_code == 200
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
        mock_response = '{"id": "id", "version": 7, "is_draft": true, "needs_attention_state": [{"event_id": "event_id", "event": "event", "severity": "INFO", "action_url": "action_url", "target": "target", "triggered_by": "triggered_by", "timestamp": "timestamp"}], "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "last_approved": {"at": "2019-01-01T12:00:00.000Z", "comment": "comment", "is_forced": false, "user_id": "user_id"}, "last_saved_at": "2019-01-01T12:00:00.000Z", "last_validated": {"href": "href", "result": "failed", "job": {"id": "id", "summary": {"version": "version", "plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "success_messages": ["success_messages"], "update_messages": ["update_messages"], "destroy_messages": ["destroy_messages"]}, "apply_messages": {"error_messages": [{}], "success_messages": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}, "pre_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}, "post_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}, "cost_estimate": {"version": "version", "currency": "USD", "totalHourlyCost": "total_hourly_cost", "totalMonthlyCost": "total_monthly_cost", "pastTotalHourlyCost": "past_total_hourly_cost", "pastTotalMonthlyCost": "past_total_monthly_cost", "diffTotalHourlyCost": "diff_total_hourly_cost", "diffTotalMonthlyCost": "diff_total_monthly_cost", "timeGenerated": "2019-01-01T12:00:00.000Z", "user_id": "user_id"}, "cra_logs": {"cra_version": "2.0.4", "schema_version": "schema_version", "status": "passed", "summary": {"total": "total", "passed": "passed", "failed": "failed", "skipped": "skipped"}, "timestamp": "2019-01-01T12:00:00.000Z"}}, "last_deployed": {"href": "href", "result": "failed", "job": {"id": "id", "summary": {"version": "version", "plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "success_messages": ["success_messages"], "update_messages": ["update_messages"], "destroy_messages": ["destroy_messages"]}, "apply_messages": {"error_messages": [{}], "success_messages": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}, "pre_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}, "post_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}}, "last_undeployed": {"href": "href", "result": "failed", "job": {"id": "id", "summary": {"version": "version", "plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "success_messages": ["success_messages"], "update_messages": ["update_messages"], "destroy_messages": ["destroy_messages"]}, "apply_messages": {"error_messages": [{}], "success_messages": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}, "pre_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}, "post_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}}, "last_monitoring": {"href": "href", "result": "failed", "drift_detection": {"job": {"id": "id", "summary": {"version": "version", "plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "success_messages": ["success_messages"], "update_messages": ["update_messages"], "destroy_messages": ["destroy_messages"]}, "apply_messages": {"error_messages": [{}], "success_messages": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}}}, "outputs": [{"name": "name", "description": "description", "value": "anyValue"}], "project": {"id": "id", "href": "href", "definition": {"name": "name"}, "crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::"}, "references": {"anyKey": "anyValue"}, "schematics": {"workspace_crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::", "validate_pre_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "validate_post_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "deploy_pre_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "deploy_post_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "undeploy_pre_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "undeploy_post_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}}, "state": "approved", "update_available": true, "template": {"id": "id", "href": "href"}, "href": "href", "definition": {"compliance_profile": {"id": "id", "instance_id": "instance_id", "instance_location": "instance_location", "attachment_id": "attachment_id", "profile_name": "profile_name"}, "locator_id": "locator_id", "description": "description", "name": "name", "environment_id": "environment_id", "authorizations": {"trusted_profile_id": "trusted_profile_id", "method": "api_key", "api_key": "api_key"}, "inputs": {"anyKey": "anyValue"}, "settings": {"anyKey": "anyValue"}}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
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
        assert response.status_code == 200

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
        mock_response = '{"id": "id", "version": 7, "is_draft": true, "needs_attention_state": [{"event_id": "event_id", "event": "event", "severity": "INFO", "action_url": "action_url", "target": "target", "triggered_by": "triggered_by", "timestamp": "timestamp"}], "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "last_approved": {"at": "2019-01-01T12:00:00.000Z", "comment": "comment", "is_forced": false, "user_id": "user_id"}, "last_saved_at": "2019-01-01T12:00:00.000Z", "last_validated": {"href": "href", "result": "failed", "job": {"id": "id", "summary": {"version": "version", "plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "success_messages": ["success_messages"], "update_messages": ["update_messages"], "destroy_messages": ["destroy_messages"]}, "apply_messages": {"error_messages": [{}], "success_messages": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}, "pre_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}, "post_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}, "cost_estimate": {"version": "version", "currency": "USD", "totalHourlyCost": "total_hourly_cost", "totalMonthlyCost": "total_monthly_cost", "pastTotalHourlyCost": "past_total_hourly_cost", "pastTotalMonthlyCost": "past_total_monthly_cost", "diffTotalHourlyCost": "diff_total_hourly_cost", "diffTotalMonthlyCost": "diff_total_monthly_cost", "timeGenerated": "2019-01-01T12:00:00.000Z", "user_id": "user_id"}, "cra_logs": {"cra_version": "2.0.4", "schema_version": "schema_version", "status": "passed", "summary": {"total": "total", "passed": "passed", "failed": "failed", "skipped": "skipped"}, "timestamp": "2019-01-01T12:00:00.000Z"}}, "last_deployed": {"href": "href", "result": "failed", "job": {"id": "id", "summary": {"version": "version", "plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "success_messages": ["success_messages"], "update_messages": ["update_messages"], "destroy_messages": ["destroy_messages"]}, "apply_messages": {"error_messages": [{}], "success_messages": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}, "pre_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}, "post_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}}, "last_undeployed": {"href": "href", "result": "failed", "job": {"id": "id", "summary": {"version": "version", "plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "success_messages": ["success_messages"], "update_messages": ["update_messages"], "destroy_messages": ["destroy_messages"]}, "apply_messages": {"error_messages": [{}], "success_messages": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}, "pre_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}, "post_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}}, "last_monitoring": {"href": "href", "result": "failed", "drift_detection": {"job": {"id": "id", "summary": {"version": "version", "plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "success_messages": ["success_messages"], "update_messages": ["update_messages"], "destroy_messages": ["destroy_messages"]}, "apply_messages": {"error_messages": [{}], "success_messages": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}}}, "outputs": [{"name": "name", "description": "description", "value": "anyValue"}], "project": {"id": "id", "href": "href", "definition": {"name": "name"}, "crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::"}, "references": {"anyKey": "anyValue"}, "schematics": {"workspace_crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::", "validate_pre_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "validate_post_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "deploy_pre_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "deploy_post_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "undeploy_pre_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "undeploy_post_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}}, "state": "approved", "update_available": true, "template": {"id": "id", "href": "href"}, "href": "href", "definition": {"compliance_profile": {"id": "id", "instance_id": "instance_id", "instance_location": "instance_location", "attachment_id": "attachment_id", "profile_name": "profile_name"}, "locator_id": "locator_id", "description": "description", "name": "name", "environment_id": "environment_id", "authorizations": {"trusted_profile_id": "trusted_profile_id", "method": "api_key", "api_key": "api_key"}, "inputs": {"anyKey": "anyValue"}, "settings": {"anyKey": "anyValue"}}}'
        responses.add(
            responses.POST,
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
        mock_response = '{"id": "id", "version": 7, "is_draft": true, "needs_attention_state": [{"event_id": "event_id", "event": "event", "severity": "INFO", "action_url": "action_url", "target": "target", "triggered_by": "triggered_by", "timestamp": "timestamp"}], "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "last_approved": {"at": "2019-01-01T12:00:00.000Z", "comment": "comment", "is_forced": false, "user_id": "user_id"}, "last_saved_at": "2019-01-01T12:00:00.000Z", "last_validated": {"href": "href", "result": "failed", "job": {"id": "id", "summary": {"version": "version", "plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "success_messages": ["success_messages"], "update_messages": ["update_messages"], "destroy_messages": ["destroy_messages"]}, "apply_messages": {"error_messages": [{}], "success_messages": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}, "pre_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}, "post_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}, "cost_estimate": {"version": "version", "currency": "USD", "totalHourlyCost": "total_hourly_cost", "totalMonthlyCost": "total_monthly_cost", "pastTotalHourlyCost": "past_total_hourly_cost", "pastTotalMonthlyCost": "past_total_monthly_cost", "diffTotalHourlyCost": "diff_total_hourly_cost", "diffTotalMonthlyCost": "diff_total_monthly_cost", "timeGenerated": "2019-01-01T12:00:00.000Z", "user_id": "user_id"}, "cra_logs": {"cra_version": "2.0.4", "schema_version": "schema_version", "status": "passed", "summary": {"total": "total", "passed": "passed", "failed": "failed", "skipped": "skipped"}, "timestamp": "2019-01-01T12:00:00.000Z"}}, "last_deployed": {"href": "href", "result": "failed", "job": {"id": "id", "summary": {"version": "version", "plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "success_messages": ["success_messages"], "update_messages": ["update_messages"], "destroy_messages": ["destroy_messages"]}, "apply_messages": {"error_messages": [{}], "success_messages": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}, "pre_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}, "post_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}}, "last_undeployed": {"href": "href", "result": "failed", "job": {"id": "id", "summary": {"version": "version", "plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "success_messages": ["success_messages"], "update_messages": ["update_messages"], "destroy_messages": ["destroy_messages"]}, "apply_messages": {"error_messages": [{}], "success_messages": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}, "pre_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}, "post_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}}, "last_monitoring": {"href": "href", "result": "failed", "drift_detection": {"job": {"id": "id", "summary": {"version": "version", "plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "success_messages": ["success_messages"], "update_messages": ["update_messages"], "destroy_messages": ["destroy_messages"]}, "apply_messages": {"error_messages": [{}], "success_messages": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}}}, "outputs": [{"name": "name", "description": "description", "value": "anyValue"}], "project": {"id": "id", "href": "href", "definition": {"name": "name"}, "crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::"}, "references": {"anyKey": "anyValue"}, "schematics": {"workspace_crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::", "validate_pre_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "validate_post_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "deploy_pre_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "deploy_post_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "undeploy_pre_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "undeploy_post_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}}, "state": "approved", "update_available": true, "template": {"id": "id", "href": "href"}, "href": "href", "definition": {"compliance_profile": {"id": "id", "instance_id": "instance_id", "instance_location": "instance_location", "attachment_id": "attachment_id", "profile_name": "profile_name"}, "locator_id": "locator_id", "description": "description", "name": "name", "environment_id": "environment_id", "authorizations": {"trusted_profile_id": "trusted_profile_id", "method": "api_key", "api_key": "api_key"}, "inputs": {"anyKey": "anyValue"}, "settings": {"anyKey": "anyValue"}}}'
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
        mock_response = '{"id": "id", "version": 7, "is_draft": true, "needs_attention_state": [{"event_id": "event_id", "event": "event", "severity": "INFO", "action_url": "action_url", "target": "target", "triggered_by": "triggered_by", "timestamp": "timestamp"}], "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "last_approved": {"at": "2019-01-01T12:00:00.000Z", "comment": "comment", "is_forced": false, "user_id": "user_id"}, "last_saved_at": "2019-01-01T12:00:00.000Z", "last_validated": {"href": "href", "result": "failed", "job": {"id": "id", "summary": {"version": "version", "plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "success_messages": ["success_messages"], "update_messages": ["update_messages"], "destroy_messages": ["destroy_messages"]}, "apply_messages": {"error_messages": [{}], "success_messages": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}, "pre_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}, "post_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}, "cost_estimate": {"version": "version", "currency": "USD", "totalHourlyCost": "total_hourly_cost", "totalMonthlyCost": "total_monthly_cost", "pastTotalHourlyCost": "past_total_hourly_cost", "pastTotalMonthlyCost": "past_total_monthly_cost", "diffTotalHourlyCost": "diff_total_hourly_cost", "diffTotalMonthlyCost": "diff_total_monthly_cost", "timeGenerated": "2019-01-01T12:00:00.000Z", "user_id": "user_id"}, "cra_logs": {"cra_version": "2.0.4", "schema_version": "schema_version", "status": "passed", "summary": {"total": "total", "passed": "passed", "failed": "failed", "skipped": "skipped"}, "timestamp": "2019-01-01T12:00:00.000Z"}}, "last_deployed": {"href": "href", "result": "failed", "job": {"id": "id", "summary": {"version": "version", "plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "success_messages": ["success_messages"], "update_messages": ["update_messages"], "destroy_messages": ["destroy_messages"]}, "apply_messages": {"error_messages": [{}], "success_messages": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}, "pre_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}, "post_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}}, "last_undeployed": {"href": "href", "result": "failed", "job": {"id": "id", "summary": {"version": "version", "plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "success_messages": ["success_messages"], "update_messages": ["update_messages"], "destroy_messages": ["destroy_messages"]}, "apply_messages": {"error_messages": [{}], "success_messages": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}, "pre_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}, "post_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}}, "last_monitoring": {"href": "href", "result": "failed", "drift_detection": {"job": {"id": "id", "summary": {"version": "version", "plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "success_messages": ["success_messages"], "update_messages": ["update_messages"], "destroy_messages": ["destroy_messages"]}, "apply_messages": {"error_messages": [{}], "success_messages": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}}}, "outputs": [{"name": "name", "description": "description", "value": "anyValue"}], "project": {"id": "id", "href": "href", "definition": {"name": "name"}, "crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::"}, "references": {"anyKey": "anyValue"}, "schematics": {"workspace_crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::", "validate_pre_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "validate_post_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "deploy_pre_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "deploy_post_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "undeploy_pre_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "undeploy_post_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}}, "state": "approved", "update_available": true, "template": {"id": "id", "href": "href"}, "href": "href", "definition": {"compliance_profile": {"id": "id", "instance_id": "instance_id", "instance_location": "instance_location", "attachment_id": "attachment_id", "profile_name": "profile_name"}, "locator_id": "locator_id", "description": "description", "name": "name", "environment_id": "environment_id", "authorizations": {"trusted_profile_id": "trusted_profile_id", "method": "api_key", "api_key": "api_key"}, "inputs": {"anyKey": "anyValue"}, "settings": {"anyKey": "anyValue"}}}'
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
        mock_response = '{"id": "id", "version": 7, "is_draft": true, "needs_attention_state": [{"event_id": "event_id", "event": "event", "severity": "INFO", "action_url": "action_url", "target": "target", "triggered_by": "triggered_by", "timestamp": "timestamp"}], "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "last_approved": {"at": "2019-01-01T12:00:00.000Z", "comment": "comment", "is_forced": false, "user_id": "user_id"}, "last_saved_at": "2019-01-01T12:00:00.000Z", "last_validated": {"href": "href", "result": "failed", "job": {"id": "id", "summary": {"version": "version", "plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "success_messages": ["success_messages"], "update_messages": ["update_messages"], "destroy_messages": ["destroy_messages"]}, "apply_messages": {"error_messages": [{}], "success_messages": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}, "pre_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}, "post_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}, "cost_estimate": {"version": "version", "currency": "USD", "totalHourlyCost": "total_hourly_cost", "totalMonthlyCost": "total_monthly_cost", "pastTotalHourlyCost": "past_total_hourly_cost", "pastTotalMonthlyCost": "past_total_monthly_cost", "diffTotalHourlyCost": "diff_total_hourly_cost", "diffTotalMonthlyCost": "diff_total_monthly_cost", "timeGenerated": "2019-01-01T12:00:00.000Z", "user_id": "user_id"}, "cra_logs": {"cra_version": "2.0.4", "schema_version": "schema_version", "status": "passed", "summary": {"total": "total", "passed": "passed", "failed": "failed", "skipped": "skipped"}, "timestamp": "2019-01-01T12:00:00.000Z"}}, "last_deployed": {"href": "href", "result": "failed", "job": {"id": "id", "summary": {"version": "version", "plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "success_messages": ["success_messages"], "update_messages": ["update_messages"], "destroy_messages": ["destroy_messages"]}, "apply_messages": {"error_messages": [{}], "success_messages": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}, "pre_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}, "post_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}}, "last_undeployed": {"href": "href", "result": "failed", "job": {"id": "id", "summary": {"version": "version", "plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "success_messages": ["success_messages"], "update_messages": ["update_messages"], "destroy_messages": ["destroy_messages"]}, "apply_messages": {"error_messages": [{}], "success_messages": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}, "pre_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}, "post_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}}, "last_monitoring": {"href": "href", "result": "failed", "drift_detection": {"job": {"id": "id", "summary": {"version": "version", "plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "success_messages": ["success_messages"], "update_messages": ["update_messages"], "destroy_messages": ["destroy_messages"]}, "apply_messages": {"error_messages": [{}], "success_messages": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}}}, "outputs": [{"name": "name", "description": "description", "value": "anyValue"}], "project": {"id": "id", "href": "href", "definition": {"name": "name"}, "crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::"}, "references": {"anyKey": "anyValue"}, "schematics": {"workspace_crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::", "validate_pre_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "validate_post_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "deploy_pre_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "deploy_post_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "undeploy_pre_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "undeploy_post_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}}, "state": "approved", "update_available": true, "template": {"id": "id", "href": "href"}, "href": "href", "definition": {"compliance_profile": {"id": "id", "instance_id": "instance_id", "instance_location": "instance_location", "attachment_id": "attachment_id", "profile_name": "profile_name"}, "locator_id": "locator_id", "description": "description", "name": "name", "environment_id": "environment_id", "authorizations": {"trusted_profile_id": "trusted_profile_id", "method": "api_key", "api_key": "api_key"}, "inputs": {"anyKey": "anyValue"}, "settings": {"anyKey": "anyValue"}}}'
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
        mock_response = '{"id": "id", "version": 7, "is_draft": true, "needs_attention_state": [{"event_id": "event_id", "event": "event", "severity": "INFO", "action_url": "action_url", "target": "target", "triggered_by": "triggered_by", "timestamp": "timestamp"}], "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "last_approved": {"at": "2019-01-01T12:00:00.000Z", "comment": "comment", "is_forced": false, "user_id": "user_id"}, "last_saved_at": "2019-01-01T12:00:00.000Z", "last_validated": {"href": "href", "result": "failed", "job": {"id": "id", "summary": {"version": "version", "plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "success_messages": ["success_messages"], "update_messages": ["update_messages"], "destroy_messages": ["destroy_messages"]}, "apply_messages": {"error_messages": [{}], "success_messages": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}, "pre_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}, "post_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}, "cost_estimate": {"version": "version", "currency": "USD", "totalHourlyCost": "total_hourly_cost", "totalMonthlyCost": "total_monthly_cost", "pastTotalHourlyCost": "past_total_hourly_cost", "pastTotalMonthlyCost": "past_total_monthly_cost", "diffTotalHourlyCost": "diff_total_hourly_cost", "diffTotalMonthlyCost": "diff_total_monthly_cost", "timeGenerated": "2019-01-01T12:00:00.000Z", "user_id": "user_id"}, "cra_logs": {"cra_version": "2.0.4", "schema_version": "schema_version", "status": "passed", "summary": {"total": "total", "passed": "passed", "failed": "failed", "skipped": "skipped"}, "timestamp": "2019-01-01T12:00:00.000Z"}}, "last_deployed": {"href": "href", "result": "failed", "job": {"id": "id", "summary": {"version": "version", "plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "success_messages": ["success_messages"], "update_messages": ["update_messages"], "destroy_messages": ["destroy_messages"]}, "apply_messages": {"error_messages": [{}], "success_messages": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}, "pre_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}, "post_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}}, "last_undeployed": {"href": "href", "result": "failed", "job": {"id": "id", "summary": {"version": "version", "plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "success_messages": ["success_messages"], "update_messages": ["update_messages"], "destroy_messages": ["destroy_messages"]}, "apply_messages": {"error_messages": [{}], "success_messages": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}, "pre_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}, "post_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}}, "last_monitoring": {"href": "href", "result": "failed", "drift_detection": {"job": {"id": "id", "summary": {"version": "version", "plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "success_messages": ["success_messages"], "update_messages": ["update_messages"], "destroy_messages": ["destroy_messages"]}, "apply_messages": {"error_messages": [{}], "success_messages": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}}}, "outputs": [{"name": "name", "description": "description", "value": "anyValue"}], "project": {"id": "id", "href": "href", "definition": {"name": "name"}, "crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::"}, "references": {"anyKey": "anyValue"}, "schematics": {"workspace_crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::", "validate_pre_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "validate_post_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "deploy_pre_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "deploy_post_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "undeploy_pre_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "undeploy_post_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}}, "state": "approved", "update_available": true, "template": {"id": "id", "href": "href"}, "href": "href", "definition": {"compliance_profile": {"id": "id", "instance_id": "instance_id", "instance_location": "instance_location", "attachment_id": "attachment_id", "profile_name": "profile_name"}, "locator_id": "locator_id", "description": "description", "name": "name", "environment_id": "environment_id", "authorizations": {"trusted_profile_id": "trusted_profile_id", "method": "api_key", "api_key": "api_key"}, "inputs": {"anyKey": "anyValue"}, "settings": {"anyKey": "anyValue"}}}'
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
        mock_response = '{"id": "id", "version": 7, "is_draft": true, "needs_attention_state": [{"event_id": "event_id", "event": "event", "severity": "INFO", "action_url": "action_url", "target": "target", "triggered_by": "triggered_by", "timestamp": "timestamp"}], "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "last_approved": {"at": "2019-01-01T12:00:00.000Z", "comment": "comment", "is_forced": false, "user_id": "user_id"}, "last_saved_at": "2019-01-01T12:00:00.000Z", "last_validated": {"href": "href", "result": "failed", "job": {"id": "id", "summary": {"version": "version", "plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "success_messages": ["success_messages"], "update_messages": ["update_messages"], "destroy_messages": ["destroy_messages"]}, "apply_messages": {"error_messages": [{}], "success_messages": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}, "pre_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}, "post_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}, "cost_estimate": {"version": "version", "currency": "USD", "totalHourlyCost": "total_hourly_cost", "totalMonthlyCost": "total_monthly_cost", "pastTotalHourlyCost": "past_total_hourly_cost", "pastTotalMonthlyCost": "past_total_monthly_cost", "diffTotalHourlyCost": "diff_total_hourly_cost", "diffTotalMonthlyCost": "diff_total_monthly_cost", "timeGenerated": "2019-01-01T12:00:00.000Z", "user_id": "user_id"}, "cra_logs": {"cra_version": "2.0.4", "schema_version": "schema_version", "status": "passed", "summary": {"total": "total", "passed": "passed", "failed": "failed", "skipped": "skipped"}, "timestamp": "2019-01-01T12:00:00.000Z"}}, "last_deployed": {"href": "href", "result": "failed", "job": {"id": "id", "summary": {"version": "version", "plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "success_messages": ["success_messages"], "update_messages": ["update_messages"], "destroy_messages": ["destroy_messages"]}, "apply_messages": {"error_messages": [{}], "success_messages": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}, "pre_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}, "post_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}}, "last_undeployed": {"href": "href", "result": "failed", "job": {"id": "id", "summary": {"version": "version", "plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "success_messages": ["success_messages"], "update_messages": ["update_messages"], "destroy_messages": ["destroy_messages"]}, "apply_messages": {"error_messages": [{}], "success_messages": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}, "pre_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}, "post_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}}, "last_monitoring": {"href": "href", "result": "failed", "drift_detection": {"job": {"id": "id", "summary": {"version": "version", "plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "success_messages": ["success_messages"], "update_messages": ["update_messages"], "destroy_messages": ["destroy_messages"]}, "apply_messages": {"error_messages": [{}], "success_messages": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}}}, "outputs": [{"name": "name", "description": "description", "value": "anyValue"}], "project": {"id": "id", "href": "href", "definition": {"name": "name"}, "crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::"}, "references": {"anyKey": "anyValue"}, "schematics": {"workspace_crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::", "validate_pre_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "validate_post_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "deploy_pre_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "deploy_post_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "undeploy_pre_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "undeploy_post_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}}, "state": "approved", "update_available": true, "template": {"id": "id", "href": "href"}, "href": "href", "definition": {"compliance_profile": {"id": "id", "instance_id": "instance_id", "instance_location": "instance_location", "attachment_id": "attachment_id", "profile_name": "profile_name"}, "locator_id": "locator_id", "description": "description", "name": "name", "environment_id": "environment_id", "authorizations": {"trusted_profile_id": "trusted_profile_id", "method": "api_key", "api_key": "api_key"}, "inputs": {"anyKey": "anyValue"}, "settings": {"anyKey": "anyValue"}}}'
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
        response = _service.undeploy_config(
            project_id,
            id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202

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
        mock_response = '{"id": "id", "version": 7, "is_draft": true, "needs_attention_state": [{"event_id": "event_id", "event": "event", "severity": "INFO", "action_url": "action_url", "target": "target", "triggered_by": "triggered_by", "timestamp": "timestamp"}], "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "last_approved": {"at": "2019-01-01T12:00:00.000Z", "comment": "comment", "is_forced": false, "user_id": "user_id"}, "last_saved_at": "2019-01-01T12:00:00.000Z", "last_validated": {"href": "href", "result": "failed", "job": {"id": "id", "summary": {"version": "version", "plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "success_messages": ["success_messages"], "update_messages": ["update_messages"], "destroy_messages": ["destroy_messages"]}, "apply_messages": {"error_messages": [{}], "success_messages": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}, "pre_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}, "post_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}, "cost_estimate": {"version": "version", "currency": "USD", "totalHourlyCost": "total_hourly_cost", "totalMonthlyCost": "total_monthly_cost", "pastTotalHourlyCost": "past_total_hourly_cost", "pastTotalMonthlyCost": "past_total_monthly_cost", "diffTotalHourlyCost": "diff_total_hourly_cost", "diffTotalMonthlyCost": "diff_total_monthly_cost", "timeGenerated": "2019-01-01T12:00:00.000Z", "user_id": "user_id"}, "cra_logs": {"cra_version": "2.0.4", "schema_version": "schema_version", "status": "passed", "summary": {"total": "total", "passed": "passed", "failed": "failed", "skipped": "skipped"}, "timestamp": "2019-01-01T12:00:00.000Z"}}, "last_deployed": {"href": "href", "result": "failed", "job": {"id": "id", "summary": {"version": "version", "plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "success_messages": ["success_messages"], "update_messages": ["update_messages"], "destroy_messages": ["destroy_messages"]}, "apply_messages": {"error_messages": [{}], "success_messages": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}, "pre_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}, "post_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}}, "last_undeployed": {"href": "href", "result": "failed", "job": {"id": "id", "summary": {"version": "version", "plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "success_messages": ["success_messages"], "update_messages": ["update_messages"], "destroy_messages": ["destroy_messages"]}, "apply_messages": {"error_messages": [{}], "success_messages": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}, "pre_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}, "post_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}}, "last_monitoring": {"href": "href", "result": "failed", "drift_detection": {"job": {"id": "id", "summary": {"version": "version", "plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "success_messages": ["success_messages"], "update_messages": ["update_messages"], "destroy_messages": ["destroy_messages"]}, "apply_messages": {"error_messages": [{}], "success_messages": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}}}, "outputs": [{"name": "name", "description": "description", "value": "anyValue"}], "project": {"id": "id", "href": "href", "definition": {"name": "name"}, "crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::"}, "references": {"anyKey": "anyValue"}, "schematics": {"workspace_crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::", "validate_pre_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "validate_post_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "deploy_pre_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "deploy_post_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "undeploy_pre_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "undeploy_post_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}}, "state": "approved", "update_available": true, "template": {"id": "id", "href": "href"}, "href": "href", "definition": {"compliance_profile": {"id": "id", "instance_id": "instance_id", "instance_location": "instance_location", "attachment_id": "attachment_id", "profile_name": "profile_name"}, "locator_id": "locator_id", "description": "description", "name": "name", "environment_id": "environment_id", "authorizations": {"trusted_profile_id": "trusted_profile_id", "method": "api_key", "api_key": "api_key"}, "inputs": {"anyKey": "anyValue"}, "settings": {"anyKey": "anyValue"}}}'
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
        schematics_workspace_model['workspace_crn'] = (
            'crn:v1:staging:public:schematics:us-south:a/38acaf4469814090a4e675dc0c317a0d:95ad49de-ab96-4e7d-a08c-45c38aa448e6:workspace:us-south.workspace.service.e0106139'
        )

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


class TestCreateStackDefinition:
    """
    Test Class for create_stack_definition
    """

    @responses.activate
    def test_create_stack_definition_all_params(self):
        """
        create_stack_definition()
        """
        # Set up mock
        url = preprocess_url('/v1/projects/testString/configs/testString/stack_definition')
        mock_response = '{"id": "id", "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "state": "draft", "configuration": {"id": "id", "href": "href", "definition": {"name": "name"}}, "href": "href", "stack_definition": {"inputs": [{"name": "name", "type": "array", "description": "description", "default": "anyValue", "required": true, "hidden": true}], "outputs": [{"name": "name", "value": "anyValue"}], "members": [{"name": "name", "version_locator": "version_locator", "inputs": [{"name": "name", "value": "anyValue"}]}]}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a StackDefinitionInputVariable model
        stack_definition_input_variable_model = {}
        stack_definition_input_variable_model['name'] = 'region'
        stack_definition_input_variable_model['type'] = 'string'
        stack_definition_input_variable_model['description'] = 'testString'
        stack_definition_input_variable_model['default'] = 'us-south'
        stack_definition_input_variable_model['required'] = True
        stack_definition_input_variable_model['hidden'] = False

        # Construct a dict representation of a StackDefinitionOutputVariable model
        stack_definition_output_variable_model = {}
        stack_definition_output_variable_model['name'] = 'vpc_cluster_id'
        stack_definition_output_variable_model['value'] = 'cluster_id'

        # Construct a dict representation of a StackDefinitionMemberInputPrototype model
        stack_definition_member_input_prototype_model = {}
        stack_definition_member_input_prototype_model['name'] = 'region'

        # Construct a dict representation of a StackDefinitionMemberPrototype model
        stack_definition_member_prototype_model = {}
        stack_definition_member_prototype_model['name'] = 'foundation-deployable-architecture'
        stack_definition_member_prototype_model['inputs'] = [stack_definition_member_input_prototype_model]

        # Construct a dict representation of a StackDefinitionBlockPrototype model
        stack_definition_block_prototype_model = {}
        stack_definition_block_prototype_model['inputs'] = [stack_definition_input_variable_model]
        stack_definition_block_prototype_model['outputs'] = [stack_definition_output_variable_model]
        stack_definition_block_prototype_model['members'] = [stack_definition_member_prototype_model]

        # Set up parameter values
        project_id = 'testString'
        id = 'testString'
        stack_definition = stack_definition_block_prototype_model

        # Invoke method
        response = _service.create_stack_definition(
            project_id,
            id,
            stack_definition,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['stack_definition'] == stack_definition_block_prototype_model

    def test_create_stack_definition_all_params_with_retries(self):
        # Enable retries and run test_create_stack_definition_all_params.
        _service.enable_retries()
        self.test_create_stack_definition_all_params()

        # Disable retries and run test_create_stack_definition_all_params.
        _service.disable_retries()
        self.test_create_stack_definition_all_params()

    @responses.activate
    def test_create_stack_definition_value_error(self):
        """
        test_create_stack_definition_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/projects/testString/configs/testString/stack_definition')
        mock_response = '{"id": "id", "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "state": "draft", "configuration": {"id": "id", "href": "href", "definition": {"name": "name"}}, "href": "href", "stack_definition": {"inputs": [{"name": "name", "type": "array", "description": "description", "default": "anyValue", "required": true, "hidden": true}], "outputs": [{"name": "name", "value": "anyValue"}], "members": [{"name": "name", "version_locator": "version_locator", "inputs": [{"name": "name", "value": "anyValue"}]}]}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a StackDefinitionInputVariable model
        stack_definition_input_variable_model = {}
        stack_definition_input_variable_model['name'] = 'region'
        stack_definition_input_variable_model['type'] = 'string'
        stack_definition_input_variable_model['description'] = 'testString'
        stack_definition_input_variable_model['default'] = 'us-south'
        stack_definition_input_variable_model['required'] = True
        stack_definition_input_variable_model['hidden'] = False

        # Construct a dict representation of a StackDefinitionOutputVariable model
        stack_definition_output_variable_model = {}
        stack_definition_output_variable_model['name'] = 'vpc_cluster_id'
        stack_definition_output_variable_model['value'] = 'cluster_id'

        # Construct a dict representation of a StackDefinitionMemberInputPrototype model
        stack_definition_member_input_prototype_model = {}
        stack_definition_member_input_prototype_model['name'] = 'region'

        # Construct a dict representation of a StackDefinitionMemberPrototype model
        stack_definition_member_prototype_model = {}
        stack_definition_member_prototype_model['name'] = 'foundation-deployable-architecture'
        stack_definition_member_prototype_model['inputs'] = [stack_definition_member_input_prototype_model]

        # Construct a dict representation of a StackDefinitionBlockPrototype model
        stack_definition_block_prototype_model = {}
        stack_definition_block_prototype_model['inputs'] = [stack_definition_input_variable_model]
        stack_definition_block_prototype_model['outputs'] = [stack_definition_output_variable_model]
        stack_definition_block_prototype_model['members'] = [stack_definition_member_prototype_model]

        # Set up parameter values
        project_id = 'testString'
        id = 'testString'
        stack_definition = stack_definition_block_prototype_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "id": id,
            "stack_definition": stack_definition,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_stack_definition(**req_copy)

    def test_create_stack_definition_value_error_with_retries(self):
        # Enable retries and run test_create_stack_definition_value_error.
        _service.enable_retries()
        self.test_create_stack_definition_value_error()

        # Disable retries and run test_create_stack_definition_value_error.
        _service.disable_retries()
        self.test_create_stack_definition_value_error()


class TestGetStackDefinition:
    """
    Test Class for get_stack_definition
    """

    @responses.activate
    def test_get_stack_definition_all_params(self):
        """
        get_stack_definition()
        """
        # Set up mock
        url = preprocess_url('/v1/projects/testString/configs/testString/stack_definition')
        mock_response = '{"id": "id", "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "state": "draft", "configuration": {"id": "id", "href": "href", "definition": {"name": "name"}}, "href": "href", "stack_definition": {"inputs": [{"name": "name", "type": "array", "description": "description", "default": "anyValue", "required": true, "hidden": true}], "outputs": [{"name": "name", "value": "anyValue"}], "members": [{"name": "name", "version_locator": "version_locator", "inputs": [{"name": "name", "value": "anyValue"}]}]}}'
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
        response = _service.get_stack_definition(
            project_id,
            id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_stack_definition_all_params_with_retries(self):
        # Enable retries and run test_get_stack_definition_all_params.
        _service.enable_retries()
        self.test_get_stack_definition_all_params()

        # Disable retries and run test_get_stack_definition_all_params.
        _service.disable_retries()
        self.test_get_stack_definition_all_params()

    @responses.activate
    def test_get_stack_definition_value_error(self):
        """
        test_get_stack_definition_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/projects/testString/configs/testString/stack_definition')
        mock_response = '{"id": "id", "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "state": "draft", "configuration": {"id": "id", "href": "href", "definition": {"name": "name"}}, "href": "href", "stack_definition": {"inputs": [{"name": "name", "type": "array", "description": "description", "default": "anyValue", "required": true, "hidden": true}], "outputs": [{"name": "name", "value": "anyValue"}], "members": [{"name": "name", "version_locator": "version_locator", "inputs": [{"name": "name", "value": "anyValue"}]}]}}'
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
                _service.get_stack_definition(**req_copy)

    def test_get_stack_definition_value_error_with_retries(self):
        # Enable retries and run test_get_stack_definition_value_error.
        _service.enable_retries()
        self.test_get_stack_definition_value_error()

        # Disable retries and run test_get_stack_definition_value_error.
        _service.disable_retries()
        self.test_get_stack_definition_value_error()


class TestUpdateStackDefinition:
    """
    Test Class for update_stack_definition
    """

    @responses.activate
    def test_update_stack_definition_all_params(self):
        """
        update_stack_definition()
        """
        # Set up mock
        url = preprocess_url('/v1/projects/testString/configs/testString/stack_definition')
        mock_response = '{"id": "id", "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "state": "draft", "configuration": {"id": "id", "href": "href", "definition": {"name": "name"}}, "href": "href", "stack_definition": {"inputs": [{"name": "name", "type": "array", "description": "description", "default": "anyValue", "required": true, "hidden": true}], "outputs": [{"name": "name", "value": "anyValue"}], "members": [{"name": "name", "version_locator": "version_locator", "inputs": [{"name": "name", "value": "anyValue"}]}]}}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a StackDefinitionInputVariable model
        stack_definition_input_variable_model = {}
        stack_definition_input_variable_model['name'] = 'region'
        stack_definition_input_variable_model['type'] = 'string'
        stack_definition_input_variable_model['description'] = 'testString'
        stack_definition_input_variable_model['default'] = 'eu-gb'
        stack_definition_input_variable_model['required'] = True
        stack_definition_input_variable_model['hidden'] = False

        # Construct a dict representation of a StackDefinitionOutputVariable model
        stack_definition_output_variable_model = {}
        stack_definition_output_variable_model['name'] = 'testString'
        stack_definition_output_variable_model['value'] = 'testString'

        # Construct a dict representation of a StackDefinitionMemberInputPrototype model
        stack_definition_member_input_prototype_model = {}
        stack_definition_member_input_prototype_model['name'] = 'cluster_name'

        # Construct a dict representation of a StackDefinitionMemberPrototype model
        stack_definition_member_prototype_model = {}
        stack_definition_member_prototype_model['name'] = 'foundation-deployable-architecture'
        stack_definition_member_prototype_model['inputs'] = [stack_definition_member_input_prototype_model]

        # Construct a dict representation of a StackDefinitionBlockPrototype model
        stack_definition_block_prototype_model = {}
        stack_definition_block_prototype_model['inputs'] = [stack_definition_input_variable_model]
        stack_definition_block_prototype_model['outputs'] = [stack_definition_output_variable_model]
        stack_definition_block_prototype_model['members'] = [stack_definition_member_prototype_model]

        # Set up parameter values
        project_id = 'testString'
        id = 'testString'
        stack_definition = stack_definition_block_prototype_model

        # Invoke method
        response = _service.update_stack_definition(
            project_id,
            id,
            stack_definition,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['stack_definition'] == stack_definition_block_prototype_model

    def test_update_stack_definition_all_params_with_retries(self):
        # Enable retries and run test_update_stack_definition_all_params.
        _service.enable_retries()
        self.test_update_stack_definition_all_params()

        # Disable retries and run test_update_stack_definition_all_params.
        _service.disable_retries()
        self.test_update_stack_definition_all_params()

    @responses.activate
    def test_update_stack_definition_value_error(self):
        """
        test_update_stack_definition_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/projects/testString/configs/testString/stack_definition')
        mock_response = '{"id": "id", "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "state": "draft", "configuration": {"id": "id", "href": "href", "definition": {"name": "name"}}, "href": "href", "stack_definition": {"inputs": [{"name": "name", "type": "array", "description": "description", "default": "anyValue", "required": true, "hidden": true}], "outputs": [{"name": "name", "value": "anyValue"}], "members": [{"name": "name", "version_locator": "version_locator", "inputs": [{"name": "name", "value": "anyValue"}]}]}}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a StackDefinitionInputVariable model
        stack_definition_input_variable_model = {}
        stack_definition_input_variable_model['name'] = 'region'
        stack_definition_input_variable_model['type'] = 'string'
        stack_definition_input_variable_model['description'] = 'testString'
        stack_definition_input_variable_model['default'] = 'eu-gb'
        stack_definition_input_variable_model['required'] = True
        stack_definition_input_variable_model['hidden'] = False

        # Construct a dict representation of a StackDefinitionOutputVariable model
        stack_definition_output_variable_model = {}
        stack_definition_output_variable_model['name'] = 'testString'
        stack_definition_output_variable_model['value'] = 'testString'

        # Construct a dict representation of a StackDefinitionMemberInputPrototype model
        stack_definition_member_input_prototype_model = {}
        stack_definition_member_input_prototype_model['name'] = 'cluster_name'

        # Construct a dict representation of a StackDefinitionMemberPrototype model
        stack_definition_member_prototype_model = {}
        stack_definition_member_prototype_model['name'] = 'foundation-deployable-architecture'
        stack_definition_member_prototype_model['inputs'] = [stack_definition_member_input_prototype_model]

        # Construct a dict representation of a StackDefinitionBlockPrototype model
        stack_definition_block_prototype_model = {}
        stack_definition_block_prototype_model['inputs'] = [stack_definition_input_variable_model]
        stack_definition_block_prototype_model['outputs'] = [stack_definition_output_variable_model]
        stack_definition_block_prototype_model['members'] = [stack_definition_member_prototype_model]

        # Set up parameter values
        project_id = 'testString'
        id = 'testString'
        stack_definition = stack_definition_block_prototype_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "id": id,
            "stack_definition": stack_definition,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_stack_definition(**req_copy)

    def test_update_stack_definition_value_error_with_retries(self):
        # Enable retries and run test_update_stack_definition_value_error.
        _service.enable_retries()
        self.test_update_stack_definition_value_error()

        # Disable retries and run test_update_stack_definition_value_error.
        _service.disable_retries()
        self.test_update_stack_definition_value_error()


class TestExportStackDefinition:
    """
    Test Class for export_stack_definition
    """

    @responses.activate
    def test_export_stack_definition_all_params(self):
        """
        export_stack_definition()
        """
        # Set up mock
        url = preprocess_url('/v1/projects/testString/configs/testString/stack_definition/export')
        mock_response = '{"catalog_id": "catalog_id", "product_id": "product_id", "version_locator": "version_locator", "kind": "kind", "format": "format"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a StackDefinitionExportRequestStackDefinitionExportCatalogRequest model
        stack_definition_export_request_model = {}
        stack_definition_export_request_model['catalog_id'] = '01e1a9ad-534b-4ab9-996a-b8f2a8653d5c'
        stack_definition_export_request_model['target_version'] = 'testString'
        stack_definition_export_request_model['variation'] = 'testString'
        stack_definition_export_request_model['label'] = 'Stack Deployable Architecture'
        stack_definition_export_request_model['tags'] = ['testString']

        # Set up parameter values
        project_id = 'testString'
        id = 'testString'
        settings = stack_definition_export_request_model

        # Invoke method
        response = _service.export_stack_definition(
            project_id,
            id,
            settings,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == settings

    def test_export_stack_definition_all_params_with_retries(self):
        # Enable retries and run test_export_stack_definition_all_params.
        _service.enable_retries()
        self.test_export_stack_definition_all_params()

        # Disable retries and run test_export_stack_definition_all_params.
        _service.disable_retries()
        self.test_export_stack_definition_all_params()

    @responses.activate
    def test_export_stack_definition_value_error(self):
        """
        test_export_stack_definition_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/projects/testString/configs/testString/stack_definition/export')
        mock_response = '{"catalog_id": "catalog_id", "product_id": "product_id", "version_locator": "version_locator", "kind": "kind", "format": "format"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a StackDefinitionExportRequestStackDefinitionExportCatalogRequest model
        stack_definition_export_request_model = {}
        stack_definition_export_request_model['catalog_id'] = '01e1a9ad-534b-4ab9-996a-b8f2a8653d5c'
        stack_definition_export_request_model['target_version'] = 'testString'
        stack_definition_export_request_model['variation'] = 'testString'
        stack_definition_export_request_model['label'] = 'Stack Deployable Architecture'
        stack_definition_export_request_model['tags'] = ['testString']

        # Set up parameter values
        project_id = 'testString'
        id = 'testString'
        settings = stack_definition_export_request_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "id": id,
            "settings": settings,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.export_stack_definition(**req_copy)

    def test_export_stack_definition_value_error_with_retries(self):
        # Enable retries and run test_export_stack_definition_value_error.
        _service.enable_retries()
        self.test_export_stack_definition_value_error()

        # Disable retries and run test_export_stack_definition_value_error.
        _service.disable_retries()
        self.test_export_stack_definition_value_error()


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
        mock_response = '{"versions": [{"definition": {"environment_id": "environment_id", "locator_id": "locator_id"}, "state": "approved", "version": 7, "href": "href"}]}'
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
        mock_response = '{"versions": [{"definition": {"environment_id": "environment_id", "locator_id": "locator_id"}, "state": "approved", "version": 7, "href": "href"}]}'
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
        mock_response = '{"id": "id", "version": 7, "is_draft": true, "needs_attention_state": [{"event_id": "event_id", "event": "event", "severity": "INFO", "action_url": "action_url", "target": "target", "triggered_by": "triggered_by", "timestamp": "timestamp"}], "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "last_approved": {"at": "2019-01-01T12:00:00.000Z", "comment": "comment", "is_forced": false, "user_id": "user_id"}, "last_saved_at": "2019-01-01T12:00:00.000Z", "last_validated": {"href": "href", "result": "failed", "job": {"id": "id", "summary": {"version": "version", "plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "success_messages": ["success_messages"], "update_messages": ["update_messages"], "destroy_messages": ["destroy_messages"]}, "apply_messages": {"error_messages": [{}], "success_messages": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}, "pre_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}, "post_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}, "cost_estimate": {"version": "version", "currency": "USD", "totalHourlyCost": "total_hourly_cost", "totalMonthlyCost": "total_monthly_cost", "pastTotalHourlyCost": "past_total_hourly_cost", "pastTotalMonthlyCost": "past_total_monthly_cost", "diffTotalHourlyCost": "diff_total_hourly_cost", "diffTotalMonthlyCost": "diff_total_monthly_cost", "timeGenerated": "2019-01-01T12:00:00.000Z", "user_id": "user_id"}, "cra_logs": {"cra_version": "2.0.4", "schema_version": "schema_version", "status": "passed", "summary": {"total": "total", "passed": "passed", "failed": "failed", "skipped": "skipped"}, "timestamp": "2019-01-01T12:00:00.000Z"}}, "last_deployed": {"href": "href", "result": "failed", "job": {"id": "id", "summary": {"version": "version", "plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "success_messages": ["success_messages"], "update_messages": ["update_messages"], "destroy_messages": ["destroy_messages"]}, "apply_messages": {"error_messages": [{}], "success_messages": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}, "pre_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}, "post_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}}, "last_undeployed": {"href": "href", "result": "failed", "job": {"id": "id", "summary": {"version": "version", "plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "success_messages": ["success_messages"], "update_messages": ["update_messages"], "destroy_messages": ["destroy_messages"]}, "apply_messages": {"error_messages": [{}], "success_messages": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}, "pre_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}, "post_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}}, "last_monitoring": {"href": "href", "result": "failed", "drift_detection": {"job": {"id": "id", "summary": {"version": "version", "plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "success_messages": ["success_messages"], "update_messages": ["update_messages"], "destroy_messages": ["destroy_messages"]}, "apply_messages": {"error_messages": [{}], "success_messages": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}}}, "outputs": [{"name": "name", "description": "description", "value": "anyValue"}], "project": {"id": "id", "href": "href", "definition": {"name": "name"}, "crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::"}, "references": {"anyKey": "anyValue"}, "schematics": {"workspace_crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::", "validate_pre_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "validate_post_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "deploy_pre_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "deploy_post_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "undeploy_pre_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "undeploy_post_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}}, "state": "approved", "update_available": true, "template": {"id": "id", "href": "href"}, "href": "href", "definition": {"compliance_profile": {"id": "id", "instance_id": "instance_id", "instance_location": "instance_location", "attachment_id": "attachment_id", "profile_name": "profile_name"}, "locator_id": "locator_id", "description": "description", "name": "name", "environment_id": "environment_id", "authorizations": {"trusted_profile_id": "trusted_profile_id", "method": "api_key", "api_key": "api_key"}, "inputs": {"anyKey": "anyValue"}, "settings": {"anyKey": "anyValue"}}}'
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
        mock_response = '{"id": "id", "version": 7, "is_draft": true, "needs_attention_state": [{"event_id": "event_id", "event": "event", "severity": "INFO", "action_url": "action_url", "target": "target", "triggered_by": "triggered_by", "timestamp": "timestamp"}], "created_at": "2019-01-01T12:00:00.000Z", "modified_at": "2019-01-01T12:00:00.000Z", "last_approved": {"at": "2019-01-01T12:00:00.000Z", "comment": "comment", "is_forced": false, "user_id": "user_id"}, "last_saved_at": "2019-01-01T12:00:00.000Z", "last_validated": {"href": "href", "result": "failed", "job": {"id": "id", "summary": {"version": "version", "plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "success_messages": ["success_messages"], "update_messages": ["update_messages"], "destroy_messages": ["destroy_messages"]}, "apply_messages": {"error_messages": [{}], "success_messages": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}, "pre_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}, "post_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}, "cost_estimate": {"version": "version", "currency": "USD", "totalHourlyCost": "total_hourly_cost", "totalMonthlyCost": "total_monthly_cost", "pastTotalHourlyCost": "past_total_hourly_cost", "pastTotalMonthlyCost": "past_total_monthly_cost", "diffTotalHourlyCost": "diff_total_hourly_cost", "diffTotalMonthlyCost": "diff_total_monthly_cost", "timeGenerated": "2019-01-01T12:00:00.000Z", "user_id": "user_id"}, "cra_logs": {"cra_version": "2.0.4", "schema_version": "schema_version", "status": "passed", "summary": {"total": "total", "passed": "passed", "failed": "failed", "skipped": "skipped"}, "timestamp": "2019-01-01T12:00:00.000Z"}}, "last_deployed": {"href": "href", "result": "failed", "job": {"id": "id", "summary": {"version": "version", "plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "success_messages": ["success_messages"], "update_messages": ["update_messages"], "destroy_messages": ["destroy_messages"]}, "apply_messages": {"error_messages": [{}], "success_messages": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}, "pre_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}, "post_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}}, "last_undeployed": {"href": "href", "result": "failed", "job": {"id": "id", "summary": {"version": "version", "plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "success_messages": ["success_messages"], "update_messages": ["update_messages"], "destroy_messages": ["destroy_messages"]}, "apply_messages": {"error_messages": [{}], "success_messages": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}, "pre_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}, "post_job": {"id": "id", "summary": {"job_id": "job_id", "start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "tasks": 5, "ok": 2, "failed": 6, "skipped": 7, "changed": 7, "project_error": {"timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id", "status_code": "status_code", "description": "description", "error_response": "error_response"}}}}, "last_monitoring": {"href": "href", "result": "failed", "drift_detection": {"job": {"id": "id", "summary": {"version": "version", "plan_summary": {"add": 3, "failed": 6, "update": 6, "destroy": 7, "add_resources": ["add_resources"], "failed_resources": ["failed_resources"], "updated_resources": ["updated_resources"], "destroy_resources": ["destroy_resources"]}, "apply_summary": {"success": 7, "failed": 6, "success_resources": ["success_resources"], "failed_resources": ["failed_resources"]}, "destroy_summary": {"success": 7, "failed": 6, "tainted": 7, "resources": {"success": ["success"], "failed": ["failed"], "tainted": ["tainted"]}}, "message_summary": {"info": 4, "debug": 5, "error": 5}, "plan_messages": {"error_messages": [{}], "success_messages": ["success_messages"], "update_messages": ["update_messages"], "destroy_messages": ["destroy_messages"]}, "apply_messages": {"error_messages": [{}], "success_messages": [{"resource_type": "resource_type", "time-taken": "time_taken", "id": "id"}]}, "destroy_messages": {"error_messages": [{}]}}}}}, "outputs": [{"name": "name", "description": "description", "value": "anyValue"}], "project": {"id": "id", "href": "href", "definition": {"name": "name"}, "crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::"}, "references": {"anyKey": "anyValue"}, "schematics": {"workspace_crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::", "validate_pre_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "validate_post_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "deploy_pre_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "deploy_post_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "undeploy_pre_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}, "undeploy_post_script": {"type": "ansible", "path": "scripts/validate-post-ansible-playbook.yaml", "short_description": "short_description"}}, "state": "approved", "update_available": true, "template": {"id": "id", "href": "href"}, "href": "href", "definition": {"compliance_profile": {"id": "id", "instance_id": "instance_id", "instance_location": "instance_location", "attachment_id": "attachment_id", "profile_name": "profile_name"}, "locator_id": "locator_id", "description": "description", "name": "name", "environment_id": "environment_id", "authorizations": {"trusted_profile_id": "trusted_profile_id", "method": "api_key", "api_key": "api_key"}, "inputs": {"anyKey": "anyValue"}, "settings": {"anyKey": "anyValue"}}}'
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
        action_job_apply_messages_summary_model_json['success_messages'] = [
            terraform_log_analyzer_success_message_model
        ]

        # Construct a model instance of ActionJobApplyMessagesSummary by calling from_dict on the json representation
        action_job_apply_messages_summary_model = ActionJobApplyMessagesSummary.from_dict(
            action_job_apply_messages_summary_model_json
        )
        assert action_job_apply_messages_summary_model != False

        # Construct a model instance of ActionJobApplyMessagesSummary by calling from_dict on the json representation
        action_job_apply_messages_summary_model_dict = ActionJobApplyMessagesSummary.from_dict(
            action_job_apply_messages_summary_model_json
        ).__dict__
        action_job_apply_messages_summary_model2 = ActionJobApplyMessagesSummary(
            **action_job_apply_messages_summary_model_dict
        )

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
        action_job_apply_summary_model_dict = ActionJobApplySummary.from_dict(
            action_job_apply_summary_model_json
        ).__dict__
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
        action_job_destroy_messages_summary_model = ActionJobDestroyMessagesSummary.from_dict(
            action_job_destroy_messages_summary_model_json
        )
        assert action_job_destroy_messages_summary_model != False

        # Construct a model instance of ActionJobDestroyMessagesSummary by calling from_dict on the json representation
        action_job_destroy_messages_summary_model_dict = ActionJobDestroyMessagesSummary.from_dict(
            action_job_destroy_messages_summary_model_json
        ).__dict__
        action_job_destroy_messages_summary_model2 = ActionJobDestroyMessagesSummary(
            **action_job_destroy_messages_summary_model_dict
        )

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
        action_job_destroy_summary_model_dict = ActionJobDestroySummary.from_dict(
            action_job_destroy_summary_model_json
        ).__dict__
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
        action_job_destroy_summary_resources_model = ActionJobDestroySummaryResources.from_dict(
            action_job_destroy_summary_resources_model_json
        )
        assert action_job_destroy_summary_resources_model != False

        # Construct a model instance of ActionJobDestroySummaryResources by calling from_dict on the json representation
        action_job_destroy_summary_resources_model_dict = ActionJobDestroySummaryResources.from_dict(
            action_job_destroy_summary_resources_model_json
        ).__dict__
        action_job_destroy_summary_resources_model2 = ActionJobDestroySummaryResources(
            **action_job_destroy_summary_resources_model_dict
        )

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
        action_job_message_summary_model_dict = ActionJobMessageSummary.from_dict(
            action_job_message_summary_model_json
        ).__dict__
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
        action_job_plan_messages_summary_model_json['success_messages'] = ['testString']
        action_job_plan_messages_summary_model_json['update_messages'] = ['testString']
        action_job_plan_messages_summary_model_json['destroy_messages'] = ['testString']

        # Construct a model instance of ActionJobPlanMessagesSummary by calling from_dict on the json representation
        action_job_plan_messages_summary_model = ActionJobPlanMessagesSummary.from_dict(
            action_job_plan_messages_summary_model_json
        )
        assert action_job_plan_messages_summary_model != False

        # Construct a model instance of ActionJobPlanMessagesSummary by calling from_dict on the json representation
        action_job_plan_messages_summary_model_dict = ActionJobPlanMessagesSummary.from_dict(
            action_job_plan_messages_summary_model_json
        ).__dict__
        action_job_plan_messages_summary_model2 = ActionJobPlanMessagesSummary(
            **action_job_plan_messages_summary_model_dict
        )

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
        action_job_plan_messages_summary_model['success_messages'] = ['testString']
        action_job_plan_messages_summary_model['update_messages'] = ['testString']
        action_job_plan_messages_summary_model['destroy_messages'] = ['testString']

        terraform_log_analyzer_success_message_model = {}  # TerraformLogAnalyzerSuccessMessage
        terraform_log_analyzer_success_message_model['resource_type'] = 'testString'
        terraform_log_analyzer_success_message_model['time-taken'] = 'testString'
        terraform_log_analyzer_success_message_model['id'] = 'testString'

        action_job_apply_messages_summary_model = {}  # ActionJobApplyMessagesSummary
        action_job_apply_messages_summary_model['error_messages'] = [terraform_log_analyzer_error_message_model]
        action_job_apply_messages_summary_model['success_messages'] = [terraform_log_analyzer_success_message_model]

        action_job_destroy_messages_summary_model = {}  # ActionJobDestroyMessagesSummary
        action_job_destroy_messages_summary_model['error_messages'] = [terraform_log_analyzer_error_message_model]

        # Construct a json representation of a ActionJobSummary model
        action_job_summary_model_json = {}
        action_job_summary_model_json['version'] = 'testString'
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
        action_job_plan_messages_summary_model['success_messages'] = ['testString']
        action_job_plan_messages_summary_model['update_messages'] = ['testString']
        action_job_plan_messages_summary_model['destroy_messages'] = ['testString']

        terraform_log_analyzer_success_message_model = {}  # TerraformLogAnalyzerSuccessMessage
        terraform_log_analyzer_success_message_model['resource_type'] = 'testString'
        terraform_log_analyzer_success_message_model['time-taken'] = 'testString'
        terraform_log_analyzer_success_message_model['id'] = 'testString'

        action_job_apply_messages_summary_model = {}  # ActionJobApplyMessagesSummary
        action_job_apply_messages_summary_model['error_messages'] = [terraform_log_analyzer_error_message_model]
        action_job_apply_messages_summary_model['success_messages'] = [terraform_log_analyzer_success_message_model]

        action_job_destroy_messages_summary_model = {}  # ActionJobDestroyMessagesSummary
        action_job_destroy_messages_summary_model['error_messages'] = [terraform_log_analyzer_error_message_model]

        action_job_summary_model = {}  # ActionJobSummary
        action_job_summary_model['version'] = 'testString'
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
        action_job_with_id_and_summary_model = ActionJobWithIdAndSummary.from_dict(
            action_job_with_id_and_summary_model_json
        )
        assert action_job_with_id_and_summary_model != False

        # Construct a model instance of ActionJobWithIdAndSummary by calling from_dict on the json representation
        action_job_with_id_and_summary_model_dict = ActionJobWithIdAndSummary.from_dict(
            action_job_with_id_and_summary_model_json
        ).__dict__
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
        code_risk_analyzer_logs_summary_model = CodeRiskAnalyzerLogsSummary.from_dict(
            code_risk_analyzer_logs_summary_model_json
        )
        assert code_risk_analyzer_logs_summary_model != False

        # Construct a model instance of CodeRiskAnalyzerLogsSummary by calling from_dict on the json representation
        code_risk_analyzer_logs_summary_model_dict = CodeRiskAnalyzerLogsSummary.from_dict(
            code_risk_analyzer_logs_summary_model_json
        ).__dict__
        code_risk_analyzer_logs_summary_model2 = CodeRiskAnalyzerLogsSummary(
            **code_risk_analyzer_logs_summary_model_dict
        )

        # Verify the model instances are equivalent
        assert code_risk_analyzer_logs_summary_model == code_risk_analyzer_logs_summary_model2

        # Convert model instance back to dict and verify no loss of data
        code_risk_analyzer_logs_summary_model_json2 = code_risk_analyzer_logs_summary_model.to_dict()
        assert code_risk_analyzer_logs_summary_model_json2 == code_risk_analyzer_logs_summary_model_json


class TestModel_ConfigDefinitionReference:
    """
    Test Class for ConfigDefinitionReference
    """

    def test_config_definition_reference_serialization(self):
        """
        Test serialization/deserialization for ConfigDefinitionReference
        """

        # Construct a json representation of a ConfigDefinitionReference model
        config_definition_reference_model_json = {}
        config_definition_reference_model_json['name'] = 'testString'

        # Construct a model instance of ConfigDefinitionReference by calling from_dict on the json representation
        config_definition_reference_model = ConfigDefinitionReference.from_dict(config_definition_reference_model_json)
        assert config_definition_reference_model != False

        # Construct a model instance of ConfigDefinitionReference by calling from_dict on the json representation
        config_definition_reference_model_dict = ConfigDefinitionReference.from_dict(
            config_definition_reference_model_json
        ).__dict__
        config_definition_reference_model2 = ConfigDefinitionReference(**config_definition_reference_model_dict)

        # Verify the model instances are equivalent
        assert config_definition_reference_model == config_definition_reference_model2

        # Convert model instance back to dict and verify no loss of data
        config_definition_reference_model_json2 = config_definition_reference_model.to_dict()
        assert config_definition_reference_model_json2 == config_definition_reference_model_json


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
        cumulative_needs_attention_model_dict = CumulativeNeedsAttention.from_dict(
            cumulative_needs_attention_model_json
        ).__dict__
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
        project_reference_model['href'] = 'testString'
        project_reference_model['definition'] = project_definition_reference_model
        project_reference_model['crn'] = (
            'crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::'
        )

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

        environment_definition_required_properties_response_model = (
            {}
        )  # EnvironmentDefinitionRequiredPropertiesResponse
        environment_definition_required_properties_response_model['description'] = 'testString'
        environment_definition_required_properties_response_model['name'] = 'testString'
        environment_definition_required_properties_response_model['authorizations'] = project_config_auth_model
        environment_definition_required_properties_response_model['inputs'] = {'anyKey': 'anyValue'}
        environment_definition_required_properties_response_model['compliance_profile'] = (
            project_compliance_profile_model
        )

        # Construct a json representation of a Environment model
        environment_model_json = {}
        environment_model_json['id'] = 'testString'
        environment_model_json['project'] = project_reference_model
        environment_model_json['created_at'] = '2019-01-01T12:00:00Z'
        environment_model_json['target_account'] = 'testString'
        environment_model_json['modified_at'] = '2019-01-01T12:00:00Z'
        environment_model_json['href'] = 'testString'
        environment_model_json['definition'] = environment_definition_required_properties_response_model

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

        pagination_link_model = {}  # PaginationLink
        pagination_link_model['href'] = 'testString'

        project_definition_reference_model = {}  # ProjectDefinitionReference
        project_definition_reference_model['name'] = 'testString'

        project_reference_model = {}  # ProjectReference
        project_reference_model['id'] = 'testString'
        project_reference_model['href'] = 'testString'
        project_reference_model['definition'] = project_definition_reference_model
        project_reference_model['crn'] = (
            'crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::'
        )

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

        environment_definition_required_properties_response_model = (
            {}
        )  # EnvironmentDefinitionRequiredPropertiesResponse
        environment_definition_required_properties_response_model['description'] = 'testString'
        environment_definition_required_properties_response_model['name'] = 'testString'
        environment_definition_required_properties_response_model['authorizations'] = project_config_auth_model
        environment_definition_required_properties_response_model['inputs'] = {'anyKey': 'anyValue'}
        environment_definition_required_properties_response_model['compliance_profile'] = (
            project_compliance_profile_model
        )

        environment_model = {}  # Environment
        environment_model['id'] = 'testString'
        environment_model['project'] = project_reference_model
        environment_model['created_at'] = '2019-01-01T12:00:00Z'
        environment_model['target_account'] = 'testString'
        environment_model['modified_at'] = '2019-01-01T12:00:00Z'
        environment_model['href'] = 'testString'
        environment_model['definition'] = environment_definition_required_properties_response_model

        # Construct a json representation of a EnvironmentCollection model
        environment_collection_model_json = {}
        environment_collection_model_json['limit'] = 10
        environment_collection_model_json['first'] = pagination_link_model
        environment_collection_model_json['next'] = pagination_link_model
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


class TestModel_EnvironmentDefinitionPropertiesPatch:
    """
    Test Class for EnvironmentDefinitionPropertiesPatch
    """

    def test_environment_definition_properties_patch_serialization(self):
        """
        Test serialization/deserialization for EnvironmentDefinitionPropertiesPatch
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

        # Construct a json representation of a EnvironmentDefinitionPropertiesPatch model
        environment_definition_properties_patch_model_json = {}
        environment_definition_properties_patch_model_json['description'] = 'testString'
        environment_definition_properties_patch_model_json['name'] = 'testString'
        environment_definition_properties_patch_model_json['authorizations'] = project_config_auth_model
        environment_definition_properties_patch_model_json['inputs'] = {'anyKey': 'anyValue'}
        environment_definition_properties_patch_model_json['compliance_profile'] = project_compliance_profile_model

        # Construct a model instance of EnvironmentDefinitionPropertiesPatch by calling from_dict on the json representation
        environment_definition_properties_patch_model = EnvironmentDefinitionPropertiesPatch.from_dict(
            environment_definition_properties_patch_model_json
        )
        assert environment_definition_properties_patch_model != False

        # Construct a model instance of EnvironmentDefinitionPropertiesPatch by calling from_dict on the json representation
        environment_definition_properties_patch_model_dict = EnvironmentDefinitionPropertiesPatch.from_dict(
            environment_definition_properties_patch_model_json
        ).__dict__
        environment_definition_properties_patch_model2 = EnvironmentDefinitionPropertiesPatch(
            **environment_definition_properties_patch_model_dict
        )

        # Verify the model instances are equivalent
        assert environment_definition_properties_patch_model == environment_definition_properties_patch_model2

        # Convert model instance back to dict and verify no loss of data
        environment_definition_properties_patch_model_json2 = environment_definition_properties_patch_model.to_dict()
        assert environment_definition_properties_patch_model_json2 == environment_definition_properties_patch_model_json


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

        project_compliance_profile_model = {}  # ProjectComplianceProfile
        project_compliance_profile_model['id'] = 'testString'
        project_compliance_profile_model['instance_id'] = 'testString'
        project_compliance_profile_model['instance_location'] = 'testString'
        project_compliance_profile_model['attachment_id'] = 'testString'
        project_compliance_profile_model['profile_name'] = 'testString'

        # Construct a json representation of a EnvironmentDefinitionRequiredProperties model
        environment_definition_required_properties_model_json = {}
        environment_definition_required_properties_model_json['description'] = 'testString'
        environment_definition_required_properties_model_json['name'] = 'testString'
        environment_definition_required_properties_model_json['authorizations'] = project_config_auth_model
        environment_definition_required_properties_model_json['inputs'] = {'anyKey': 'anyValue'}
        environment_definition_required_properties_model_json['compliance_profile'] = project_compliance_profile_model

        # Construct a model instance of EnvironmentDefinitionRequiredProperties by calling from_dict on the json representation
        environment_definition_required_properties_model = EnvironmentDefinitionRequiredProperties.from_dict(
            environment_definition_required_properties_model_json
        )
        assert environment_definition_required_properties_model != False

        # Construct a model instance of EnvironmentDefinitionRequiredProperties by calling from_dict on the json representation
        environment_definition_required_properties_model_dict = EnvironmentDefinitionRequiredProperties.from_dict(
            environment_definition_required_properties_model_json
        ).__dict__
        environment_definition_required_properties_model2 = EnvironmentDefinitionRequiredProperties(
            **environment_definition_required_properties_model_dict
        )

        # Verify the model instances are equivalent
        assert environment_definition_required_properties_model == environment_definition_required_properties_model2

        # Convert model instance back to dict and verify no loss of data
        environment_definition_required_properties_model_json2 = (
            environment_definition_required_properties_model.to_dict()
        )
        assert (
            environment_definition_required_properties_model_json2
            == environment_definition_required_properties_model_json
        )


class TestModel_EnvironmentDefinitionRequiredPropertiesResponse:
    """
    Test Class for EnvironmentDefinitionRequiredPropertiesResponse
    """

    def test_environment_definition_required_properties_response_serialization(self):
        """
        Test serialization/deserialization for EnvironmentDefinitionRequiredPropertiesResponse
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

        # Construct a json representation of a EnvironmentDefinitionRequiredPropertiesResponse model
        environment_definition_required_properties_response_model_json = {}
        environment_definition_required_properties_response_model_json['description'] = 'testString'
        environment_definition_required_properties_response_model_json['name'] = 'testString'
        environment_definition_required_properties_response_model_json['authorizations'] = project_config_auth_model
        environment_definition_required_properties_response_model_json['inputs'] = {'anyKey': 'anyValue'}
        environment_definition_required_properties_response_model_json['compliance_profile'] = (
            project_compliance_profile_model
        )

        # Construct a model instance of EnvironmentDefinitionRequiredPropertiesResponse by calling from_dict on the json representation
        environment_definition_required_properties_response_model = (
            EnvironmentDefinitionRequiredPropertiesResponse.from_dict(
                environment_definition_required_properties_response_model_json
            )
        )
        assert environment_definition_required_properties_response_model != False

        # Construct a model instance of EnvironmentDefinitionRequiredPropertiesResponse by calling from_dict on the json representation
        environment_definition_required_properties_response_model_dict = (
            EnvironmentDefinitionRequiredPropertiesResponse.from_dict(
                environment_definition_required_properties_response_model_json
            ).__dict__
        )
        environment_definition_required_properties_response_model2 = EnvironmentDefinitionRequiredPropertiesResponse(
            **environment_definition_required_properties_response_model_dict
        )

        # Verify the model instances are equivalent
        assert (
            environment_definition_required_properties_response_model
            == environment_definition_required_properties_response_model2
        )

        # Convert model instance back to dict and verify no loss of data
        environment_definition_required_properties_response_model_json2 = (
            environment_definition_required_properties_response_model.to_dict()
        )
        assert (
            environment_definition_required_properties_response_model_json2
            == environment_definition_required_properties_response_model_json
        )


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
        environment_delete_response_model_dict = EnvironmentDeleteResponse.from_dict(
            environment_delete_response_model_json
        ).__dict__
        environment_delete_response_model2 = EnvironmentDeleteResponse(**environment_delete_response_model_dict)

        # Verify the model instances are equivalent
        assert environment_delete_response_model == environment_delete_response_model2

        # Convert model instance back to dict and verify no loss of data
        environment_delete_response_model_json2 = environment_delete_response_model.to_dict()
        assert environment_delete_response_model_json2 == environment_delete_response_model_json


class TestModel_EnvironmentPrototype:
    """
    Test Class for EnvironmentPrototype
    """

    def test_environment_prototype_serialization(self):
        """
        Test serialization/deserialization for EnvironmentPrototype
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

        environment_definition_required_properties_model = {}  # EnvironmentDefinitionRequiredProperties
        environment_definition_required_properties_model['description'] = 'testString'
        environment_definition_required_properties_model['name'] = 'testString'
        environment_definition_required_properties_model['authorizations'] = project_config_auth_model
        environment_definition_required_properties_model['inputs'] = {'anyKey': 'anyValue'}
        environment_definition_required_properties_model['compliance_profile'] = project_compliance_profile_model

        # Construct a json representation of a EnvironmentPrototype model
        environment_prototype_model_json = {}
        environment_prototype_model_json['definition'] = environment_definition_required_properties_model

        # Construct a model instance of EnvironmentPrototype by calling from_dict on the json representation
        environment_prototype_model = EnvironmentPrototype.from_dict(environment_prototype_model_json)
        assert environment_prototype_model != False

        # Construct a model instance of EnvironmentPrototype by calling from_dict on the json representation
        environment_prototype_model_dict = EnvironmentPrototype.from_dict(environment_prototype_model_json).__dict__
        environment_prototype_model2 = EnvironmentPrototype(**environment_prototype_model_dict)

        # Verify the model instances are equivalent
        assert environment_prototype_model == environment_prototype_model2

        # Convert model instance back to dict and verify no loss of data
        environment_prototype_model_json2 = environment_prototype_model.to_dict()
        assert environment_prototype_model_json2 == environment_prototype_model_json


class TestModel_LastActionWithSummary:
    """
    Test Class for LastActionWithSummary
    """

    def test_last_action_with_summary_serialization(self):
        """
        Test serialization/deserialization for LastActionWithSummary
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
        action_job_plan_messages_summary_model['success_messages'] = ['testString']
        action_job_plan_messages_summary_model['update_messages'] = ['testString']
        action_job_plan_messages_summary_model['destroy_messages'] = ['testString']

        terraform_log_analyzer_success_message_model = {}  # TerraformLogAnalyzerSuccessMessage
        terraform_log_analyzer_success_message_model['resource_type'] = 'testString'
        terraform_log_analyzer_success_message_model['time-taken'] = 'testString'
        terraform_log_analyzer_success_message_model['id'] = 'testString'

        action_job_apply_messages_summary_model = {}  # ActionJobApplyMessagesSummary
        action_job_apply_messages_summary_model['error_messages'] = [terraform_log_analyzer_error_message_model]
        action_job_apply_messages_summary_model['success_messages'] = [terraform_log_analyzer_success_message_model]

        action_job_destroy_messages_summary_model = {}  # ActionJobDestroyMessagesSummary
        action_job_destroy_messages_summary_model['error_messages'] = [terraform_log_analyzer_error_message_model]

        action_job_summary_model = {}  # ActionJobSummary
        action_job_summary_model['version'] = 'testString'
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

        pre_post_action_job_system_error_model = {}  # PrePostActionJobSystemError
        pre_post_action_job_system_error_model['timestamp'] = '2019-01-01T12:00:00Z'
        pre_post_action_job_system_error_model['user_id'] = 'testString'
        pre_post_action_job_system_error_model['status_code'] = 'testString'
        pre_post_action_job_system_error_model['description'] = 'testString'
        pre_post_action_job_system_error_model['error_response'] = 'testString'

        pre_post_action_job_summary_model = {}  # PrePostActionJobSummary
        pre_post_action_job_summary_model['job_id'] = 'testString'
        pre_post_action_job_summary_model['start_time'] = '2019-01-01T12:00:00Z'
        pre_post_action_job_summary_model['end_time'] = '2019-01-01T12:00:00Z'
        pre_post_action_job_summary_model['tasks'] = 38
        pre_post_action_job_summary_model['ok'] = 38
        pre_post_action_job_summary_model['failed'] = 38
        pre_post_action_job_summary_model['skipped'] = 38
        pre_post_action_job_summary_model['changed'] = 38
        pre_post_action_job_summary_model['project_error'] = pre_post_action_job_system_error_model

        pre_post_action_job_with_id_and_summary_model = {}  # PrePostActionJobWithIdAndSummary
        pre_post_action_job_with_id_and_summary_model['id'] = 'testString'
        pre_post_action_job_with_id_and_summary_model['summary'] = pre_post_action_job_summary_model

        # Construct a json representation of a LastActionWithSummary model
        last_action_with_summary_model_json = {}
        last_action_with_summary_model_json['href'] = 'testString'
        last_action_with_summary_model_json['result'] = 'failed'
        last_action_with_summary_model_json['job'] = action_job_with_id_and_summary_model
        last_action_with_summary_model_json['pre_job'] = pre_post_action_job_with_id_and_summary_model
        last_action_with_summary_model_json['post_job'] = pre_post_action_job_with_id_and_summary_model

        # Construct a model instance of LastActionWithSummary by calling from_dict on the json representation
        last_action_with_summary_model = LastActionWithSummary.from_dict(last_action_with_summary_model_json)
        assert last_action_with_summary_model != False

        # Construct a model instance of LastActionWithSummary by calling from_dict on the json representation
        last_action_with_summary_model_dict = LastActionWithSummary.from_dict(
            last_action_with_summary_model_json
        ).__dict__
        last_action_with_summary_model2 = LastActionWithSummary(**last_action_with_summary_model_dict)

        # Verify the model instances are equivalent
        assert last_action_with_summary_model == last_action_with_summary_model2

        # Convert model instance back to dict and verify no loss of data
        last_action_with_summary_model_json2 = last_action_with_summary_model.to_dict()
        assert last_action_with_summary_model_json2 == last_action_with_summary_model_json


class TestModel_LastDriftDetectionJobSummary:
    """
    Test Class for LastDriftDetectionJobSummary
    """

    def test_last_drift_detection_job_summary_serialization(self):
        """
        Test serialization/deserialization for LastDriftDetectionJobSummary
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
        action_job_plan_messages_summary_model['success_messages'] = ['testString']
        action_job_plan_messages_summary_model['update_messages'] = ['testString']
        action_job_plan_messages_summary_model['destroy_messages'] = ['testString']

        terraform_log_analyzer_success_message_model = {}  # TerraformLogAnalyzerSuccessMessage
        terraform_log_analyzer_success_message_model['resource_type'] = 'testString'
        terraform_log_analyzer_success_message_model['time-taken'] = 'testString'
        terraform_log_analyzer_success_message_model['id'] = 'testString'

        action_job_apply_messages_summary_model = {}  # ActionJobApplyMessagesSummary
        action_job_apply_messages_summary_model['error_messages'] = [terraform_log_analyzer_error_message_model]
        action_job_apply_messages_summary_model['success_messages'] = [terraform_log_analyzer_success_message_model]

        action_job_destroy_messages_summary_model = {}  # ActionJobDestroyMessagesSummary
        action_job_destroy_messages_summary_model['error_messages'] = [terraform_log_analyzer_error_message_model]

        action_job_summary_model = {}  # ActionJobSummary
        action_job_summary_model['version'] = 'testString'
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

        # Construct a json representation of a LastDriftDetectionJobSummary model
        last_drift_detection_job_summary_model_json = {}
        last_drift_detection_job_summary_model_json['job'] = action_job_with_id_and_summary_model

        # Construct a model instance of LastDriftDetectionJobSummary by calling from_dict on the json representation
        last_drift_detection_job_summary_model = LastDriftDetectionJobSummary.from_dict(
            last_drift_detection_job_summary_model_json
        )
        assert last_drift_detection_job_summary_model != False

        # Construct a model instance of LastDriftDetectionJobSummary by calling from_dict on the json representation
        last_drift_detection_job_summary_model_dict = LastDriftDetectionJobSummary.from_dict(
            last_drift_detection_job_summary_model_json
        ).__dict__
        last_drift_detection_job_summary_model2 = LastDriftDetectionJobSummary(
            **last_drift_detection_job_summary_model_dict
        )

        # Verify the model instances are equivalent
        assert last_drift_detection_job_summary_model == last_drift_detection_job_summary_model2

        # Convert model instance back to dict and verify no loss of data
        last_drift_detection_job_summary_model_json2 = last_drift_detection_job_summary_model.to_dict()
        assert last_drift_detection_job_summary_model_json2 == last_drift_detection_job_summary_model_json


class TestModel_LastMonitoringActionWithSummary:
    """
    Test Class for LastMonitoringActionWithSummary
    """

    def test_last_monitoring_action_with_summary_serialization(self):
        """
        Test serialization/deserialization for LastMonitoringActionWithSummary
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
        action_job_plan_messages_summary_model['success_messages'] = ['testString']
        action_job_plan_messages_summary_model['update_messages'] = ['testString']
        action_job_plan_messages_summary_model['destroy_messages'] = ['testString']

        terraform_log_analyzer_success_message_model = {}  # TerraformLogAnalyzerSuccessMessage
        terraform_log_analyzer_success_message_model['resource_type'] = 'testString'
        terraform_log_analyzer_success_message_model['time-taken'] = 'testString'
        terraform_log_analyzer_success_message_model['id'] = 'testString'

        action_job_apply_messages_summary_model = {}  # ActionJobApplyMessagesSummary
        action_job_apply_messages_summary_model['error_messages'] = [terraform_log_analyzer_error_message_model]
        action_job_apply_messages_summary_model['success_messages'] = [terraform_log_analyzer_success_message_model]

        action_job_destroy_messages_summary_model = {}  # ActionJobDestroyMessagesSummary
        action_job_destroy_messages_summary_model['error_messages'] = [terraform_log_analyzer_error_message_model]

        action_job_summary_model = {}  # ActionJobSummary
        action_job_summary_model['version'] = 'testString'
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

        last_drift_detection_job_summary_model = {}  # LastDriftDetectionJobSummary
        last_drift_detection_job_summary_model['job'] = action_job_with_id_and_summary_model

        # Construct a json representation of a LastMonitoringActionWithSummary model
        last_monitoring_action_with_summary_model_json = {}
        last_monitoring_action_with_summary_model_json['href'] = 'testString'
        last_monitoring_action_with_summary_model_json['result'] = 'failed'
        last_monitoring_action_with_summary_model_json['drift_detection'] = last_drift_detection_job_summary_model

        # Construct a model instance of LastMonitoringActionWithSummary by calling from_dict on the json representation
        last_monitoring_action_with_summary_model = LastMonitoringActionWithSummary.from_dict(
            last_monitoring_action_with_summary_model_json
        )
        assert last_monitoring_action_with_summary_model != False

        # Construct a model instance of LastMonitoringActionWithSummary by calling from_dict on the json representation
        last_monitoring_action_with_summary_model_dict = LastMonitoringActionWithSummary.from_dict(
            last_monitoring_action_with_summary_model_json
        ).__dict__
        last_monitoring_action_with_summary_model2 = LastMonitoringActionWithSummary(
            **last_monitoring_action_with_summary_model_dict
        )

        # Verify the model instances are equivalent
        assert last_monitoring_action_with_summary_model == last_monitoring_action_with_summary_model2

        # Convert model instance back to dict and verify no loss of data
        last_monitoring_action_with_summary_model_json2 = last_monitoring_action_with_summary_model.to_dict()
        assert last_monitoring_action_with_summary_model_json2 == last_monitoring_action_with_summary_model_json


class TestModel_LastValidatedActionWithSummary:
    """
    Test Class for LastValidatedActionWithSummary
    """

    def test_last_validated_action_with_summary_serialization(self):
        """
        Test serialization/deserialization for LastValidatedActionWithSummary
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
        action_job_plan_messages_summary_model['success_messages'] = ['testString']
        action_job_plan_messages_summary_model['update_messages'] = ['testString']
        action_job_plan_messages_summary_model['destroy_messages'] = ['testString']

        terraform_log_analyzer_success_message_model = {}  # TerraformLogAnalyzerSuccessMessage
        terraform_log_analyzer_success_message_model['resource_type'] = 'testString'
        terraform_log_analyzer_success_message_model['time-taken'] = 'testString'
        terraform_log_analyzer_success_message_model['id'] = 'testString'

        action_job_apply_messages_summary_model = {}  # ActionJobApplyMessagesSummary
        action_job_apply_messages_summary_model['error_messages'] = [terraform_log_analyzer_error_message_model]
        action_job_apply_messages_summary_model['success_messages'] = [terraform_log_analyzer_success_message_model]

        action_job_destroy_messages_summary_model = {}  # ActionJobDestroyMessagesSummary
        action_job_destroy_messages_summary_model['error_messages'] = [terraform_log_analyzer_error_message_model]

        action_job_summary_model = {}  # ActionJobSummary
        action_job_summary_model['version'] = 'testString'
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

        pre_post_action_job_system_error_model = {}  # PrePostActionJobSystemError
        pre_post_action_job_system_error_model['timestamp'] = '2019-01-01T12:00:00Z'
        pre_post_action_job_system_error_model['user_id'] = 'testString'
        pre_post_action_job_system_error_model['status_code'] = 'testString'
        pre_post_action_job_system_error_model['description'] = 'testString'
        pre_post_action_job_system_error_model['error_response'] = 'testString'

        pre_post_action_job_summary_model = {}  # PrePostActionJobSummary
        pre_post_action_job_summary_model['job_id'] = 'testString'
        pre_post_action_job_summary_model['start_time'] = '2019-01-01T12:00:00Z'
        pre_post_action_job_summary_model['end_time'] = '2019-01-01T12:00:00Z'
        pre_post_action_job_summary_model['tasks'] = 38
        pre_post_action_job_summary_model['ok'] = 38
        pre_post_action_job_summary_model['failed'] = 38
        pre_post_action_job_summary_model['skipped'] = 38
        pre_post_action_job_summary_model['changed'] = 38
        pre_post_action_job_summary_model['project_error'] = pre_post_action_job_system_error_model

        pre_post_action_job_with_id_and_summary_model = {}  # PrePostActionJobWithIdAndSummary
        pre_post_action_job_with_id_and_summary_model['id'] = 'testString'
        pre_post_action_job_with_id_and_summary_model['summary'] = pre_post_action_job_summary_model

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

        project_config_metadata_code_risk_analyzer_logs_model = (
            {}
        )  # ProjectConfigMetadataCodeRiskAnalyzerLogsVersion204
        project_config_metadata_code_risk_analyzer_logs_model['cra_version'] = '2.0.4'
        project_config_metadata_code_risk_analyzer_logs_model['schema_version'] = 'testString'
        project_config_metadata_code_risk_analyzer_logs_model['status'] = 'passed'
        project_config_metadata_code_risk_analyzer_logs_model['summary'] = code_risk_analyzer_logs_summary_model
        project_config_metadata_code_risk_analyzer_logs_model['timestamp'] = '2019-01-01T12:00:00Z'

        # Construct a json representation of a LastValidatedActionWithSummary model
        last_validated_action_with_summary_model_json = {}
        last_validated_action_with_summary_model_json['href'] = 'testString'
        last_validated_action_with_summary_model_json['result'] = 'failed'
        last_validated_action_with_summary_model_json['job'] = action_job_with_id_and_summary_model
        last_validated_action_with_summary_model_json['pre_job'] = pre_post_action_job_with_id_and_summary_model
        last_validated_action_with_summary_model_json['post_job'] = pre_post_action_job_with_id_and_summary_model
        last_validated_action_with_summary_model_json['cost_estimate'] = project_config_metadata_cost_estimate_model
        last_validated_action_with_summary_model_json['cra_logs'] = (
            project_config_metadata_code_risk_analyzer_logs_model
        )

        # Construct a model instance of LastValidatedActionWithSummary by calling from_dict on the json representation
        last_validated_action_with_summary_model = LastValidatedActionWithSummary.from_dict(
            last_validated_action_with_summary_model_json
        )
        assert last_validated_action_with_summary_model != False

        # Construct a model instance of LastValidatedActionWithSummary by calling from_dict on the json representation
        last_validated_action_with_summary_model_dict = LastValidatedActionWithSummary.from_dict(
            last_validated_action_with_summary_model_json
        ).__dict__
        last_validated_action_with_summary_model2 = LastValidatedActionWithSummary(
            **last_validated_action_with_summary_model_dict
        )

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


class TestModel_PrePostActionJobSummary:
    """
    Test Class for PrePostActionJobSummary
    """

    def test_pre_post_action_job_summary_serialization(self):
        """
        Test serialization/deserialization for PrePostActionJobSummary
        """

        # Construct dict forms of any model objects needed in order to build this model.

        pre_post_action_job_system_error_model = {}  # PrePostActionJobSystemError
        pre_post_action_job_system_error_model['timestamp'] = '2019-01-01T12:00:00Z'
        pre_post_action_job_system_error_model['user_id'] = 'testString'
        pre_post_action_job_system_error_model['status_code'] = 'testString'
        pre_post_action_job_system_error_model['description'] = 'testString'
        pre_post_action_job_system_error_model['error_response'] = 'testString'

        # Construct a json representation of a PrePostActionJobSummary model
        pre_post_action_job_summary_model_json = {}
        pre_post_action_job_summary_model_json['job_id'] = 'testString'
        pre_post_action_job_summary_model_json['start_time'] = '2019-01-01T12:00:00Z'
        pre_post_action_job_summary_model_json['end_time'] = '2019-01-01T12:00:00Z'
        pre_post_action_job_summary_model_json['tasks'] = 38
        pre_post_action_job_summary_model_json['ok'] = 38
        pre_post_action_job_summary_model_json['failed'] = 38
        pre_post_action_job_summary_model_json['skipped'] = 38
        pre_post_action_job_summary_model_json['changed'] = 38
        pre_post_action_job_summary_model_json['project_error'] = pre_post_action_job_system_error_model

        # Construct a model instance of PrePostActionJobSummary by calling from_dict on the json representation
        pre_post_action_job_summary_model = PrePostActionJobSummary.from_dict(pre_post_action_job_summary_model_json)
        assert pre_post_action_job_summary_model != False

        # Construct a model instance of PrePostActionJobSummary by calling from_dict on the json representation
        pre_post_action_job_summary_model_dict = PrePostActionJobSummary.from_dict(
            pre_post_action_job_summary_model_json
        ).__dict__
        pre_post_action_job_summary_model2 = PrePostActionJobSummary(**pre_post_action_job_summary_model_dict)

        # Verify the model instances are equivalent
        assert pre_post_action_job_summary_model == pre_post_action_job_summary_model2

        # Convert model instance back to dict and verify no loss of data
        pre_post_action_job_summary_model_json2 = pre_post_action_job_summary_model.to_dict()
        assert pre_post_action_job_summary_model_json2 == pre_post_action_job_summary_model_json


class TestModel_PrePostActionJobSystemError:
    """
    Test Class for PrePostActionJobSystemError
    """

    def test_pre_post_action_job_system_error_serialization(self):
        """
        Test serialization/deserialization for PrePostActionJobSystemError
        """

        # Construct a json representation of a PrePostActionJobSystemError model
        pre_post_action_job_system_error_model_json = {}
        pre_post_action_job_system_error_model_json['timestamp'] = '2019-01-01T12:00:00Z'
        pre_post_action_job_system_error_model_json['user_id'] = 'testString'
        pre_post_action_job_system_error_model_json['status_code'] = 'testString'
        pre_post_action_job_system_error_model_json['description'] = 'testString'
        pre_post_action_job_system_error_model_json['error_response'] = 'testString'

        # Construct a model instance of PrePostActionJobSystemError by calling from_dict on the json representation
        pre_post_action_job_system_error_model = PrePostActionJobSystemError.from_dict(
            pre_post_action_job_system_error_model_json
        )
        assert pre_post_action_job_system_error_model != False

        # Construct a model instance of PrePostActionJobSystemError by calling from_dict on the json representation
        pre_post_action_job_system_error_model_dict = PrePostActionJobSystemError.from_dict(
            pre_post_action_job_system_error_model_json
        ).__dict__
        pre_post_action_job_system_error_model2 = PrePostActionJobSystemError(
            **pre_post_action_job_system_error_model_dict
        )

        # Verify the model instances are equivalent
        assert pre_post_action_job_system_error_model == pre_post_action_job_system_error_model2

        # Convert model instance back to dict and verify no loss of data
        pre_post_action_job_system_error_model_json2 = pre_post_action_job_system_error_model.to_dict()
        assert pre_post_action_job_system_error_model_json2 == pre_post_action_job_system_error_model_json


class TestModel_PrePostActionJobWithIdAndSummary:
    """
    Test Class for PrePostActionJobWithIdAndSummary
    """

    def test_pre_post_action_job_with_id_and_summary_serialization(self):
        """
        Test serialization/deserialization for PrePostActionJobWithIdAndSummary
        """

        # Construct dict forms of any model objects needed in order to build this model.

        pre_post_action_job_system_error_model = {}  # PrePostActionJobSystemError
        pre_post_action_job_system_error_model['timestamp'] = '2019-01-01T12:00:00Z'
        pre_post_action_job_system_error_model['user_id'] = 'testString'
        pre_post_action_job_system_error_model['status_code'] = 'testString'
        pre_post_action_job_system_error_model['description'] = 'testString'
        pre_post_action_job_system_error_model['error_response'] = 'testString'

        pre_post_action_job_summary_model = {}  # PrePostActionJobSummary
        pre_post_action_job_summary_model['job_id'] = 'testString'
        pre_post_action_job_summary_model['start_time'] = '2019-01-01T12:00:00Z'
        pre_post_action_job_summary_model['end_time'] = '2019-01-01T12:00:00Z'
        pre_post_action_job_summary_model['tasks'] = 38
        pre_post_action_job_summary_model['ok'] = 38
        pre_post_action_job_summary_model['failed'] = 38
        pre_post_action_job_summary_model['skipped'] = 38
        pre_post_action_job_summary_model['changed'] = 38
        pre_post_action_job_summary_model['project_error'] = pre_post_action_job_system_error_model

        # Construct a json representation of a PrePostActionJobWithIdAndSummary model
        pre_post_action_job_with_id_and_summary_model_json = {}
        pre_post_action_job_with_id_and_summary_model_json['id'] = 'testString'
        pre_post_action_job_with_id_and_summary_model_json['summary'] = pre_post_action_job_summary_model

        # Construct a model instance of PrePostActionJobWithIdAndSummary by calling from_dict on the json representation
        pre_post_action_job_with_id_and_summary_model = PrePostActionJobWithIdAndSummary.from_dict(
            pre_post_action_job_with_id_and_summary_model_json
        )
        assert pre_post_action_job_with_id_and_summary_model != False

        # Construct a model instance of PrePostActionJobWithIdAndSummary by calling from_dict on the json representation
        pre_post_action_job_with_id_and_summary_model_dict = PrePostActionJobWithIdAndSummary.from_dict(
            pre_post_action_job_with_id_and_summary_model_json
        ).__dict__
        pre_post_action_job_with_id_and_summary_model2 = PrePostActionJobWithIdAndSummary(
            **pre_post_action_job_with_id_and_summary_model_dict
        )

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

        project_config_version_definition_summary_model = {}  # ProjectConfigVersionDefinitionSummary
        project_config_version_definition_summary_model['environment_id'] = 'testString'
        project_config_version_definition_summary_model['locator_id'] = 'testString'

        project_config_version_summary_model = {}  # ProjectConfigVersionSummary
        project_config_version_summary_model['definition'] = project_config_version_definition_summary_model
        project_config_version_summary_model['state'] = 'approved'
        project_config_version_summary_model['version'] = 38
        project_config_version_summary_model['href'] = 'testString'

        project_config_summary_definition_model = {}  # ProjectConfigSummaryDefinition
        project_config_summary_definition_model['description'] = 'testString'
        project_config_summary_definition_model['name'] = 'testString'
        project_config_summary_definition_model['locator_id'] = 'testString'

        project_definition_reference_model = {}  # ProjectDefinitionReference
        project_definition_reference_model['name'] = 'testString'

        project_reference_model = {}  # ProjectReference
        project_reference_model['id'] = 'testString'
        project_reference_model['href'] = 'testString'
        project_reference_model['definition'] = project_definition_reference_model
        project_reference_model['crn'] = (
            'crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::'
        )

        project_config_summary_model = {}  # ProjectConfigSummary
        project_config_summary_model['approved_version'] = project_config_version_summary_model
        project_config_summary_model['deployed_version'] = project_config_version_summary_model
        project_config_summary_model['id'] = 'testString'
        project_config_summary_model['version'] = 38
        project_config_summary_model['state'] = 'approved'
        project_config_summary_model['created_at'] = '2019-01-01T12:00:00Z'
        project_config_summary_model['modified_at'] = '2019-01-01T12:00:00Z'
        project_config_summary_model['href'] = 'testString'
        project_config_summary_model['definition'] = project_config_summary_definition_model
        project_config_summary_model['project'] = project_reference_model
        project_config_summary_model['deployment_model'] = 'project_deployed'

        project_environment_summary_definition_model = {}  # ProjectEnvironmentSummaryDefinition
        project_environment_summary_definition_model['description'] = 'testString'
        project_environment_summary_definition_model['name'] = 'testString'

        project_environment_summary_model = {}  # ProjectEnvironmentSummary
        project_environment_summary_model['id'] = 'testString'
        project_environment_summary_model['project'] = project_reference_model
        project_environment_summary_model['created_at'] = '2019-01-01T12:00:00Z'
        project_environment_summary_model['href'] = 'testString'
        project_environment_summary_model['definition'] = project_environment_summary_definition_model

        project_definition_properties_model = {}  # ProjectDefinitionProperties
        project_definition_properties_model['name'] = 'testString'
        project_definition_properties_model['destroy_on_delete'] = True
        project_definition_properties_model['description'] = 'testString'
        project_definition_properties_model['monitoring_enabled'] = False

        # Construct a json representation of a Project model
        project_model_json = {}
        project_model_json['crn'] = (
            'crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::'
        )
        project_model_json['created_at'] = '2019-01-01T12:00:00Z'
        project_model_json['cumulative_needs_attention_view'] = [cumulative_needs_attention_model]
        project_model_json['cumulative_needs_attention_view_error'] = False
        project_model_json['id'] = 'testString'
        project_model_json['location'] = 'testString'
        project_model_json['resource_group_id'] = 'testString'
        project_model_json['state'] = 'ready'
        project_model_json['href'] = 'testString'
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
        project_definition_properties_model['destroy_on_delete'] = True
        project_definition_properties_model['description'] = 'testString'
        project_definition_properties_model['monitoring_enabled'] = False

        project_summary_model = {}  # ProjectSummary
        project_summary_model['crn'] = (
            'crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::'
        )
        project_summary_model['created_at'] = '2019-01-01T12:00:00Z'
        project_summary_model['cumulative_needs_attention_view'] = [cumulative_needs_attention_model]
        project_summary_model['cumulative_needs_attention_view_error'] = False
        project_summary_model['id'] = 'testString'
        project_summary_model['location'] = 'testString'
        project_summary_model['resource_group_id'] = 'testString'
        project_summary_model['state'] = 'ready'
        project_summary_model['href'] = 'testString'
        project_summary_model['definition'] = project_definition_properties_model

        # Construct a json representation of a ProjectCollection model
        project_collection_model_json = {}
        project_collection_model_json['limit'] = 10
        project_collection_model_json['first'] = pagination_link_model
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
        project_compliance_profile_model_dict = ProjectComplianceProfile.from_dict(
            project_compliance_profile_model_json
        ).__dict__
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

        project_config_needs_attention_state_model = {}  # ProjectConfigNeedsAttentionState
        project_config_needs_attention_state_model['event_id'] = 'testString'
        project_config_needs_attention_state_model['event'] = 'testString'
        project_config_needs_attention_state_model['severity'] = 'INFO'
        project_config_needs_attention_state_model['action_url'] = 'testString'
        project_config_needs_attention_state_model['target'] = 'testString'
        project_config_needs_attention_state_model['triggered_by'] = 'testString'
        project_config_needs_attention_state_model['timestamp'] = 'testString'

        project_config_metadata_last_approved_model = {}  # ProjectConfigMetadataLastApproved
        project_config_metadata_last_approved_model['at'] = '2019-01-01T12:00:00Z'
        project_config_metadata_last_approved_model['comment'] = 'testString'
        project_config_metadata_last_approved_model['is_forced'] = True
        project_config_metadata_last_approved_model['user_id'] = 'testString'

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
        action_job_plan_messages_summary_model['success_messages'] = ['testString']
        action_job_plan_messages_summary_model['update_messages'] = ['testString']
        action_job_plan_messages_summary_model['destroy_messages'] = ['testString']

        terraform_log_analyzer_success_message_model = {}  # TerraformLogAnalyzerSuccessMessage
        terraform_log_analyzer_success_message_model['resource_type'] = 'testString'
        terraform_log_analyzer_success_message_model['time-taken'] = 'testString'
        terraform_log_analyzer_success_message_model['id'] = 'testString'

        action_job_apply_messages_summary_model = {}  # ActionJobApplyMessagesSummary
        action_job_apply_messages_summary_model['error_messages'] = [terraform_log_analyzer_error_message_model]
        action_job_apply_messages_summary_model['success_messages'] = [terraform_log_analyzer_success_message_model]

        action_job_destroy_messages_summary_model = {}  # ActionJobDestroyMessagesSummary
        action_job_destroy_messages_summary_model['error_messages'] = [terraform_log_analyzer_error_message_model]

        action_job_summary_model = {}  # ActionJobSummary
        action_job_summary_model['version'] = 'testString'
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

        pre_post_action_job_system_error_model = {}  # PrePostActionJobSystemError
        pre_post_action_job_system_error_model['timestamp'] = '2019-01-01T12:00:00Z'
        pre_post_action_job_system_error_model['user_id'] = 'testString'
        pre_post_action_job_system_error_model['status_code'] = 'testString'
        pre_post_action_job_system_error_model['description'] = 'testString'
        pre_post_action_job_system_error_model['error_response'] = 'testString'

        pre_post_action_job_summary_model = {}  # PrePostActionJobSummary
        pre_post_action_job_summary_model['job_id'] = 'testString'
        pre_post_action_job_summary_model['start_time'] = '2019-01-01T12:00:00Z'
        pre_post_action_job_summary_model['end_time'] = '2019-01-01T12:00:00Z'
        pre_post_action_job_summary_model['tasks'] = 38
        pre_post_action_job_summary_model['ok'] = 38
        pre_post_action_job_summary_model['failed'] = 38
        pre_post_action_job_summary_model['skipped'] = 38
        pre_post_action_job_summary_model['changed'] = 38
        pre_post_action_job_summary_model['project_error'] = pre_post_action_job_system_error_model

        pre_post_action_job_with_id_and_summary_model = {}  # PrePostActionJobWithIdAndSummary
        pre_post_action_job_with_id_and_summary_model['id'] = 'testString'
        pre_post_action_job_with_id_and_summary_model['summary'] = pre_post_action_job_summary_model

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

        project_config_metadata_code_risk_analyzer_logs_model = (
            {}
        )  # ProjectConfigMetadataCodeRiskAnalyzerLogsVersion204
        project_config_metadata_code_risk_analyzer_logs_model['cra_version'] = '2.0.4'
        project_config_metadata_code_risk_analyzer_logs_model['schema_version'] = 'testString'
        project_config_metadata_code_risk_analyzer_logs_model['status'] = 'passed'
        project_config_metadata_code_risk_analyzer_logs_model['summary'] = code_risk_analyzer_logs_summary_model
        project_config_metadata_code_risk_analyzer_logs_model['timestamp'] = '2019-01-01T12:00:00Z'

        last_validated_action_with_summary_model = {}  # LastValidatedActionWithSummary
        last_validated_action_with_summary_model['href'] = 'testString'
        last_validated_action_with_summary_model['result'] = 'failed'
        last_validated_action_with_summary_model['job'] = action_job_with_id_and_summary_model
        last_validated_action_with_summary_model['pre_job'] = pre_post_action_job_with_id_and_summary_model
        last_validated_action_with_summary_model['post_job'] = pre_post_action_job_with_id_and_summary_model
        last_validated_action_with_summary_model['cost_estimate'] = project_config_metadata_cost_estimate_model
        last_validated_action_with_summary_model['cra_logs'] = project_config_metadata_code_risk_analyzer_logs_model

        last_action_with_summary_model = {}  # LastActionWithSummary
        last_action_with_summary_model['href'] = 'testString'
        last_action_with_summary_model['result'] = 'failed'
        last_action_with_summary_model['job'] = action_job_with_id_and_summary_model
        last_action_with_summary_model['pre_job'] = pre_post_action_job_with_id_and_summary_model
        last_action_with_summary_model['post_job'] = pre_post_action_job_with_id_and_summary_model

        last_drift_detection_job_summary_model = {}  # LastDriftDetectionJobSummary
        last_drift_detection_job_summary_model['job'] = action_job_with_id_and_summary_model

        last_monitoring_action_with_summary_model = {}  # LastMonitoringActionWithSummary
        last_monitoring_action_with_summary_model['href'] = 'testString'
        last_monitoring_action_with_summary_model['result'] = 'failed'
        last_monitoring_action_with_summary_model['drift_detection'] = last_drift_detection_job_summary_model

        output_value_model = {}  # OutputValue
        output_value_model['name'] = 'testString'
        output_value_model['description'] = 'testString'
        output_value_model['value'] = 'testString'

        project_definition_reference_model = {}  # ProjectDefinitionReference
        project_definition_reference_model['name'] = 'testString'

        project_reference_model = {}  # ProjectReference
        project_reference_model['id'] = 'testString'
        project_reference_model['href'] = 'testString'
        project_reference_model['definition'] = project_definition_reference_model
        project_reference_model['crn'] = (
            'crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::'
        )

        script_model = {}  # Script
        script_model['type'] = 'ansible'
        script_model['path'] = 'scripts/validate-post-ansible-playbook.yaml'
        script_model['short_description'] = 'testString'

        schematics_metadata_model = {}  # SchematicsMetadata
        schematics_metadata_model['workspace_crn'] = (
            'crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::'
        )
        schematics_metadata_model['validate_pre_script'] = script_model
        schematics_metadata_model['validate_post_script'] = script_model
        schematics_metadata_model['deploy_pre_script'] = script_model
        schematics_metadata_model['deploy_post_script'] = script_model
        schematics_metadata_model['undeploy_pre_script'] = script_model
        schematics_metadata_model['undeploy_post_script'] = script_model

        project_object_reference_model = {}  # ProjectObjectReference
        project_object_reference_model['id'] = 'testString'
        project_object_reference_model['href'] = 'testString'

        project_compliance_profile_model = {}  # ProjectComplianceProfile
        project_compliance_profile_model['id'] = 'testString'
        project_compliance_profile_model['instance_id'] = 'testString'
        project_compliance_profile_model['instance_location'] = 'testString'
        project_compliance_profile_model['attachment_id'] = 'testString'
        project_compliance_profile_model['profile_name'] = 'testString'

        project_config_auth_model = {}  # ProjectConfigAuth
        project_config_auth_model['trusted_profile_id'] = 'testString'
        project_config_auth_model['method'] = 'api_key'
        project_config_auth_model['api_key'] = 'testString'

        project_config_definition_response_model = (
            {}
        )  # ProjectConfigDefinitionResponseDAConfigDefinitionPropertiesResponse
        project_config_definition_response_model['compliance_profile'] = project_compliance_profile_model
        project_config_definition_response_model['locator_id'] = 'testString'
        project_config_definition_response_model['description'] = 'testString'
        project_config_definition_response_model['name'] = 'testString'
        project_config_definition_response_model['environment_id'] = 'testString'
        project_config_definition_response_model['authorizations'] = project_config_auth_model
        project_config_definition_response_model['inputs'] = {'anyKey': 'anyValue'}
        project_config_definition_response_model['settings'] = {'anyKey': 'anyValue'}

        project_config_version_definition_summary_model = {}  # ProjectConfigVersionDefinitionSummary
        project_config_version_definition_summary_model['environment_id'] = 'testString'
        project_config_version_definition_summary_model['locator_id'] = 'testString'

        project_config_version_summary_model = {}  # ProjectConfigVersionSummary
        project_config_version_summary_model['definition'] = project_config_version_definition_summary_model
        project_config_version_summary_model['state'] = 'approved'
        project_config_version_summary_model['version'] = 38
        project_config_version_summary_model['href'] = 'testString'

        # Construct a json representation of a ProjectConfig model
        project_config_model_json = {}
        project_config_model_json['id'] = 'testString'
        project_config_model_json['version'] = 38
        project_config_model_json['is_draft'] = True
        project_config_model_json['needs_attention_state'] = [project_config_needs_attention_state_model]
        project_config_model_json['created_at'] = '2019-01-01T12:00:00Z'
        project_config_model_json['modified_at'] = '2019-01-01T12:00:00Z'
        project_config_model_json['last_approved'] = project_config_metadata_last_approved_model
        project_config_model_json['last_saved_at'] = '2019-01-01T12:00:00Z'
        project_config_model_json['last_validated'] = last_validated_action_with_summary_model
        project_config_model_json['last_deployed'] = last_action_with_summary_model
        project_config_model_json['last_undeployed'] = last_action_with_summary_model
        project_config_model_json['last_monitoring'] = last_monitoring_action_with_summary_model
        project_config_model_json['outputs'] = [output_value_model]
        project_config_model_json['project'] = project_reference_model
        project_config_model_json['references'] = {'anyKey': 'anyValue'}
        project_config_model_json['schematics'] = schematics_metadata_model
        project_config_model_json['state'] = 'approved'
        project_config_model_json['update_available'] = True
        project_config_model_json['template'] = project_object_reference_model
        project_config_model_json['href'] = 'testString'
        project_config_model_json['definition'] = project_config_definition_response_model
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

        pagination_link_model = {}  # PaginationLink
        pagination_link_model['href'] = 'testString'

        project_config_version_definition_summary_model = {}  # ProjectConfigVersionDefinitionSummary
        project_config_version_definition_summary_model['environment_id'] = 'testString'
        project_config_version_definition_summary_model['locator_id'] = 'testString'

        project_config_version_summary_model = {}  # ProjectConfigVersionSummary
        project_config_version_summary_model['definition'] = project_config_version_definition_summary_model
        project_config_version_summary_model['state'] = 'approved'
        project_config_version_summary_model['version'] = 38
        project_config_version_summary_model['href'] = 'testString'

        project_config_summary_definition_model = {}  # ProjectConfigSummaryDefinition
        project_config_summary_definition_model['description'] = 'testString'
        project_config_summary_definition_model['name'] = 'testString'
        project_config_summary_definition_model['locator_id'] = 'testString'

        project_definition_reference_model = {}  # ProjectDefinitionReference
        project_definition_reference_model['name'] = 'testString'

        project_reference_model = {}  # ProjectReference
        project_reference_model['id'] = 'testString'
        project_reference_model['href'] = 'testString'
        project_reference_model['definition'] = project_definition_reference_model
        project_reference_model['crn'] = (
            'crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::'
        )

        project_config_summary_model = {}  # ProjectConfigSummary
        project_config_summary_model['approved_version'] = project_config_version_summary_model
        project_config_summary_model['deployed_version'] = project_config_version_summary_model
        project_config_summary_model['id'] = 'testString'
        project_config_summary_model['version'] = 38
        project_config_summary_model['state'] = 'approved'
        project_config_summary_model['created_at'] = '2019-01-01T12:00:00Z'
        project_config_summary_model['modified_at'] = '2019-01-01T12:00:00Z'
        project_config_summary_model['href'] = 'testString'
        project_config_summary_model['definition'] = project_config_summary_definition_model
        project_config_summary_model['project'] = project_reference_model
        project_config_summary_model['deployment_model'] = 'project_deployed'

        # Construct a json representation of a ProjectConfigCollection model
        project_config_collection_model_json = {}
        project_config_collection_model_json['limit'] = 10
        project_config_collection_model_json['first'] = pagination_link_model
        project_config_collection_model_json['next'] = pagination_link_model
        project_config_collection_model_json['configs'] = [project_config_summary_model]

        # Construct a model instance of ProjectConfigCollection by calling from_dict on the json representation
        project_config_collection_model = ProjectConfigCollection.from_dict(project_config_collection_model_json)
        assert project_config_collection_model != False

        # Construct a model instance of ProjectConfigCollection by calling from_dict on the json representation
        project_config_collection_model_dict = ProjectConfigCollection.from_dict(
            project_config_collection_model_json
        ).__dict__
        project_config_collection_model2 = ProjectConfigCollection(**project_config_collection_model_dict)

        # Verify the model instances are equivalent
        assert project_config_collection_model == project_config_collection_model2

        # Convert model instance back to dict and verify no loss of data
        project_config_collection_model_json2 = project_config_collection_model.to_dict()
        assert project_config_collection_model_json2 == project_config_collection_model_json


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
        project_config_metadata_cost_estimate_model = ProjectConfigMetadataCostEstimate.from_dict(
            project_config_metadata_cost_estimate_model_json
        )
        assert project_config_metadata_cost_estimate_model != False

        # Construct a model instance of ProjectConfigMetadataCostEstimate by calling from_dict on the json representation
        project_config_metadata_cost_estimate_model_dict = ProjectConfigMetadataCostEstimate.from_dict(
            project_config_metadata_cost_estimate_model_json
        ).__dict__
        project_config_metadata_cost_estimate_model2 = ProjectConfigMetadataCostEstimate(
            **project_config_metadata_cost_estimate_model_dict
        )

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
        project_config_metadata_last_approved_model = ProjectConfigMetadataLastApproved.from_dict(
            project_config_metadata_last_approved_model_json
        )
        assert project_config_metadata_last_approved_model != False

        # Construct a model instance of ProjectConfigMetadataLastApproved by calling from_dict on the json representation
        project_config_metadata_last_approved_model_dict = ProjectConfigMetadataLastApproved.from_dict(
            project_config_metadata_last_approved_model_json
        ).__dict__
        project_config_metadata_last_approved_model2 = ProjectConfigMetadataLastApproved(
            **project_config_metadata_last_approved_model_dict
        )

        # Verify the model instances are equivalent
        assert project_config_metadata_last_approved_model == project_config_metadata_last_approved_model2

        # Convert model instance back to dict and verify no loss of data
        project_config_metadata_last_approved_model_json2 = project_config_metadata_last_approved_model.to_dict()
        assert project_config_metadata_last_approved_model_json2 == project_config_metadata_last_approved_model_json


class TestModel_ProjectConfigNeedsAttentionState:
    """
    Test Class for ProjectConfigNeedsAttentionState
    """

    def test_project_config_needs_attention_state_serialization(self):
        """
        Test serialization/deserialization for ProjectConfigNeedsAttentionState
        """

        # Construct a json representation of a ProjectConfigNeedsAttentionState model
        project_config_needs_attention_state_model_json = {}
        project_config_needs_attention_state_model_json['event_id'] = 'testString'
        project_config_needs_attention_state_model_json['event'] = 'testString'
        project_config_needs_attention_state_model_json['severity'] = 'INFO'
        project_config_needs_attention_state_model_json['action_url'] = 'testString'
        project_config_needs_attention_state_model_json['target'] = 'testString'
        project_config_needs_attention_state_model_json['triggered_by'] = 'testString'
        project_config_needs_attention_state_model_json['timestamp'] = 'testString'

        # Construct a model instance of ProjectConfigNeedsAttentionState by calling from_dict on the json representation
        project_config_needs_attention_state_model = ProjectConfigNeedsAttentionState.from_dict(
            project_config_needs_attention_state_model_json
        )
        assert project_config_needs_attention_state_model != False

        # Construct a model instance of ProjectConfigNeedsAttentionState by calling from_dict on the json representation
        project_config_needs_attention_state_model_dict = ProjectConfigNeedsAttentionState.from_dict(
            project_config_needs_attention_state_model_json
        ).__dict__
        project_config_needs_attention_state_model2 = ProjectConfigNeedsAttentionState(
            **project_config_needs_attention_state_model_dict
        )

        # Verify the model instances are equivalent
        assert project_config_needs_attention_state_model == project_config_needs_attention_state_model2

        # Convert model instance back to dict and verify no loss of data
        project_config_needs_attention_state_model_json2 = project_config_needs_attention_state_model.to_dict()
        assert project_config_needs_attention_state_model_json2 == project_config_needs_attention_state_model_json


class TestModel_ProjectConfigPrototype:
    """
    Test Class for ProjectConfigPrototype
    """

    def test_project_config_prototype_serialization(self):
        """
        Test serialization/deserialization for ProjectConfigPrototype
        """

        # Construct dict forms of any model objects needed in order to build this model.

        project_compliance_profile_model = {}  # ProjectComplianceProfile
        project_compliance_profile_model['id'] = 'testString'
        project_compliance_profile_model['instance_id'] = 'testString'
        project_compliance_profile_model['instance_location'] = 'testString'
        project_compliance_profile_model['attachment_id'] = 'testString'
        project_compliance_profile_model['profile_name'] = 'testString'

        project_config_auth_model = {}  # ProjectConfigAuth
        project_config_auth_model['trusted_profile_id'] = 'testString'
        project_config_auth_model['method'] = 'api_key'
        project_config_auth_model['api_key'] = 'testString'

        project_config_definition_prototype_model = (
            {}
        )  # ProjectConfigDefinitionPrototypeDAConfigDefinitionPropertiesPrototype
        project_config_definition_prototype_model['compliance_profile'] = project_compliance_profile_model
        project_config_definition_prototype_model['locator_id'] = 'testString'
        project_config_definition_prototype_model['description'] = 'testString'
        project_config_definition_prototype_model['name'] = 'testString'
        project_config_definition_prototype_model['environment_id'] = 'testString'
        project_config_definition_prototype_model['authorizations'] = project_config_auth_model
        project_config_definition_prototype_model['inputs'] = {'anyKey': 'anyValue'}
        project_config_definition_prototype_model['settings'] = {'anyKey': 'anyValue'}

        schematics_workspace_model = {}  # SchematicsWorkspace
        schematics_workspace_model['workspace_crn'] = (
            'crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::'
        )

        # Construct a json representation of a ProjectConfigPrototype model
        project_config_prototype_model_json = {}
        project_config_prototype_model_json['definition'] = project_config_definition_prototype_model
        project_config_prototype_model_json['schematics'] = schematics_workspace_model

        # Construct a model instance of ProjectConfigPrototype by calling from_dict on the json representation
        project_config_prototype_model = ProjectConfigPrototype.from_dict(project_config_prototype_model_json)
        assert project_config_prototype_model != False

        # Construct a model instance of ProjectConfigPrototype by calling from_dict on the json representation
        project_config_prototype_model_dict = ProjectConfigPrototype.from_dict(
            project_config_prototype_model_json
        ).__dict__
        project_config_prototype_model2 = ProjectConfigPrototype(**project_config_prototype_model_dict)

        # Verify the model instances are equivalent
        assert project_config_prototype_model == project_config_prototype_model2

        # Convert model instance back to dict and verify no loss of data
        project_config_prototype_model_json2 = project_config_prototype_model.to_dict()
        assert project_config_prototype_model_json2 == project_config_prototype_model_json


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
        project_config_resource_model_json['resource_crn'] = (
            'crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::'
        )
        project_config_resource_model_json['resource_name'] = 'testString'
        project_config_resource_model_json['resource_type'] = 'testString'
        project_config_resource_model_json['resource_tainted'] = True
        project_config_resource_model_json['resource_group_name'] = 'testString'

        # Construct a model instance of ProjectConfigResource by calling from_dict on the json representation
        project_config_resource_model = ProjectConfigResource.from_dict(project_config_resource_model_json)
        assert project_config_resource_model != False

        # Construct a model instance of ProjectConfigResource by calling from_dict on the json representation
        project_config_resource_model_dict = ProjectConfigResource.from_dict(
            project_config_resource_model_json
        ).__dict__
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
        project_config_resource_model['resource_crn'] = (
            'crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::'
        )
        project_config_resource_model['resource_name'] = 'testString'
        project_config_resource_model['resource_type'] = 'testString'
        project_config_resource_model['resource_tainted'] = True
        project_config_resource_model['resource_group_name'] = 'testString'

        # Construct a json representation of a ProjectConfigResourceCollection model
        project_config_resource_collection_model_json = {}
        project_config_resource_collection_model_json['resources'] = [project_config_resource_model]
        project_config_resource_collection_model_json['resources_count'] = 38

        # Construct a model instance of ProjectConfigResourceCollection by calling from_dict on the json representation
        project_config_resource_collection_model = ProjectConfigResourceCollection.from_dict(
            project_config_resource_collection_model_json
        )
        assert project_config_resource_collection_model != False

        # Construct a model instance of ProjectConfigResourceCollection by calling from_dict on the json representation
        project_config_resource_collection_model_dict = ProjectConfigResourceCollection.from_dict(
            project_config_resource_collection_model_json
        ).__dict__
        project_config_resource_collection_model2 = ProjectConfigResourceCollection(
            **project_config_resource_collection_model_dict
        )

        # Verify the model instances are equivalent
        assert project_config_resource_collection_model == project_config_resource_collection_model2

        # Convert model instance back to dict and verify no loss of data
        project_config_resource_collection_model_json2 = project_config_resource_collection_model.to_dict()
        assert project_config_resource_collection_model_json2 == project_config_resource_collection_model_json


class TestModel_ProjectConfigSummary:
    """
    Test Class for ProjectConfigSummary
    """

    def test_project_config_summary_serialization(self):
        """
        Test serialization/deserialization for ProjectConfigSummary
        """

        # Construct dict forms of any model objects needed in order to build this model.

        project_config_version_definition_summary_model = {}  # ProjectConfigVersionDefinitionSummary
        project_config_version_definition_summary_model['environment_id'] = 'testString'
        project_config_version_definition_summary_model['locator_id'] = 'testString'

        project_config_version_summary_model = {}  # ProjectConfigVersionSummary
        project_config_version_summary_model['definition'] = project_config_version_definition_summary_model
        project_config_version_summary_model['state'] = 'approved'
        project_config_version_summary_model['version'] = 38
        project_config_version_summary_model['href'] = 'testString'

        project_config_summary_definition_model = {}  # ProjectConfigSummaryDefinition
        project_config_summary_definition_model['description'] = 'testString'
        project_config_summary_definition_model['name'] = 'testString'
        project_config_summary_definition_model['locator_id'] = 'testString'

        project_definition_reference_model = {}  # ProjectDefinitionReference
        project_definition_reference_model['name'] = 'testString'

        project_reference_model = {}  # ProjectReference
        project_reference_model['id'] = 'testString'
        project_reference_model['href'] = 'testString'
        project_reference_model['definition'] = project_definition_reference_model
        project_reference_model['crn'] = (
            'crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::'
        )

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
        project_config_summary_model_json['definition'] = project_config_summary_definition_model
        project_config_summary_model_json['project'] = project_reference_model
        project_config_summary_model_json['deployment_model'] = 'project_deployed'

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


class TestModel_ProjectConfigSummaryDefinition:
    """
    Test Class for ProjectConfigSummaryDefinition
    """

    def test_project_config_summary_definition_serialization(self):
        """
        Test serialization/deserialization for ProjectConfigSummaryDefinition
        """

        # Construct a json representation of a ProjectConfigSummaryDefinition model
        project_config_summary_definition_model_json = {}
        project_config_summary_definition_model_json['description'] = 'testString'
        project_config_summary_definition_model_json['name'] = 'testString'
        project_config_summary_definition_model_json['locator_id'] = 'testString'

        # Construct a model instance of ProjectConfigSummaryDefinition by calling from_dict on the json representation
        project_config_summary_definition_model = ProjectConfigSummaryDefinition.from_dict(
            project_config_summary_definition_model_json
        )
        assert project_config_summary_definition_model != False

        # Construct a model instance of ProjectConfigSummaryDefinition by calling from_dict on the json representation
        project_config_summary_definition_model_dict = ProjectConfigSummaryDefinition.from_dict(
            project_config_summary_definition_model_json
        ).__dict__
        project_config_summary_definition_model2 = ProjectConfigSummaryDefinition(
            **project_config_summary_definition_model_dict
        )

        # Verify the model instances are equivalent
        assert project_config_summary_definition_model == project_config_summary_definition_model2

        # Convert model instance back to dict and verify no loss of data
        project_config_summary_definition_model_json2 = project_config_summary_definition_model.to_dict()
        assert project_config_summary_definition_model_json2 == project_config_summary_definition_model_json


class TestModel_ProjectConfigVersion:
    """
    Test Class for ProjectConfigVersion
    """

    def test_project_config_version_serialization(self):
        """
        Test serialization/deserialization for ProjectConfigVersion
        """

        # Construct dict forms of any model objects needed in order to build this model.

        project_config_needs_attention_state_model = {}  # ProjectConfigNeedsAttentionState
        project_config_needs_attention_state_model['event_id'] = 'testString'
        project_config_needs_attention_state_model['event'] = 'testString'
        project_config_needs_attention_state_model['severity'] = 'INFO'
        project_config_needs_attention_state_model['action_url'] = 'testString'
        project_config_needs_attention_state_model['target'] = 'testString'
        project_config_needs_attention_state_model['triggered_by'] = 'testString'
        project_config_needs_attention_state_model['timestamp'] = 'testString'

        project_config_metadata_last_approved_model = {}  # ProjectConfigMetadataLastApproved
        project_config_metadata_last_approved_model['at'] = '2019-01-01T12:00:00Z'
        project_config_metadata_last_approved_model['comment'] = 'testString'
        project_config_metadata_last_approved_model['is_forced'] = True
        project_config_metadata_last_approved_model['user_id'] = 'testString'

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
        action_job_plan_messages_summary_model['success_messages'] = ['testString']
        action_job_plan_messages_summary_model['update_messages'] = ['testString']
        action_job_plan_messages_summary_model['destroy_messages'] = ['testString']

        terraform_log_analyzer_success_message_model = {}  # TerraformLogAnalyzerSuccessMessage
        terraform_log_analyzer_success_message_model['resource_type'] = 'testString'
        terraform_log_analyzer_success_message_model['time-taken'] = 'testString'
        terraform_log_analyzer_success_message_model['id'] = 'testString'

        action_job_apply_messages_summary_model = {}  # ActionJobApplyMessagesSummary
        action_job_apply_messages_summary_model['error_messages'] = [terraform_log_analyzer_error_message_model]
        action_job_apply_messages_summary_model['success_messages'] = [terraform_log_analyzer_success_message_model]

        action_job_destroy_messages_summary_model = {}  # ActionJobDestroyMessagesSummary
        action_job_destroy_messages_summary_model['error_messages'] = [terraform_log_analyzer_error_message_model]

        action_job_summary_model = {}  # ActionJobSummary
        action_job_summary_model['version'] = 'testString'
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

        pre_post_action_job_system_error_model = {}  # PrePostActionJobSystemError
        pre_post_action_job_system_error_model['timestamp'] = '2019-01-01T12:00:00Z'
        pre_post_action_job_system_error_model['user_id'] = 'testString'
        pre_post_action_job_system_error_model['status_code'] = 'testString'
        pre_post_action_job_system_error_model['description'] = 'testString'
        pre_post_action_job_system_error_model['error_response'] = 'testString'

        pre_post_action_job_summary_model = {}  # PrePostActionJobSummary
        pre_post_action_job_summary_model['job_id'] = 'testString'
        pre_post_action_job_summary_model['start_time'] = '2019-01-01T12:00:00Z'
        pre_post_action_job_summary_model['end_time'] = '2019-01-01T12:00:00Z'
        pre_post_action_job_summary_model['tasks'] = 38
        pre_post_action_job_summary_model['ok'] = 38
        pre_post_action_job_summary_model['failed'] = 38
        pre_post_action_job_summary_model['skipped'] = 38
        pre_post_action_job_summary_model['changed'] = 38
        pre_post_action_job_summary_model['project_error'] = pre_post_action_job_system_error_model

        pre_post_action_job_with_id_and_summary_model = {}  # PrePostActionJobWithIdAndSummary
        pre_post_action_job_with_id_and_summary_model['id'] = 'testString'
        pre_post_action_job_with_id_and_summary_model['summary'] = pre_post_action_job_summary_model

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

        project_config_metadata_code_risk_analyzer_logs_model = (
            {}
        )  # ProjectConfigMetadataCodeRiskAnalyzerLogsVersion204
        project_config_metadata_code_risk_analyzer_logs_model['cra_version'] = '2.0.4'
        project_config_metadata_code_risk_analyzer_logs_model['schema_version'] = 'testString'
        project_config_metadata_code_risk_analyzer_logs_model['status'] = 'passed'
        project_config_metadata_code_risk_analyzer_logs_model['summary'] = code_risk_analyzer_logs_summary_model
        project_config_metadata_code_risk_analyzer_logs_model['timestamp'] = '2019-01-01T12:00:00Z'

        last_validated_action_with_summary_model = {}  # LastValidatedActionWithSummary
        last_validated_action_with_summary_model['href'] = 'testString'
        last_validated_action_with_summary_model['result'] = 'failed'
        last_validated_action_with_summary_model['job'] = action_job_with_id_and_summary_model
        last_validated_action_with_summary_model['pre_job'] = pre_post_action_job_with_id_and_summary_model
        last_validated_action_with_summary_model['post_job'] = pre_post_action_job_with_id_and_summary_model
        last_validated_action_with_summary_model['cost_estimate'] = project_config_metadata_cost_estimate_model
        last_validated_action_with_summary_model['cra_logs'] = project_config_metadata_code_risk_analyzer_logs_model

        last_action_with_summary_model = {}  # LastActionWithSummary
        last_action_with_summary_model['href'] = 'testString'
        last_action_with_summary_model['result'] = 'failed'
        last_action_with_summary_model['job'] = action_job_with_id_and_summary_model
        last_action_with_summary_model['pre_job'] = pre_post_action_job_with_id_and_summary_model
        last_action_with_summary_model['post_job'] = pre_post_action_job_with_id_and_summary_model

        last_drift_detection_job_summary_model = {}  # LastDriftDetectionJobSummary
        last_drift_detection_job_summary_model['job'] = action_job_with_id_and_summary_model

        last_monitoring_action_with_summary_model = {}  # LastMonitoringActionWithSummary
        last_monitoring_action_with_summary_model['href'] = 'testString'
        last_monitoring_action_with_summary_model['result'] = 'failed'
        last_monitoring_action_with_summary_model['drift_detection'] = last_drift_detection_job_summary_model

        output_value_model = {}  # OutputValue
        output_value_model['name'] = 'testString'
        output_value_model['description'] = 'testString'
        output_value_model['value'] = 'testString'

        project_definition_reference_model = {}  # ProjectDefinitionReference
        project_definition_reference_model['name'] = 'testString'

        project_reference_model = {}  # ProjectReference
        project_reference_model['id'] = 'testString'
        project_reference_model['href'] = 'testString'
        project_reference_model['definition'] = project_definition_reference_model
        project_reference_model['crn'] = (
            'crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::'
        )

        script_model = {}  # Script
        script_model['type'] = 'ansible'
        script_model['path'] = 'scripts/validate-post-ansible-playbook.yaml'
        script_model['short_description'] = 'testString'

        schematics_metadata_model = {}  # SchematicsMetadata
        schematics_metadata_model['workspace_crn'] = (
            'crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::'
        )
        schematics_metadata_model['validate_pre_script'] = script_model
        schematics_metadata_model['validate_post_script'] = script_model
        schematics_metadata_model['deploy_pre_script'] = script_model
        schematics_metadata_model['deploy_post_script'] = script_model
        schematics_metadata_model['undeploy_pre_script'] = script_model
        schematics_metadata_model['undeploy_post_script'] = script_model

        project_object_reference_model = {}  # ProjectObjectReference
        project_object_reference_model['id'] = 'testString'
        project_object_reference_model['href'] = 'testString'

        project_compliance_profile_model = {}  # ProjectComplianceProfile
        project_compliance_profile_model['id'] = 'testString'
        project_compliance_profile_model['instance_id'] = 'testString'
        project_compliance_profile_model['instance_location'] = 'testString'
        project_compliance_profile_model['attachment_id'] = 'testString'
        project_compliance_profile_model['profile_name'] = 'testString'

        project_config_auth_model = {}  # ProjectConfigAuth
        project_config_auth_model['trusted_profile_id'] = 'testString'
        project_config_auth_model['method'] = 'api_key'
        project_config_auth_model['api_key'] = 'testString'

        project_config_definition_response_model = (
            {}
        )  # ProjectConfigDefinitionResponseDAConfigDefinitionPropertiesResponse
        project_config_definition_response_model['compliance_profile'] = project_compliance_profile_model
        project_config_definition_response_model['locator_id'] = 'testString'
        project_config_definition_response_model['description'] = 'testString'
        project_config_definition_response_model['name'] = 'testString'
        project_config_definition_response_model['environment_id'] = 'testString'
        project_config_definition_response_model['authorizations'] = project_config_auth_model
        project_config_definition_response_model['inputs'] = {'anyKey': 'anyValue'}
        project_config_definition_response_model['settings'] = {'anyKey': 'anyValue'}

        # Construct a json representation of a ProjectConfigVersion model
        project_config_version_model_json = {}
        project_config_version_model_json['id'] = 'testString'
        project_config_version_model_json['version'] = 38
        project_config_version_model_json['is_draft'] = True
        project_config_version_model_json['needs_attention_state'] = [project_config_needs_attention_state_model]
        project_config_version_model_json['created_at'] = '2019-01-01T12:00:00Z'
        project_config_version_model_json['modified_at'] = '2019-01-01T12:00:00Z'
        project_config_version_model_json['last_approved'] = project_config_metadata_last_approved_model
        project_config_version_model_json['last_saved_at'] = '2019-01-01T12:00:00Z'
        project_config_version_model_json['last_validated'] = last_validated_action_with_summary_model
        project_config_version_model_json['last_deployed'] = last_action_with_summary_model
        project_config_version_model_json['last_undeployed'] = last_action_with_summary_model
        project_config_version_model_json['last_monitoring'] = last_monitoring_action_with_summary_model
        project_config_version_model_json['outputs'] = [output_value_model]
        project_config_version_model_json['project'] = project_reference_model
        project_config_version_model_json['references'] = {'anyKey': 'anyValue'}
        project_config_version_model_json['schematics'] = schematics_metadata_model
        project_config_version_model_json['state'] = 'approved'
        project_config_version_model_json['update_available'] = True
        project_config_version_model_json['template'] = project_object_reference_model
        project_config_version_model_json['href'] = 'testString'
        project_config_version_model_json['definition'] = project_config_definition_response_model

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


class TestModel_ProjectConfigVersionDefinitionSummary:
    """
    Test Class for ProjectConfigVersionDefinitionSummary
    """

    def test_project_config_version_definition_summary_serialization(self):
        """
        Test serialization/deserialization for ProjectConfigVersionDefinitionSummary
        """

        # Construct a json representation of a ProjectConfigVersionDefinitionSummary model
        project_config_version_definition_summary_model_json = {}
        project_config_version_definition_summary_model_json['environment_id'] = 'testString'
        project_config_version_definition_summary_model_json['locator_id'] = 'testString'

        # Construct a model instance of ProjectConfigVersionDefinitionSummary by calling from_dict on the json representation
        project_config_version_definition_summary_model = ProjectConfigVersionDefinitionSummary.from_dict(
            project_config_version_definition_summary_model_json
        )
        assert project_config_version_definition_summary_model != False

        # Construct a model instance of ProjectConfigVersionDefinitionSummary by calling from_dict on the json representation
        project_config_version_definition_summary_model_dict = ProjectConfigVersionDefinitionSummary.from_dict(
            project_config_version_definition_summary_model_json
        ).__dict__
        project_config_version_definition_summary_model2 = ProjectConfigVersionDefinitionSummary(
            **project_config_version_definition_summary_model_dict
        )

        # Verify the model instances are equivalent
        assert project_config_version_definition_summary_model == project_config_version_definition_summary_model2

        # Convert model instance back to dict and verify no loss of data
        project_config_version_definition_summary_model_json2 = (
            project_config_version_definition_summary_model.to_dict()
        )
        assert (
            project_config_version_definition_summary_model_json2
            == project_config_version_definition_summary_model_json
        )


class TestModel_ProjectConfigVersionSummary:
    """
    Test Class for ProjectConfigVersionSummary
    """

    def test_project_config_version_summary_serialization(self):
        """
        Test serialization/deserialization for ProjectConfigVersionSummary
        """

        # Construct dict forms of any model objects needed in order to build this model.

        project_config_version_definition_summary_model = {}  # ProjectConfigVersionDefinitionSummary
        project_config_version_definition_summary_model['environment_id'] = 'testString'
        project_config_version_definition_summary_model['locator_id'] = 'testString'

        # Construct a json representation of a ProjectConfigVersionSummary model
        project_config_version_summary_model_json = {}
        project_config_version_summary_model_json['definition'] = project_config_version_definition_summary_model
        project_config_version_summary_model_json['state'] = 'approved'
        project_config_version_summary_model_json['version'] = 38
        project_config_version_summary_model_json['href'] = 'testString'

        # Construct a model instance of ProjectConfigVersionSummary by calling from_dict on the json representation
        project_config_version_summary_model = ProjectConfigVersionSummary.from_dict(
            project_config_version_summary_model_json
        )
        assert project_config_version_summary_model != False

        # Construct a model instance of ProjectConfigVersionSummary by calling from_dict on the json representation
        project_config_version_summary_model_dict = ProjectConfigVersionSummary.from_dict(
            project_config_version_summary_model_json
        ).__dict__
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

        project_config_version_definition_summary_model = {}  # ProjectConfigVersionDefinitionSummary
        project_config_version_definition_summary_model['environment_id'] = 'testString'
        project_config_version_definition_summary_model['locator_id'] = 'testString'

        project_config_version_summary_model = {}  # ProjectConfigVersionSummary
        project_config_version_summary_model['definition'] = project_config_version_definition_summary_model
        project_config_version_summary_model['state'] = 'approved'
        project_config_version_summary_model['version'] = 38
        project_config_version_summary_model['href'] = 'testString'

        # Construct a json representation of a ProjectConfigVersionSummaryCollection model
        project_config_version_summary_collection_model_json = {}
        project_config_version_summary_collection_model_json['versions'] = [project_config_version_summary_model]

        # Construct a model instance of ProjectConfigVersionSummaryCollection by calling from_dict on the json representation
        project_config_version_summary_collection_model = ProjectConfigVersionSummaryCollection.from_dict(
            project_config_version_summary_collection_model_json
        )
        assert project_config_version_summary_collection_model != False

        # Construct a model instance of ProjectConfigVersionSummaryCollection by calling from_dict on the json representation
        project_config_version_summary_collection_model_dict = ProjectConfigVersionSummaryCollection.from_dict(
            project_config_version_summary_collection_model_json
        ).__dict__
        project_config_version_summary_collection_model2 = ProjectConfigVersionSummaryCollection(
            **project_config_version_summary_collection_model_dict
        )

        # Verify the model instances are equivalent
        assert project_config_version_summary_collection_model == project_config_version_summary_collection_model2

        # Convert model instance back to dict and verify no loss of data
        project_config_version_summary_collection_model_json2 = (
            project_config_version_summary_collection_model.to_dict()
        )
        assert (
            project_config_version_summary_collection_model_json2
            == project_config_version_summary_collection_model_json
        )


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
        project_definition_properties_model_json['destroy_on_delete'] = True
        project_definition_properties_model_json['description'] = 'testString'
        project_definition_properties_model_json['monitoring_enabled'] = False

        # Construct a model instance of ProjectDefinitionProperties by calling from_dict on the json representation
        project_definition_properties_model = ProjectDefinitionProperties.from_dict(
            project_definition_properties_model_json
        )
        assert project_definition_properties_model != False

        # Construct a model instance of ProjectDefinitionProperties by calling from_dict on the json representation
        project_definition_properties_model_dict = ProjectDefinitionProperties.from_dict(
            project_definition_properties_model_json
        ).__dict__
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
        project_definition_reference_model = ProjectDefinitionReference.from_dict(
            project_definition_reference_model_json
        )
        assert project_definition_reference_model != False

        # Construct a model instance of ProjectDefinitionReference by calling from_dict on the json representation
        project_definition_reference_model_dict = ProjectDefinitionReference.from_dict(
            project_definition_reference_model_json
        ).__dict__
        project_definition_reference_model2 = ProjectDefinitionReference(**project_definition_reference_model_dict)

        # Verify the model instances are equivalent
        assert project_definition_reference_model == project_definition_reference_model2

        # Convert model instance back to dict and verify no loss of data
        project_definition_reference_model_json2 = project_definition_reference_model.to_dict()
        assert project_definition_reference_model_json2 == project_definition_reference_model_json


class TestModel_ProjectDeleteResponse:
    """
    Test Class for ProjectDeleteResponse
    """

    def test_project_delete_response_serialization(self):
        """
        Test serialization/deserialization for ProjectDeleteResponse
        """

        # Construct a json representation of a ProjectDeleteResponse model
        project_delete_response_model_json = {}
        project_delete_response_model_json['id'] = 'testString'

        # Construct a model instance of ProjectDeleteResponse by calling from_dict on the json representation
        project_delete_response_model = ProjectDeleteResponse.from_dict(project_delete_response_model_json)
        assert project_delete_response_model != False

        # Construct a model instance of ProjectDeleteResponse by calling from_dict on the json representation
        project_delete_response_model_dict = ProjectDeleteResponse.from_dict(
            project_delete_response_model_json
        ).__dict__
        project_delete_response_model2 = ProjectDeleteResponse(**project_delete_response_model_dict)

        # Verify the model instances are equivalent
        assert project_delete_response_model == project_delete_response_model2

        # Convert model instance back to dict and verify no loss of data
        project_delete_response_model_json2 = project_delete_response_model.to_dict()
        assert project_delete_response_model_json2 == project_delete_response_model_json


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
        project_reference_model['href'] = 'testString'
        project_reference_model['definition'] = project_definition_reference_model
        project_reference_model['crn'] = (
            'crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::'
        )

        project_environment_summary_definition_model = {}  # ProjectEnvironmentSummaryDefinition
        project_environment_summary_definition_model['description'] = 'testString'
        project_environment_summary_definition_model['name'] = 'testString'

        # Construct a json representation of a ProjectEnvironmentSummary model
        project_environment_summary_model_json = {}
        project_environment_summary_model_json['id'] = 'testString'
        project_environment_summary_model_json['project'] = project_reference_model
        project_environment_summary_model_json['created_at'] = '2019-01-01T12:00:00Z'
        project_environment_summary_model_json['href'] = 'testString'
        project_environment_summary_model_json['definition'] = project_environment_summary_definition_model

        # Construct a model instance of ProjectEnvironmentSummary by calling from_dict on the json representation
        project_environment_summary_model = ProjectEnvironmentSummary.from_dict(project_environment_summary_model_json)
        assert project_environment_summary_model != False

        # Construct a model instance of ProjectEnvironmentSummary by calling from_dict on the json representation
        project_environment_summary_model_dict = ProjectEnvironmentSummary.from_dict(
            project_environment_summary_model_json
        ).__dict__
        project_environment_summary_model2 = ProjectEnvironmentSummary(**project_environment_summary_model_dict)

        # Verify the model instances are equivalent
        assert project_environment_summary_model == project_environment_summary_model2

        # Convert model instance back to dict and verify no loss of data
        project_environment_summary_model_json2 = project_environment_summary_model.to_dict()
        assert project_environment_summary_model_json2 == project_environment_summary_model_json


class TestModel_ProjectEnvironmentSummaryDefinition:
    """
    Test Class for ProjectEnvironmentSummaryDefinition
    """

    def test_project_environment_summary_definition_serialization(self):
        """
        Test serialization/deserialization for ProjectEnvironmentSummaryDefinition
        """

        # Construct a json representation of a ProjectEnvironmentSummaryDefinition model
        project_environment_summary_definition_model_json = {}
        project_environment_summary_definition_model_json['description'] = 'testString'
        project_environment_summary_definition_model_json['name'] = 'testString'

        # Construct a model instance of ProjectEnvironmentSummaryDefinition by calling from_dict on the json representation
        project_environment_summary_definition_model = ProjectEnvironmentSummaryDefinition.from_dict(
            project_environment_summary_definition_model_json
        )
        assert project_environment_summary_definition_model != False

        # Construct a model instance of ProjectEnvironmentSummaryDefinition by calling from_dict on the json representation
        project_environment_summary_definition_model_dict = ProjectEnvironmentSummaryDefinition.from_dict(
            project_environment_summary_definition_model_json
        ).__dict__
        project_environment_summary_definition_model2 = ProjectEnvironmentSummaryDefinition(
            **project_environment_summary_definition_model_dict
        )

        # Verify the model instances are equivalent
        assert project_environment_summary_definition_model == project_environment_summary_definition_model2

        # Convert model instance back to dict and verify no loss of data
        project_environment_summary_definition_model_json2 = project_environment_summary_definition_model.to_dict()
        assert project_environment_summary_definition_model_json2 == project_environment_summary_definition_model_json


class TestModel_ProjectObjectReference:
    """
    Test Class for ProjectObjectReference
    """

    def test_project_object_reference_serialization(self):
        """
        Test serialization/deserialization for ProjectObjectReference
        """

        # Construct a json representation of a ProjectObjectReference model
        project_object_reference_model_json = {}
        project_object_reference_model_json['id'] = 'testString'
        project_object_reference_model_json['href'] = 'testString'

        # Construct a model instance of ProjectObjectReference by calling from_dict on the json representation
        project_object_reference_model = ProjectObjectReference.from_dict(project_object_reference_model_json)
        assert project_object_reference_model != False

        # Construct a model instance of ProjectObjectReference by calling from_dict on the json representation
        project_object_reference_model_dict = ProjectObjectReference.from_dict(
            project_object_reference_model_json
        ).__dict__
        project_object_reference_model2 = ProjectObjectReference(**project_object_reference_model_dict)

        # Verify the model instances are equivalent
        assert project_object_reference_model == project_object_reference_model2

        # Convert model instance back to dict and verify no loss of data
        project_object_reference_model_json2 = project_object_reference_model.to_dict()
        assert project_object_reference_model_json2 == project_object_reference_model_json


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
        project_patch_definition_block_model_json['destroy_on_delete'] = True
        project_patch_definition_block_model_json['description'] = 'testString'
        project_patch_definition_block_model_json['monitoring_enabled'] = True

        # Construct a model instance of ProjectPatchDefinitionBlock by calling from_dict on the json representation
        project_patch_definition_block_model = ProjectPatchDefinitionBlock.from_dict(
            project_patch_definition_block_model_json
        )
        assert project_patch_definition_block_model != False

        # Construct a model instance of ProjectPatchDefinitionBlock by calling from_dict on the json representation
        project_patch_definition_block_model_dict = ProjectPatchDefinitionBlock.from_dict(
            project_patch_definition_block_model_json
        ).__dict__
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
        project_prototype_definition_model_json['destroy_on_delete'] = True
        project_prototype_definition_model_json['description'] = 'testString'
        project_prototype_definition_model_json['monitoring_enabled'] = False

        # Construct a model instance of ProjectPrototypeDefinition by calling from_dict on the json representation
        project_prototype_definition_model = ProjectPrototypeDefinition.from_dict(
            project_prototype_definition_model_json
        )
        assert project_prototype_definition_model != False

        # Construct a model instance of ProjectPrototypeDefinition by calling from_dict on the json representation
        project_prototype_definition_model_dict = ProjectPrototypeDefinition.from_dict(
            project_prototype_definition_model_json
        ).__dict__
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
        project_reference_model_json['href'] = 'testString'
        project_reference_model_json['definition'] = project_definition_reference_model
        project_reference_model_json['crn'] = (
            'crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::'
        )

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
        project_definition_properties_model['destroy_on_delete'] = True
        project_definition_properties_model['description'] = 'testString'
        project_definition_properties_model['monitoring_enabled'] = False

        # Construct a json representation of a ProjectSummary model
        project_summary_model_json = {}
        project_summary_model_json['crn'] = (
            'crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::'
        )
        project_summary_model_json['created_at'] = '2019-01-01T12:00:00Z'
        project_summary_model_json['cumulative_needs_attention_view'] = [cumulative_needs_attention_model]
        project_summary_model_json['cumulative_needs_attention_view_error'] = False
        project_summary_model_json['id'] = 'testString'
        project_summary_model_json['location'] = 'testString'
        project_summary_model_json['resource_group_id'] = 'testString'
        project_summary_model_json['state'] = 'ready'
        project_summary_model_json['href'] = 'testString'
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


class TestModel_SchematicsMetadata:
    """
    Test Class for SchematicsMetadata
    """

    def test_schematics_metadata_serialization(self):
        """
        Test serialization/deserialization for SchematicsMetadata
        """

        # Construct dict forms of any model objects needed in order to build this model.

        script_model = {}  # Script
        script_model['type'] = 'ansible'
        script_model['path'] = 'scripts/validate-post-ansible-playbook.yaml'
        script_model['short_description'] = 'testString'

        # Construct a json representation of a SchematicsMetadata model
        schematics_metadata_model_json = {}
        schematics_metadata_model_json['workspace_crn'] = (
            'crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::'
        )
        schematics_metadata_model_json['validate_pre_script'] = script_model
        schematics_metadata_model_json['validate_post_script'] = script_model
        schematics_metadata_model_json['deploy_pre_script'] = script_model
        schematics_metadata_model_json['deploy_post_script'] = script_model
        schematics_metadata_model_json['undeploy_pre_script'] = script_model
        schematics_metadata_model_json['undeploy_post_script'] = script_model

        # Construct a model instance of SchematicsMetadata by calling from_dict on the json representation
        schematics_metadata_model = SchematicsMetadata.from_dict(schematics_metadata_model_json)
        assert schematics_metadata_model != False

        # Construct a model instance of SchematicsMetadata by calling from_dict on the json representation
        schematics_metadata_model_dict = SchematicsMetadata.from_dict(schematics_metadata_model_json).__dict__
        schematics_metadata_model2 = SchematicsMetadata(**schematics_metadata_model_dict)

        # Verify the model instances are equivalent
        assert schematics_metadata_model == schematics_metadata_model2

        # Convert model instance back to dict and verify no loss of data
        schematics_metadata_model_json2 = schematics_metadata_model.to_dict()
        assert schematics_metadata_model_json2 == schematics_metadata_model_json


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
        schematics_workspace_model_json['workspace_crn'] = (
            'crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::'
        )

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


class TestModel_Script:
    """
    Test Class for Script
    """

    def test_script_serialization(self):
        """
        Test serialization/deserialization for Script
        """

        # Construct a json representation of a Script model
        script_model_json = {}
        script_model_json['type'] = 'ansible'
        script_model_json['path'] = 'scripts/validate-post-ansible-playbook.yaml'
        script_model_json['short_description'] = 'testString'

        # Construct a model instance of Script by calling from_dict on the json representation
        script_model = Script.from_dict(script_model_json)
        assert script_model != False

        # Construct a model instance of Script by calling from_dict on the json representation
        script_model_dict = Script.from_dict(script_model_json).__dict__
        script_model2 = Script(**script_model_dict)

        # Verify the model instances are equivalent
        assert script_model == script_model2

        # Convert model instance back to dict and verify no loss of data
        script_model_json2 = script_model.to_dict()
        assert script_model_json2 == script_model_json


class TestModel_StackConfigMember:
    """
    Test Class for StackConfigMember
    """

    def test_stack_config_member_serialization(self):
        """
        Test serialization/deserialization for StackConfigMember
        """

        # Construct a json representation of a StackConfigMember model
        stack_config_member_model_json = {}
        stack_config_member_model_json['name'] = 'testString'
        stack_config_member_model_json['config_id'] = 'testString'

        # Construct a model instance of StackConfigMember by calling from_dict on the json representation
        stack_config_member_model = StackConfigMember.from_dict(stack_config_member_model_json)
        assert stack_config_member_model != False

        # Construct a model instance of StackConfigMember by calling from_dict on the json representation
        stack_config_member_model_dict = StackConfigMember.from_dict(stack_config_member_model_json).__dict__
        stack_config_member_model2 = StackConfigMember(**stack_config_member_model_dict)

        # Verify the model instances are equivalent
        assert stack_config_member_model == stack_config_member_model2

        # Convert model instance back to dict and verify no loss of data
        stack_config_member_model_json2 = stack_config_member_model.to_dict()
        assert stack_config_member_model_json2 == stack_config_member_model_json


class TestModel_StackDefinition:
    """
    Test Class for StackDefinition
    """

    def test_stack_definition_serialization(self):
        """
        Test serialization/deserialization for StackDefinition
        """

        # Construct dict forms of any model objects needed in order to build this model.

        config_definition_reference_model = {}  # ConfigDefinitionReference
        config_definition_reference_model['name'] = 'testString'

        stack_definition_metadata_configuration_model = {}  # StackDefinitionMetadataConfiguration
        stack_definition_metadata_configuration_model['id'] = 'testString'
        stack_definition_metadata_configuration_model['href'] = 'testString'
        stack_definition_metadata_configuration_model['definition'] = config_definition_reference_model

        stack_definition_input_variable_model = {}  # StackDefinitionInputVariable
        stack_definition_input_variable_model['name'] = 'testString'
        stack_definition_input_variable_model['type'] = 'array'
        stack_definition_input_variable_model['description'] = 'testString'
        stack_definition_input_variable_model['default'] = 'testString'
        stack_definition_input_variable_model['required'] = True
        stack_definition_input_variable_model['hidden'] = True

        stack_definition_output_variable_model = {}  # StackDefinitionOutputVariable
        stack_definition_output_variable_model['name'] = 'testString'
        stack_definition_output_variable_model['value'] = 'testString'

        stack_definition_member_input_model = {}  # StackDefinitionMemberInput
        stack_definition_member_input_model['name'] = 'testString'
        stack_definition_member_input_model['value'] = 'testString'

        stack_definition_member_model = {}  # StackDefinitionMember
        stack_definition_member_model['name'] = 'testString'
        stack_definition_member_model['version_locator'] = 'testString'
        stack_definition_member_model['inputs'] = [stack_definition_member_input_model]

        stack_definition_block_model = {}  # StackDefinitionBlock
        stack_definition_block_model['inputs'] = [stack_definition_input_variable_model]
        stack_definition_block_model['outputs'] = [stack_definition_output_variable_model]
        stack_definition_block_model['members'] = [stack_definition_member_model]

        # Construct a json representation of a StackDefinition model
        stack_definition_model_json = {}
        stack_definition_model_json['id'] = 'testString'
        stack_definition_model_json['created_at'] = '2019-01-01T12:00:00Z'
        stack_definition_model_json['modified_at'] = '2019-01-01T12:00:00Z'
        stack_definition_model_json['state'] = 'draft'
        stack_definition_model_json['configuration'] = stack_definition_metadata_configuration_model
        stack_definition_model_json['href'] = 'testString'
        stack_definition_model_json['stack_definition'] = stack_definition_block_model

        # Construct a model instance of StackDefinition by calling from_dict on the json representation
        stack_definition_model = StackDefinition.from_dict(stack_definition_model_json)
        assert stack_definition_model != False

        # Construct a model instance of StackDefinition by calling from_dict on the json representation
        stack_definition_model_dict = StackDefinition.from_dict(stack_definition_model_json).__dict__
        stack_definition_model2 = StackDefinition(**stack_definition_model_dict)

        # Verify the model instances are equivalent
        assert stack_definition_model == stack_definition_model2

        # Convert model instance back to dict and verify no loss of data
        stack_definition_model_json2 = stack_definition_model.to_dict()
        assert stack_definition_model_json2 == stack_definition_model_json


class TestModel_StackDefinitionBlock:
    """
    Test Class for StackDefinitionBlock
    """

    def test_stack_definition_block_serialization(self):
        """
        Test serialization/deserialization for StackDefinitionBlock
        """

        # Construct dict forms of any model objects needed in order to build this model.

        stack_definition_input_variable_model = {}  # StackDefinitionInputVariable
        stack_definition_input_variable_model['name'] = 'testString'
        stack_definition_input_variable_model['type'] = 'array'
        stack_definition_input_variable_model['description'] = 'testString'
        stack_definition_input_variable_model['default'] = 'testString'
        stack_definition_input_variable_model['required'] = True
        stack_definition_input_variable_model['hidden'] = True

        stack_definition_output_variable_model = {}  # StackDefinitionOutputVariable
        stack_definition_output_variable_model['name'] = 'testString'
        stack_definition_output_variable_model['value'] = 'testString'

        stack_definition_member_input_model = {}  # StackDefinitionMemberInput
        stack_definition_member_input_model['name'] = 'testString'
        stack_definition_member_input_model['value'] = 'testString'

        stack_definition_member_model = {}  # StackDefinitionMember
        stack_definition_member_model['name'] = 'testString'
        stack_definition_member_model['version_locator'] = 'testString'
        stack_definition_member_model['inputs'] = [stack_definition_member_input_model]

        # Construct a json representation of a StackDefinitionBlock model
        stack_definition_block_model_json = {}
        stack_definition_block_model_json['inputs'] = [stack_definition_input_variable_model]
        stack_definition_block_model_json['outputs'] = [stack_definition_output_variable_model]
        stack_definition_block_model_json['members'] = [stack_definition_member_model]

        # Construct a model instance of StackDefinitionBlock by calling from_dict on the json representation
        stack_definition_block_model = StackDefinitionBlock.from_dict(stack_definition_block_model_json)
        assert stack_definition_block_model != False

        # Construct a model instance of StackDefinitionBlock by calling from_dict on the json representation
        stack_definition_block_model_dict = StackDefinitionBlock.from_dict(stack_definition_block_model_json).__dict__
        stack_definition_block_model2 = StackDefinitionBlock(**stack_definition_block_model_dict)

        # Verify the model instances are equivalent
        assert stack_definition_block_model == stack_definition_block_model2

        # Convert model instance back to dict and verify no loss of data
        stack_definition_block_model_json2 = stack_definition_block_model.to_dict()
        assert stack_definition_block_model_json2 == stack_definition_block_model_json


class TestModel_StackDefinitionBlockPrototype:
    """
    Test Class for StackDefinitionBlockPrototype
    """

    def test_stack_definition_block_prototype_serialization(self):
        """
        Test serialization/deserialization for StackDefinitionBlockPrototype
        """

        # Construct dict forms of any model objects needed in order to build this model.

        stack_definition_input_variable_model = {}  # StackDefinitionInputVariable
        stack_definition_input_variable_model['name'] = 'testString'
        stack_definition_input_variable_model['type'] = 'array'
        stack_definition_input_variable_model['description'] = 'testString'
        stack_definition_input_variable_model['default'] = 'testString'
        stack_definition_input_variable_model['required'] = True
        stack_definition_input_variable_model['hidden'] = True

        stack_definition_output_variable_model = {}  # StackDefinitionOutputVariable
        stack_definition_output_variable_model['name'] = 'testString'
        stack_definition_output_variable_model['value'] = 'testString'

        stack_definition_member_input_prototype_model = {}  # StackDefinitionMemberInputPrototype
        stack_definition_member_input_prototype_model['name'] = 'testString'

        stack_definition_member_prototype_model = {}  # StackDefinitionMemberPrototype
        stack_definition_member_prototype_model['name'] = 'testString'
        stack_definition_member_prototype_model['inputs'] = [stack_definition_member_input_prototype_model]

        # Construct a json representation of a StackDefinitionBlockPrototype model
        stack_definition_block_prototype_model_json = {}
        stack_definition_block_prototype_model_json['inputs'] = [stack_definition_input_variable_model]
        stack_definition_block_prototype_model_json['outputs'] = [stack_definition_output_variable_model]
        stack_definition_block_prototype_model_json['members'] = [stack_definition_member_prototype_model]

        # Construct a model instance of StackDefinitionBlockPrototype by calling from_dict on the json representation
        stack_definition_block_prototype_model = StackDefinitionBlockPrototype.from_dict(
            stack_definition_block_prototype_model_json
        )
        assert stack_definition_block_prototype_model != False

        # Construct a model instance of StackDefinitionBlockPrototype by calling from_dict on the json representation
        stack_definition_block_prototype_model_dict = StackDefinitionBlockPrototype.from_dict(
            stack_definition_block_prototype_model_json
        ).__dict__
        stack_definition_block_prototype_model2 = StackDefinitionBlockPrototype(
            **stack_definition_block_prototype_model_dict
        )

        # Verify the model instances are equivalent
        assert stack_definition_block_prototype_model == stack_definition_block_prototype_model2

        # Convert model instance back to dict and verify no loss of data
        stack_definition_block_prototype_model_json2 = stack_definition_block_prototype_model.to_dict()
        assert stack_definition_block_prototype_model_json2 == stack_definition_block_prototype_model_json


class TestModel_StackDefinitionExportResponse:
    """
    Test Class for StackDefinitionExportResponse
    """

    def test_stack_definition_export_response_serialization(self):
        """
        Test serialization/deserialization for StackDefinitionExportResponse
        """

        # Construct a json representation of a StackDefinitionExportResponse model
        stack_definition_export_response_model_json = {}
        stack_definition_export_response_model_json['catalog_id'] = 'testString'
        stack_definition_export_response_model_json['product_id'] = 'testString'
        stack_definition_export_response_model_json['version_locator'] = 'testString'
        stack_definition_export_response_model_json['kind'] = 'testString'
        stack_definition_export_response_model_json['format'] = 'testString'

        # Construct a model instance of StackDefinitionExportResponse by calling from_dict on the json representation
        stack_definition_export_response_model = StackDefinitionExportResponse.from_dict(
            stack_definition_export_response_model_json
        )
        assert stack_definition_export_response_model != False

        # Construct a model instance of StackDefinitionExportResponse by calling from_dict on the json representation
        stack_definition_export_response_model_dict = StackDefinitionExportResponse.from_dict(
            stack_definition_export_response_model_json
        ).__dict__
        stack_definition_export_response_model2 = StackDefinitionExportResponse(
            **stack_definition_export_response_model_dict
        )

        # Verify the model instances are equivalent
        assert stack_definition_export_response_model == stack_definition_export_response_model2

        # Convert model instance back to dict and verify no loss of data
        stack_definition_export_response_model_json2 = stack_definition_export_response_model.to_dict()
        assert stack_definition_export_response_model_json2 == stack_definition_export_response_model_json


class TestModel_StackDefinitionInputVariable:
    """
    Test Class for StackDefinitionInputVariable
    """

    def test_stack_definition_input_variable_serialization(self):
        """
        Test serialization/deserialization for StackDefinitionInputVariable
        """

        # Construct a json representation of a StackDefinitionInputVariable model
        stack_definition_input_variable_model_json = {}
        stack_definition_input_variable_model_json['name'] = 'testString'
        stack_definition_input_variable_model_json['type'] = 'array'
        stack_definition_input_variable_model_json['description'] = 'testString'
        stack_definition_input_variable_model_json['default'] = 'testString'
        stack_definition_input_variable_model_json['required'] = True
        stack_definition_input_variable_model_json['hidden'] = True

        # Construct a model instance of StackDefinitionInputVariable by calling from_dict on the json representation
        stack_definition_input_variable_model = StackDefinitionInputVariable.from_dict(
            stack_definition_input_variable_model_json
        )
        assert stack_definition_input_variable_model != False

        # Construct a model instance of StackDefinitionInputVariable by calling from_dict on the json representation
        stack_definition_input_variable_model_dict = StackDefinitionInputVariable.from_dict(
            stack_definition_input_variable_model_json
        ).__dict__
        stack_definition_input_variable_model2 = StackDefinitionInputVariable(
            **stack_definition_input_variable_model_dict
        )

        # Verify the model instances are equivalent
        assert stack_definition_input_variable_model == stack_definition_input_variable_model2

        # Convert model instance back to dict and verify no loss of data
        stack_definition_input_variable_model_json2 = stack_definition_input_variable_model.to_dict()
        assert stack_definition_input_variable_model_json2 == stack_definition_input_variable_model_json


class TestModel_StackDefinitionMember:
    """
    Test Class for StackDefinitionMember
    """

    def test_stack_definition_member_serialization(self):
        """
        Test serialization/deserialization for StackDefinitionMember
        """

        # Construct dict forms of any model objects needed in order to build this model.

        stack_definition_member_input_model = {}  # StackDefinitionMemberInput
        stack_definition_member_input_model['name'] = 'testString'
        stack_definition_member_input_model['value'] = 'testString'

        # Construct a json representation of a StackDefinitionMember model
        stack_definition_member_model_json = {}
        stack_definition_member_model_json['name'] = 'testString'
        stack_definition_member_model_json['version_locator'] = 'testString'
        stack_definition_member_model_json['inputs'] = [stack_definition_member_input_model]

        # Construct a model instance of StackDefinitionMember by calling from_dict on the json representation
        stack_definition_member_model = StackDefinitionMember.from_dict(stack_definition_member_model_json)
        assert stack_definition_member_model != False

        # Construct a model instance of StackDefinitionMember by calling from_dict on the json representation
        stack_definition_member_model_dict = StackDefinitionMember.from_dict(
            stack_definition_member_model_json
        ).__dict__
        stack_definition_member_model2 = StackDefinitionMember(**stack_definition_member_model_dict)

        # Verify the model instances are equivalent
        assert stack_definition_member_model == stack_definition_member_model2

        # Convert model instance back to dict and verify no loss of data
        stack_definition_member_model_json2 = stack_definition_member_model.to_dict()
        assert stack_definition_member_model_json2 == stack_definition_member_model_json


class TestModel_StackDefinitionMemberInput:
    """
    Test Class for StackDefinitionMemberInput
    """

    def test_stack_definition_member_input_serialization(self):
        """
        Test serialization/deserialization for StackDefinitionMemberInput
        """

        # Construct a json representation of a StackDefinitionMemberInput model
        stack_definition_member_input_model_json = {}
        stack_definition_member_input_model_json['name'] = 'testString'
        stack_definition_member_input_model_json['value'] = 'testString'

        # Construct a model instance of StackDefinitionMemberInput by calling from_dict on the json representation
        stack_definition_member_input_model = StackDefinitionMemberInput.from_dict(
            stack_definition_member_input_model_json
        )
        assert stack_definition_member_input_model != False

        # Construct a model instance of StackDefinitionMemberInput by calling from_dict on the json representation
        stack_definition_member_input_model_dict = StackDefinitionMemberInput.from_dict(
            stack_definition_member_input_model_json
        ).__dict__
        stack_definition_member_input_model2 = StackDefinitionMemberInput(**stack_definition_member_input_model_dict)

        # Verify the model instances are equivalent
        assert stack_definition_member_input_model == stack_definition_member_input_model2

        # Convert model instance back to dict and verify no loss of data
        stack_definition_member_input_model_json2 = stack_definition_member_input_model.to_dict()
        assert stack_definition_member_input_model_json2 == stack_definition_member_input_model_json


class TestModel_StackDefinitionMemberInputPrototype:
    """
    Test Class for StackDefinitionMemberInputPrototype
    """

    def test_stack_definition_member_input_prototype_serialization(self):
        """
        Test serialization/deserialization for StackDefinitionMemberInputPrototype
        """

        # Construct a json representation of a StackDefinitionMemberInputPrototype model
        stack_definition_member_input_prototype_model_json = {}
        stack_definition_member_input_prototype_model_json['name'] = 'testString'

        # Construct a model instance of StackDefinitionMemberInputPrototype by calling from_dict on the json representation
        stack_definition_member_input_prototype_model = StackDefinitionMemberInputPrototype.from_dict(
            stack_definition_member_input_prototype_model_json
        )
        assert stack_definition_member_input_prototype_model != False

        # Construct a model instance of StackDefinitionMemberInputPrototype by calling from_dict on the json representation
        stack_definition_member_input_prototype_model_dict = StackDefinitionMemberInputPrototype.from_dict(
            stack_definition_member_input_prototype_model_json
        ).__dict__
        stack_definition_member_input_prototype_model2 = StackDefinitionMemberInputPrototype(
            **stack_definition_member_input_prototype_model_dict
        )

        # Verify the model instances are equivalent
        assert stack_definition_member_input_prototype_model == stack_definition_member_input_prototype_model2

        # Convert model instance back to dict and verify no loss of data
        stack_definition_member_input_prototype_model_json2 = stack_definition_member_input_prototype_model.to_dict()
        assert stack_definition_member_input_prototype_model_json2 == stack_definition_member_input_prototype_model_json


class TestModel_StackDefinitionMemberPrototype:
    """
    Test Class for StackDefinitionMemberPrototype
    """

    def test_stack_definition_member_prototype_serialization(self):
        """
        Test serialization/deserialization for StackDefinitionMemberPrototype
        """

        # Construct dict forms of any model objects needed in order to build this model.

        stack_definition_member_input_prototype_model = {}  # StackDefinitionMemberInputPrototype
        stack_definition_member_input_prototype_model['name'] = 'testString'

        # Construct a json representation of a StackDefinitionMemberPrototype model
        stack_definition_member_prototype_model_json = {}
        stack_definition_member_prototype_model_json['name'] = 'testString'
        stack_definition_member_prototype_model_json['inputs'] = [stack_definition_member_input_prototype_model]

        # Construct a model instance of StackDefinitionMemberPrototype by calling from_dict on the json representation
        stack_definition_member_prototype_model = StackDefinitionMemberPrototype.from_dict(
            stack_definition_member_prototype_model_json
        )
        assert stack_definition_member_prototype_model != False

        # Construct a model instance of StackDefinitionMemberPrototype by calling from_dict on the json representation
        stack_definition_member_prototype_model_dict = StackDefinitionMemberPrototype.from_dict(
            stack_definition_member_prototype_model_json
        ).__dict__
        stack_definition_member_prototype_model2 = StackDefinitionMemberPrototype(
            **stack_definition_member_prototype_model_dict
        )

        # Verify the model instances are equivalent
        assert stack_definition_member_prototype_model == stack_definition_member_prototype_model2

        # Convert model instance back to dict and verify no loss of data
        stack_definition_member_prototype_model_json2 = stack_definition_member_prototype_model.to_dict()
        assert stack_definition_member_prototype_model_json2 == stack_definition_member_prototype_model_json


class TestModel_StackDefinitionMetadataConfiguration:
    """
    Test Class for StackDefinitionMetadataConfiguration
    """

    def test_stack_definition_metadata_configuration_serialization(self):
        """
        Test serialization/deserialization for StackDefinitionMetadataConfiguration
        """

        # Construct dict forms of any model objects needed in order to build this model.

        config_definition_reference_model = {}  # ConfigDefinitionReference
        config_definition_reference_model['name'] = 'testString'

        # Construct a json representation of a StackDefinitionMetadataConfiguration model
        stack_definition_metadata_configuration_model_json = {}
        stack_definition_metadata_configuration_model_json['id'] = 'testString'
        stack_definition_metadata_configuration_model_json['href'] = 'testString'
        stack_definition_metadata_configuration_model_json['definition'] = config_definition_reference_model

        # Construct a model instance of StackDefinitionMetadataConfiguration by calling from_dict on the json representation
        stack_definition_metadata_configuration_model = StackDefinitionMetadataConfiguration.from_dict(
            stack_definition_metadata_configuration_model_json
        )
        assert stack_definition_metadata_configuration_model != False

        # Construct a model instance of StackDefinitionMetadataConfiguration by calling from_dict on the json representation
        stack_definition_metadata_configuration_model_dict = StackDefinitionMetadataConfiguration.from_dict(
            stack_definition_metadata_configuration_model_json
        ).__dict__
        stack_definition_metadata_configuration_model2 = StackDefinitionMetadataConfiguration(
            **stack_definition_metadata_configuration_model_dict
        )

        # Verify the model instances are equivalent
        assert stack_definition_metadata_configuration_model == stack_definition_metadata_configuration_model2

        # Convert model instance back to dict and verify no loss of data
        stack_definition_metadata_configuration_model_json2 = stack_definition_metadata_configuration_model.to_dict()
        assert stack_definition_metadata_configuration_model_json2 == stack_definition_metadata_configuration_model_json


class TestModel_StackDefinitionOutputVariable:
    """
    Test Class for StackDefinitionOutputVariable
    """

    def test_stack_definition_output_variable_serialization(self):
        """
        Test serialization/deserialization for StackDefinitionOutputVariable
        """

        # Construct a json representation of a StackDefinitionOutputVariable model
        stack_definition_output_variable_model_json = {}
        stack_definition_output_variable_model_json['name'] = 'testString'
        stack_definition_output_variable_model_json['value'] = 'testString'

        # Construct a model instance of StackDefinitionOutputVariable by calling from_dict on the json representation
        stack_definition_output_variable_model = StackDefinitionOutputVariable.from_dict(
            stack_definition_output_variable_model_json
        )
        assert stack_definition_output_variable_model != False

        # Construct a model instance of StackDefinitionOutputVariable by calling from_dict on the json representation
        stack_definition_output_variable_model_dict = StackDefinitionOutputVariable.from_dict(
            stack_definition_output_variable_model_json
        ).__dict__
        stack_definition_output_variable_model2 = StackDefinitionOutputVariable(
            **stack_definition_output_variable_model_dict
        )

        # Verify the model instances are equivalent
        assert stack_definition_output_variable_model == stack_definition_output_variable_model2

        # Convert model instance back to dict and verify no loss of data
        stack_definition_output_variable_model_json2 = stack_definition_output_variable_model.to_dict()
        assert stack_definition_output_variable_model_json2 == stack_definition_output_variable_model_json


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
        terraform_log_analyzer_error_message_model = TerraformLogAnalyzerErrorMessage.from_dict(
            terraform_log_analyzer_error_message_model_json
        )
        assert terraform_log_analyzer_error_message_model != False

        # Construct a model instance of TerraformLogAnalyzerErrorMessage by calling from_dict on the json representation
        terraform_log_analyzer_error_message_model_dict = TerraformLogAnalyzerErrorMessage.from_dict(
            terraform_log_analyzer_error_message_model_json
        ).__dict__
        terraform_log_analyzer_error_message_model2 = TerraformLogAnalyzerErrorMessage(
            **terraform_log_analyzer_error_message_model_dict
        )

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
        terraform_log_analyzer_success_message_model = TerraformLogAnalyzerSuccessMessage.from_dict(
            terraform_log_analyzer_success_message_model_json
        )
        assert terraform_log_analyzer_success_message_model != False

        # Construct a model instance of TerraformLogAnalyzerSuccessMessage by calling from_dict on the json representation
        terraform_log_analyzer_success_message_model_dict = TerraformLogAnalyzerSuccessMessage.from_dict(
            terraform_log_analyzer_success_message_model_json
        ).__dict__
        terraform_log_analyzer_success_message_model2 = TerraformLogAnalyzerSuccessMessage(
            **terraform_log_analyzer_success_message_model_dict
        )

        # Verify the model instances are equivalent
        assert terraform_log_analyzer_success_message_model == terraform_log_analyzer_success_message_model2

        # Convert model instance back to dict and verify no loss of data
        terraform_log_analyzer_success_message_model_json2 = terraform_log_analyzer_success_message_model.to_dict()
        assert terraform_log_analyzer_success_message_model_json2 == terraform_log_analyzer_success_message_model_json


class TestModel_ProjectConfigDefinitionPatchDAConfigDefinitionPropertiesPatch:
    """
    Test Class for ProjectConfigDefinitionPatchDAConfigDefinitionPropertiesPatch
    """

    def test_project_config_definition_patch_da_config_definition_properties_patch_serialization(self):
        """
        Test serialization/deserialization for ProjectConfigDefinitionPatchDAConfigDefinitionPropertiesPatch
        """

        # Construct dict forms of any model objects needed in order to build this model.

        project_compliance_profile_model = {}  # ProjectComplianceProfile
        project_compliance_profile_model['id'] = 'testString'
        project_compliance_profile_model['instance_id'] = 'testString'
        project_compliance_profile_model['instance_location'] = 'testString'
        project_compliance_profile_model['attachment_id'] = 'testString'
        project_compliance_profile_model['profile_name'] = 'testString'

        project_config_auth_model = {}  # ProjectConfigAuth
        project_config_auth_model['trusted_profile_id'] = 'testString'
        project_config_auth_model['method'] = 'api_key'
        project_config_auth_model['api_key'] = 'testString'

        # Construct a json representation of a ProjectConfigDefinitionPatchDAConfigDefinitionPropertiesPatch model
        project_config_definition_patch_da_config_definition_properties_patch_model_json = {}
        project_config_definition_patch_da_config_definition_properties_patch_model_json['compliance_profile'] = (
            project_compliance_profile_model
        )
        project_config_definition_patch_da_config_definition_properties_patch_model_json['locator_id'] = 'testString'
        project_config_definition_patch_da_config_definition_properties_patch_model_json['description'] = 'testString'
        project_config_definition_patch_da_config_definition_properties_patch_model_json['name'] = 'testString'
        project_config_definition_patch_da_config_definition_properties_patch_model_json['environment_id'] = (
            'testString'
        )
        project_config_definition_patch_da_config_definition_properties_patch_model_json['authorizations'] = (
            project_config_auth_model
        )
        project_config_definition_patch_da_config_definition_properties_patch_model_json['inputs'] = {
            'anyKey': 'anyValue'
        }
        project_config_definition_patch_da_config_definition_properties_patch_model_json['settings'] = {
            'anyKey': 'anyValue'
        }

        # Construct a model instance of ProjectConfigDefinitionPatchDAConfigDefinitionPropertiesPatch by calling from_dict on the json representation
        project_config_definition_patch_da_config_definition_properties_patch_model = (
            ProjectConfigDefinitionPatchDAConfigDefinitionPropertiesPatch.from_dict(
                project_config_definition_patch_da_config_definition_properties_patch_model_json
            )
        )
        assert project_config_definition_patch_da_config_definition_properties_patch_model != False

        # Construct a model instance of ProjectConfigDefinitionPatchDAConfigDefinitionPropertiesPatch by calling from_dict on the json representation
        project_config_definition_patch_da_config_definition_properties_patch_model_dict = (
            ProjectConfigDefinitionPatchDAConfigDefinitionPropertiesPatch.from_dict(
                project_config_definition_patch_da_config_definition_properties_patch_model_json
            ).__dict__
        )
        project_config_definition_patch_da_config_definition_properties_patch_model2 = (
            ProjectConfigDefinitionPatchDAConfigDefinitionPropertiesPatch(
                **project_config_definition_patch_da_config_definition_properties_patch_model_dict
            )
        )

        # Verify the model instances are equivalent
        assert (
            project_config_definition_patch_da_config_definition_properties_patch_model
            == project_config_definition_patch_da_config_definition_properties_patch_model2
        )

        # Convert model instance back to dict and verify no loss of data
        project_config_definition_patch_da_config_definition_properties_patch_model_json2 = (
            project_config_definition_patch_da_config_definition_properties_patch_model.to_dict()
        )
        assert (
            project_config_definition_patch_da_config_definition_properties_patch_model_json2
            == project_config_definition_patch_da_config_definition_properties_patch_model_json
        )


class TestModel_ProjectConfigDefinitionPatchResourceConfigDefinitionPropertiesPatch:
    """
    Test Class for ProjectConfigDefinitionPatchResourceConfigDefinitionPropertiesPatch
    """

    def test_project_config_definition_patch_resource_config_definition_properties_patch_serialization(self):
        """
        Test serialization/deserialization for ProjectConfigDefinitionPatchResourceConfigDefinitionPropertiesPatch
        """

        # Construct dict forms of any model objects needed in order to build this model.

        project_config_auth_model = {}  # ProjectConfigAuth
        project_config_auth_model['trusted_profile_id'] = 'testString'
        project_config_auth_model['method'] = 'api_key'
        project_config_auth_model['api_key'] = 'testString'

        # Construct a json representation of a ProjectConfigDefinitionPatchResourceConfigDefinitionPropertiesPatch model
        project_config_definition_patch_resource_config_definition_properties_patch_model_json = {}
        project_config_definition_patch_resource_config_definition_properties_patch_model_json['resource_crns'] = [
            'crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::'
        ]
        project_config_definition_patch_resource_config_definition_properties_patch_model_json['description'] = (
            'testString'
        )
        project_config_definition_patch_resource_config_definition_properties_patch_model_json['name'] = 'testString'
        project_config_definition_patch_resource_config_definition_properties_patch_model_json['environment_id'] = (
            'testString'
        )
        project_config_definition_patch_resource_config_definition_properties_patch_model_json['authorizations'] = (
            project_config_auth_model
        )
        project_config_definition_patch_resource_config_definition_properties_patch_model_json['inputs'] = {
            'anyKey': 'anyValue'
        }
        project_config_definition_patch_resource_config_definition_properties_patch_model_json['settings'] = {
            'anyKey': 'anyValue'
        }

        # Construct a model instance of ProjectConfigDefinitionPatchResourceConfigDefinitionPropertiesPatch by calling from_dict on the json representation
        project_config_definition_patch_resource_config_definition_properties_patch_model = (
            ProjectConfigDefinitionPatchResourceConfigDefinitionPropertiesPatch.from_dict(
                project_config_definition_patch_resource_config_definition_properties_patch_model_json
            )
        )
        assert project_config_definition_patch_resource_config_definition_properties_patch_model != False

        # Construct a model instance of ProjectConfigDefinitionPatchResourceConfigDefinitionPropertiesPatch by calling from_dict on the json representation
        project_config_definition_patch_resource_config_definition_properties_patch_model_dict = (
            ProjectConfigDefinitionPatchResourceConfigDefinitionPropertiesPatch.from_dict(
                project_config_definition_patch_resource_config_definition_properties_patch_model_json
            ).__dict__
        )
        project_config_definition_patch_resource_config_definition_properties_patch_model2 = (
            ProjectConfigDefinitionPatchResourceConfigDefinitionPropertiesPatch(
                **project_config_definition_patch_resource_config_definition_properties_patch_model_dict
            )
        )

        # Verify the model instances are equivalent
        assert (
            project_config_definition_patch_resource_config_definition_properties_patch_model
            == project_config_definition_patch_resource_config_definition_properties_patch_model2
        )

        # Convert model instance back to dict and verify no loss of data
        project_config_definition_patch_resource_config_definition_properties_patch_model_json2 = (
            project_config_definition_patch_resource_config_definition_properties_patch_model.to_dict()
        )
        assert (
            project_config_definition_patch_resource_config_definition_properties_patch_model_json2
            == project_config_definition_patch_resource_config_definition_properties_patch_model_json
        )


class TestModel_ProjectConfigDefinitionPrototypeDAConfigDefinitionPropertiesPrototype:
    """
    Test Class for ProjectConfigDefinitionPrototypeDAConfigDefinitionPropertiesPrototype
    """

    def test_project_config_definition_prototype_da_config_definition_properties_prototype_serialization(self):
        """
        Test serialization/deserialization for ProjectConfigDefinitionPrototypeDAConfigDefinitionPropertiesPrototype
        """

        # Construct dict forms of any model objects needed in order to build this model.

        project_compliance_profile_model = {}  # ProjectComplianceProfile
        project_compliance_profile_model['id'] = 'testString'
        project_compliance_profile_model['instance_id'] = 'testString'
        project_compliance_profile_model['instance_location'] = 'testString'
        project_compliance_profile_model['attachment_id'] = 'testString'
        project_compliance_profile_model['profile_name'] = 'testString'

        project_config_auth_model = {}  # ProjectConfigAuth
        project_config_auth_model['trusted_profile_id'] = 'testString'
        project_config_auth_model['method'] = 'api_key'
        project_config_auth_model['api_key'] = 'testString'

        # Construct a json representation of a ProjectConfigDefinitionPrototypeDAConfigDefinitionPropertiesPrototype model
        project_config_definition_prototype_da_config_definition_properties_prototype_model_json = {}
        project_config_definition_prototype_da_config_definition_properties_prototype_model_json[
            'compliance_profile'
        ] = project_compliance_profile_model
        project_config_definition_prototype_da_config_definition_properties_prototype_model_json['locator_id'] = (
            'testString'
        )
        project_config_definition_prototype_da_config_definition_properties_prototype_model_json['description'] = (
            'testString'
        )
        project_config_definition_prototype_da_config_definition_properties_prototype_model_json['name'] = 'testString'
        project_config_definition_prototype_da_config_definition_properties_prototype_model_json['environment_id'] = (
            'testString'
        )
        project_config_definition_prototype_da_config_definition_properties_prototype_model_json['authorizations'] = (
            project_config_auth_model
        )
        project_config_definition_prototype_da_config_definition_properties_prototype_model_json['inputs'] = {
            'anyKey': 'anyValue'
        }
        project_config_definition_prototype_da_config_definition_properties_prototype_model_json['settings'] = {
            'anyKey': 'anyValue'
        }

        # Construct a model instance of ProjectConfigDefinitionPrototypeDAConfigDefinitionPropertiesPrototype by calling from_dict on the json representation
        project_config_definition_prototype_da_config_definition_properties_prototype_model = (
            ProjectConfigDefinitionPrototypeDAConfigDefinitionPropertiesPrototype.from_dict(
                project_config_definition_prototype_da_config_definition_properties_prototype_model_json
            )
        )
        assert project_config_definition_prototype_da_config_definition_properties_prototype_model != False

        # Construct a model instance of ProjectConfigDefinitionPrototypeDAConfigDefinitionPropertiesPrototype by calling from_dict on the json representation
        project_config_definition_prototype_da_config_definition_properties_prototype_model_dict = (
            ProjectConfigDefinitionPrototypeDAConfigDefinitionPropertiesPrototype.from_dict(
                project_config_definition_prototype_da_config_definition_properties_prototype_model_json
            ).__dict__
        )
        project_config_definition_prototype_da_config_definition_properties_prototype_model2 = (
            ProjectConfigDefinitionPrototypeDAConfigDefinitionPropertiesPrototype(
                **project_config_definition_prototype_da_config_definition_properties_prototype_model_dict
            )
        )

        # Verify the model instances are equivalent
        assert (
            project_config_definition_prototype_da_config_definition_properties_prototype_model
            == project_config_definition_prototype_da_config_definition_properties_prototype_model2
        )

        # Convert model instance back to dict and verify no loss of data
        project_config_definition_prototype_da_config_definition_properties_prototype_model_json2 = (
            project_config_definition_prototype_da_config_definition_properties_prototype_model.to_dict()
        )
        assert (
            project_config_definition_prototype_da_config_definition_properties_prototype_model_json2
            == project_config_definition_prototype_da_config_definition_properties_prototype_model_json
        )


class TestModel_ProjectConfigDefinitionPrototypeResourceConfigDefinitionPropertiesPrototype:
    """
    Test Class for ProjectConfigDefinitionPrototypeResourceConfigDefinitionPropertiesPrototype
    """

    def test_project_config_definition_prototype_resource_config_definition_properties_prototype_serialization(self):
        """
        Test serialization/deserialization for ProjectConfigDefinitionPrototypeResourceConfigDefinitionPropertiesPrototype
        """

        # Construct dict forms of any model objects needed in order to build this model.

        project_config_auth_model = {}  # ProjectConfigAuth
        project_config_auth_model['trusted_profile_id'] = 'testString'
        project_config_auth_model['method'] = 'api_key'
        project_config_auth_model['api_key'] = 'testString'

        # Construct a json representation of a ProjectConfigDefinitionPrototypeResourceConfigDefinitionPropertiesPrototype model
        project_config_definition_prototype_resource_config_definition_properties_prototype_model_json = {}
        project_config_definition_prototype_resource_config_definition_properties_prototype_model_json[
            'resource_crns'
        ] = [
            'crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::'
        ]
        project_config_definition_prototype_resource_config_definition_properties_prototype_model_json[
            'description'
        ] = 'testString'
        project_config_definition_prototype_resource_config_definition_properties_prototype_model_json['name'] = (
            'testString'
        )
        project_config_definition_prototype_resource_config_definition_properties_prototype_model_json[
            'environment_id'
        ] = 'testString'
        project_config_definition_prototype_resource_config_definition_properties_prototype_model_json[
            'authorizations'
        ] = project_config_auth_model
        project_config_definition_prototype_resource_config_definition_properties_prototype_model_json['inputs'] = {
            'anyKey': 'anyValue'
        }
        project_config_definition_prototype_resource_config_definition_properties_prototype_model_json['settings'] = {
            'anyKey': 'anyValue'
        }

        # Construct a model instance of ProjectConfigDefinitionPrototypeResourceConfigDefinitionPropertiesPrototype by calling from_dict on the json representation
        project_config_definition_prototype_resource_config_definition_properties_prototype_model = (
            ProjectConfigDefinitionPrototypeResourceConfigDefinitionPropertiesPrototype.from_dict(
                project_config_definition_prototype_resource_config_definition_properties_prototype_model_json
            )
        )
        assert project_config_definition_prototype_resource_config_definition_properties_prototype_model != False

        # Construct a model instance of ProjectConfigDefinitionPrototypeResourceConfigDefinitionPropertiesPrototype by calling from_dict on the json representation
        project_config_definition_prototype_resource_config_definition_properties_prototype_model_dict = (
            ProjectConfigDefinitionPrototypeResourceConfigDefinitionPropertiesPrototype.from_dict(
                project_config_definition_prototype_resource_config_definition_properties_prototype_model_json
            ).__dict__
        )
        project_config_definition_prototype_resource_config_definition_properties_prototype_model2 = (
            ProjectConfigDefinitionPrototypeResourceConfigDefinitionPropertiesPrototype(
                **project_config_definition_prototype_resource_config_definition_properties_prototype_model_dict
            )
        )

        # Verify the model instances are equivalent
        assert (
            project_config_definition_prototype_resource_config_definition_properties_prototype_model
            == project_config_definition_prototype_resource_config_definition_properties_prototype_model2
        )

        # Convert model instance back to dict and verify no loss of data
        project_config_definition_prototype_resource_config_definition_properties_prototype_model_json2 = (
            project_config_definition_prototype_resource_config_definition_properties_prototype_model.to_dict()
        )
        assert (
            project_config_definition_prototype_resource_config_definition_properties_prototype_model_json2
            == project_config_definition_prototype_resource_config_definition_properties_prototype_model_json
        )


class TestModel_ProjectConfigDefinitionPrototypeStackConfigDefinitionProperties:
    """
    Test Class for ProjectConfigDefinitionPrototypeStackConfigDefinitionProperties
    """

    def test_project_config_definition_prototype_stack_config_definition_properties_serialization(self):
        """
        Test serialization/deserialization for ProjectConfigDefinitionPrototypeStackConfigDefinitionProperties
        """

        # Construct dict forms of any model objects needed in order to build this model.

        stack_config_member_model = {}  # StackConfigMember
        stack_config_member_model['name'] = 'testString'
        stack_config_member_model['config_id'] = 'testString'

        # Construct a json representation of a ProjectConfigDefinitionPrototypeStackConfigDefinitionProperties model
        project_config_definition_prototype_stack_config_definition_properties_model_json = {}
        project_config_definition_prototype_stack_config_definition_properties_model_json['description'] = 'testString'
        project_config_definition_prototype_stack_config_definition_properties_model_json['name'] = 'testString'
        project_config_definition_prototype_stack_config_definition_properties_model_json['locator_id'] = 'testString'
        project_config_definition_prototype_stack_config_definition_properties_model_json['environment_id'] = (
            'testString'
        )
        project_config_definition_prototype_stack_config_definition_properties_model_json['inputs'] = {
            'anyKey': 'anyValue'
        }
        project_config_definition_prototype_stack_config_definition_properties_model_json['members'] = [
            stack_config_member_model
        ]

        # Construct a model instance of ProjectConfigDefinitionPrototypeStackConfigDefinitionProperties by calling from_dict on the json representation
        project_config_definition_prototype_stack_config_definition_properties_model = (
            ProjectConfigDefinitionPrototypeStackConfigDefinitionProperties.from_dict(
                project_config_definition_prototype_stack_config_definition_properties_model_json
            )
        )
        assert project_config_definition_prototype_stack_config_definition_properties_model != False

        # Construct a model instance of ProjectConfigDefinitionPrototypeStackConfigDefinitionProperties by calling from_dict on the json representation
        project_config_definition_prototype_stack_config_definition_properties_model_dict = (
            ProjectConfigDefinitionPrototypeStackConfigDefinitionProperties.from_dict(
                project_config_definition_prototype_stack_config_definition_properties_model_json
            ).__dict__
        )
        project_config_definition_prototype_stack_config_definition_properties_model2 = (
            ProjectConfigDefinitionPrototypeStackConfigDefinitionProperties(
                **project_config_definition_prototype_stack_config_definition_properties_model_dict
            )
        )

        # Verify the model instances are equivalent
        assert (
            project_config_definition_prototype_stack_config_definition_properties_model
            == project_config_definition_prototype_stack_config_definition_properties_model2
        )

        # Convert model instance back to dict and verify no loss of data
        project_config_definition_prototype_stack_config_definition_properties_model_json2 = (
            project_config_definition_prototype_stack_config_definition_properties_model.to_dict()
        )
        assert (
            project_config_definition_prototype_stack_config_definition_properties_model_json2
            == project_config_definition_prototype_stack_config_definition_properties_model_json
        )


class TestModel_ProjectConfigDefinitionResponseDAConfigDefinitionPropertiesResponse:
    """
    Test Class for ProjectConfigDefinitionResponseDAConfigDefinitionPropertiesResponse
    """

    def test_project_config_definition_response_da_config_definition_properties_response_serialization(self):
        """
        Test serialization/deserialization for ProjectConfigDefinitionResponseDAConfigDefinitionPropertiesResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        project_compliance_profile_model = {}  # ProjectComplianceProfile
        project_compliance_profile_model['id'] = 'testString'
        project_compliance_profile_model['instance_id'] = 'testString'
        project_compliance_profile_model['instance_location'] = 'testString'
        project_compliance_profile_model['attachment_id'] = 'testString'
        project_compliance_profile_model['profile_name'] = 'testString'

        project_config_auth_model = {}  # ProjectConfigAuth
        project_config_auth_model['trusted_profile_id'] = 'testString'
        project_config_auth_model['method'] = 'api_key'
        project_config_auth_model['api_key'] = 'testString'

        # Construct a json representation of a ProjectConfigDefinitionResponseDAConfigDefinitionPropertiesResponse model
        project_config_definition_response_da_config_definition_properties_response_model_json = {}
        project_config_definition_response_da_config_definition_properties_response_model_json['compliance_profile'] = (
            project_compliance_profile_model
        )
        project_config_definition_response_da_config_definition_properties_response_model_json['locator_id'] = (
            'testString'
        )
        project_config_definition_response_da_config_definition_properties_response_model_json['description'] = (
            'testString'
        )
        project_config_definition_response_da_config_definition_properties_response_model_json['name'] = 'testString'
        project_config_definition_response_da_config_definition_properties_response_model_json['environment_id'] = (
            'testString'
        )
        project_config_definition_response_da_config_definition_properties_response_model_json['authorizations'] = (
            project_config_auth_model
        )
        project_config_definition_response_da_config_definition_properties_response_model_json['inputs'] = {
            'anyKey': 'anyValue'
        }
        project_config_definition_response_da_config_definition_properties_response_model_json['settings'] = {
            'anyKey': 'anyValue'
        }

        # Construct a model instance of ProjectConfigDefinitionResponseDAConfigDefinitionPropertiesResponse by calling from_dict on the json representation
        project_config_definition_response_da_config_definition_properties_response_model = (
            ProjectConfigDefinitionResponseDAConfigDefinitionPropertiesResponse.from_dict(
                project_config_definition_response_da_config_definition_properties_response_model_json
            )
        )
        assert project_config_definition_response_da_config_definition_properties_response_model != False

        # Construct a model instance of ProjectConfigDefinitionResponseDAConfigDefinitionPropertiesResponse by calling from_dict on the json representation
        project_config_definition_response_da_config_definition_properties_response_model_dict = (
            ProjectConfigDefinitionResponseDAConfigDefinitionPropertiesResponse.from_dict(
                project_config_definition_response_da_config_definition_properties_response_model_json
            ).__dict__
        )
        project_config_definition_response_da_config_definition_properties_response_model2 = (
            ProjectConfigDefinitionResponseDAConfigDefinitionPropertiesResponse(
                **project_config_definition_response_da_config_definition_properties_response_model_dict
            )
        )

        # Verify the model instances are equivalent
        assert (
            project_config_definition_response_da_config_definition_properties_response_model
            == project_config_definition_response_da_config_definition_properties_response_model2
        )

        # Convert model instance back to dict and verify no loss of data
        project_config_definition_response_da_config_definition_properties_response_model_json2 = (
            project_config_definition_response_da_config_definition_properties_response_model.to_dict()
        )
        assert (
            project_config_definition_response_da_config_definition_properties_response_model_json2
            == project_config_definition_response_da_config_definition_properties_response_model_json
        )


class TestModel_ProjectConfigDefinitionResponseResourceConfigDefinitionPropertiesResponse:
    """
    Test Class for ProjectConfigDefinitionResponseResourceConfigDefinitionPropertiesResponse
    """

    def test_project_config_definition_response_resource_config_definition_properties_response_serialization(self):
        """
        Test serialization/deserialization for ProjectConfigDefinitionResponseResourceConfigDefinitionPropertiesResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        project_config_auth_model = {}  # ProjectConfigAuth
        project_config_auth_model['trusted_profile_id'] = 'testString'
        project_config_auth_model['method'] = 'api_key'
        project_config_auth_model['api_key'] = 'testString'

        # Construct a json representation of a ProjectConfigDefinitionResponseResourceConfigDefinitionPropertiesResponse model
        project_config_definition_response_resource_config_definition_properties_response_model_json = {}
        project_config_definition_response_resource_config_definition_properties_response_model_json[
            'resource_crns'
        ] = [
            'crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::'
        ]
        project_config_definition_response_resource_config_definition_properties_response_model_json['description'] = (
            'testString'
        )
        project_config_definition_response_resource_config_definition_properties_response_model_json['name'] = (
            'testString'
        )
        project_config_definition_response_resource_config_definition_properties_response_model_json[
            'environment_id'
        ] = 'testString'
        project_config_definition_response_resource_config_definition_properties_response_model_json[
            'authorizations'
        ] = project_config_auth_model
        project_config_definition_response_resource_config_definition_properties_response_model_json['inputs'] = {
            'anyKey': 'anyValue'
        }
        project_config_definition_response_resource_config_definition_properties_response_model_json['settings'] = {
            'anyKey': 'anyValue'
        }

        # Construct a model instance of ProjectConfigDefinitionResponseResourceConfigDefinitionPropertiesResponse by calling from_dict on the json representation
        project_config_definition_response_resource_config_definition_properties_response_model = (
            ProjectConfigDefinitionResponseResourceConfigDefinitionPropertiesResponse.from_dict(
                project_config_definition_response_resource_config_definition_properties_response_model_json
            )
        )
        assert project_config_definition_response_resource_config_definition_properties_response_model != False

        # Construct a model instance of ProjectConfigDefinitionResponseResourceConfigDefinitionPropertiesResponse by calling from_dict on the json representation
        project_config_definition_response_resource_config_definition_properties_response_model_dict = (
            ProjectConfigDefinitionResponseResourceConfigDefinitionPropertiesResponse.from_dict(
                project_config_definition_response_resource_config_definition_properties_response_model_json
            ).__dict__
        )
        project_config_definition_response_resource_config_definition_properties_response_model2 = (
            ProjectConfigDefinitionResponseResourceConfigDefinitionPropertiesResponse(
                **project_config_definition_response_resource_config_definition_properties_response_model_dict
            )
        )

        # Verify the model instances are equivalent
        assert (
            project_config_definition_response_resource_config_definition_properties_response_model
            == project_config_definition_response_resource_config_definition_properties_response_model2
        )

        # Convert model instance back to dict and verify no loss of data
        project_config_definition_response_resource_config_definition_properties_response_model_json2 = (
            project_config_definition_response_resource_config_definition_properties_response_model.to_dict()
        )
        assert (
            project_config_definition_response_resource_config_definition_properties_response_model_json2
            == project_config_definition_response_resource_config_definition_properties_response_model_json
        )


class TestModel_ProjectConfigDefinitionResponseStackConfigDefinitionProperties:
    """
    Test Class for ProjectConfigDefinitionResponseStackConfigDefinitionProperties
    """

    def test_project_config_definition_response_stack_config_definition_properties_serialization(self):
        """
        Test serialization/deserialization for ProjectConfigDefinitionResponseStackConfigDefinitionProperties
        """

        # Construct dict forms of any model objects needed in order to build this model.

        stack_config_member_model = {}  # StackConfigMember
        stack_config_member_model['name'] = 'testString'
        stack_config_member_model['config_id'] = 'testString'

        # Construct a json representation of a ProjectConfigDefinitionResponseStackConfigDefinitionProperties model
        project_config_definition_response_stack_config_definition_properties_model_json = {}
        project_config_definition_response_stack_config_definition_properties_model_json['description'] = 'testString'
        project_config_definition_response_stack_config_definition_properties_model_json['name'] = 'testString'
        project_config_definition_response_stack_config_definition_properties_model_json['locator_id'] = 'testString'
        project_config_definition_response_stack_config_definition_properties_model_json['environment_id'] = (
            'testString'
        )
        project_config_definition_response_stack_config_definition_properties_model_json['inputs'] = {
            'anyKey': 'anyValue'
        }
        project_config_definition_response_stack_config_definition_properties_model_json['members'] = [
            stack_config_member_model
        ]

        # Construct a model instance of ProjectConfigDefinitionResponseStackConfigDefinitionProperties by calling from_dict on the json representation
        project_config_definition_response_stack_config_definition_properties_model = (
            ProjectConfigDefinitionResponseStackConfigDefinitionProperties.from_dict(
                project_config_definition_response_stack_config_definition_properties_model_json
            )
        )
        assert project_config_definition_response_stack_config_definition_properties_model != False

        # Construct a model instance of ProjectConfigDefinitionResponseStackConfigDefinitionProperties by calling from_dict on the json representation
        project_config_definition_response_stack_config_definition_properties_model_dict = (
            ProjectConfigDefinitionResponseStackConfigDefinitionProperties.from_dict(
                project_config_definition_response_stack_config_definition_properties_model_json
            ).__dict__
        )
        project_config_definition_response_stack_config_definition_properties_model2 = (
            ProjectConfigDefinitionResponseStackConfigDefinitionProperties(
                **project_config_definition_response_stack_config_definition_properties_model_dict
            )
        )

        # Verify the model instances are equivalent
        assert (
            project_config_definition_response_stack_config_definition_properties_model
            == project_config_definition_response_stack_config_definition_properties_model2
        )

        # Convert model instance back to dict and verify no loss of data
        project_config_definition_response_stack_config_definition_properties_model_json2 = (
            project_config_definition_response_stack_config_definition_properties_model.to_dict()
        )
        assert (
            project_config_definition_response_stack_config_definition_properties_model_json2
            == project_config_definition_response_stack_config_definition_properties_model_json
        )


class TestModel_ProjectConfigMetadataCodeRiskAnalyzerLogsVersion204:
    """
    Test Class for ProjectConfigMetadataCodeRiskAnalyzerLogsVersion204
    """

    def test_project_config_metadata_code_risk_analyzer_logs_version204_serialization(self):
        """
        Test serialization/deserialization for ProjectConfigMetadataCodeRiskAnalyzerLogsVersion204
        """

        # Construct dict forms of any model objects needed in order to build this model.

        code_risk_analyzer_logs_summary_model = {}  # CodeRiskAnalyzerLogsSummary
        code_risk_analyzer_logs_summary_model['total'] = 'testString'
        code_risk_analyzer_logs_summary_model['passed'] = 'testString'
        code_risk_analyzer_logs_summary_model['failed'] = 'testString'
        code_risk_analyzer_logs_summary_model['skipped'] = 'testString'

        # Construct a json representation of a ProjectConfigMetadataCodeRiskAnalyzerLogsVersion204 model
        project_config_metadata_code_risk_analyzer_logs_version2_0_4_model_json = {}
        project_config_metadata_code_risk_analyzer_logs_version2_0_4_model_json['cra_version'] = '2.0.4'
        project_config_metadata_code_risk_analyzer_logs_version2_0_4_model_json['schema_version'] = 'testString'
        project_config_metadata_code_risk_analyzer_logs_version2_0_4_model_json['status'] = 'passed'
        project_config_metadata_code_risk_analyzer_logs_version2_0_4_model_json['summary'] = (
            code_risk_analyzer_logs_summary_model
        )
        project_config_metadata_code_risk_analyzer_logs_version2_0_4_model_json['timestamp'] = '2019-01-01T12:00:00Z'

        # Construct a model instance of ProjectConfigMetadataCodeRiskAnalyzerLogsVersion204 by calling from_dict on the json representation
        project_config_metadata_code_risk_analyzer_logs_version2_0_4_model = (
            ProjectConfigMetadataCodeRiskAnalyzerLogsVersion204.from_dict(
                project_config_metadata_code_risk_analyzer_logs_version2_0_4_model_json
            )
        )
        assert project_config_metadata_code_risk_analyzer_logs_version2_0_4_model != False

        # Construct a model instance of ProjectConfigMetadataCodeRiskAnalyzerLogsVersion204 by calling from_dict on the json representation
        project_config_metadata_code_risk_analyzer_logs_version2_0_4_model_dict = (
            ProjectConfigMetadataCodeRiskAnalyzerLogsVersion204.from_dict(
                project_config_metadata_code_risk_analyzer_logs_version2_0_4_model_json
            ).__dict__
        )
        project_config_metadata_code_risk_analyzer_logs_version2_0_4_model2 = (
            ProjectConfigMetadataCodeRiskAnalyzerLogsVersion204(
                **project_config_metadata_code_risk_analyzer_logs_version2_0_4_model_dict
            )
        )

        # Verify the model instances are equivalent
        assert (
            project_config_metadata_code_risk_analyzer_logs_version2_0_4_model
            == project_config_metadata_code_risk_analyzer_logs_version2_0_4_model2
        )

        # Convert model instance back to dict and verify no loss of data
        project_config_metadata_code_risk_analyzer_logs_version2_0_4_model_json2 = (
            project_config_metadata_code_risk_analyzer_logs_version2_0_4_model.to_dict()
        )
        assert (
            project_config_metadata_code_risk_analyzer_logs_version2_0_4_model_json2
            == project_config_metadata_code_risk_analyzer_logs_version2_0_4_model_json
        )


class TestModel_StackDefinitionExportRequestStackDefinitionExportCatalogRequest:
    """
    Test Class for StackDefinitionExportRequestStackDefinitionExportCatalogRequest
    """

    def test_stack_definition_export_request_stack_definition_export_catalog_request_serialization(self):
        """
        Test serialization/deserialization for StackDefinitionExportRequestStackDefinitionExportCatalogRequest
        """

        # Construct a json representation of a StackDefinitionExportRequestStackDefinitionExportCatalogRequest model
        stack_definition_export_request_stack_definition_export_catalog_request_model_json = {}
        stack_definition_export_request_stack_definition_export_catalog_request_model_json['catalog_id'] = 'testString'
        stack_definition_export_request_stack_definition_export_catalog_request_model_json['target_version'] = (
            'testString'
        )
        stack_definition_export_request_stack_definition_export_catalog_request_model_json['variation'] = 'testString'
        stack_definition_export_request_stack_definition_export_catalog_request_model_json['label'] = 'testString'
        stack_definition_export_request_stack_definition_export_catalog_request_model_json['tags'] = ['testString']

        # Construct a model instance of StackDefinitionExportRequestStackDefinitionExportCatalogRequest by calling from_dict on the json representation
        stack_definition_export_request_stack_definition_export_catalog_request_model = (
            StackDefinitionExportRequestStackDefinitionExportCatalogRequest.from_dict(
                stack_definition_export_request_stack_definition_export_catalog_request_model_json
            )
        )
        assert stack_definition_export_request_stack_definition_export_catalog_request_model != False

        # Construct a model instance of StackDefinitionExportRequestStackDefinitionExportCatalogRequest by calling from_dict on the json representation
        stack_definition_export_request_stack_definition_export_catalog_request_model_dict = (
            StackDefinitionExportRequestStackDefinitionExportCatalogRequest.from_dict(
                stack_definition_export_request_stack_definition_export_catalog_request_model_json
            ).__dict__
        )
        stack_definition_export_request_stack_definition_export_catalog_request_model2 = (
            StackDefinitionExportRequestStackDefinitionExportCatalogRequest(
                **stack_definition_export_request_stack_definition_export_catalog_request_model_dict
            )
        )

        # Verify the model instances are equivalent
        assert (
            stack_definition_export_request_stack_definition_export_catalog_request_model
            == stack_definition_export_request_stack_definition_export_catalog_request_model2
        )

        # Convert model instance back to dict and verify no loss of data
        stack_definition_export_request_stack_definition_export_catalog_request_model_json2 = (
            stack_definition_export_request_stack_definition_export_catalog_request_model.to_dict()
        )
        assert (
            stack_definition_export_request_stack_definition_export_catalog_request_model_json2
            == stack_definition_export_request_stack_definition_export_catalog_request_model_json
        )


class TestModel_StackDefinitionExportRequestStackDefinitionExportProductRequest:
    """
    Test Class for StackDefinitionExportRequestStackDefinitionExportProductRequest
    """

    def test_stack_definition_export_request_stack_definition_export_product_request_serialization(self):
        """
        Test serialization/deserialization for StackDefinitionExportRequestStackDefinitionExportProductRequest
        """

        # Construct a json representation of a StackDefinitionExportRequestStackDefinitionExportProductRequest model
        stack_definition_export_request_stack_definition_export_product_request_model_json = {}
        stack_definition_export_request_stack_definition_export_product_request_model_json['catalog_id'] = 'testString'
        stack_definition_export_request_stack_definition_export_product_request_model_json['target_version'] = (
            'testString'
        )
        stack_definition_export_request_stack_definition_export_product_request_model_json['variation'] = 'testString'
        stack_definition_export_request_stack_definition_export_product_request_model_json['product_id'] = 'testString'

        # Construct a model instance of StackDefinitionExportRequestStackDefinitionExportProductRequest by calling from_dict on the json representation
        stack_definition_export_request_stack_definition_export_product_request_model = (
            StackDefinitionExportRequestStackDefinitionExportProductRequest.from_dict(
                stack_definition_export_request_stack_definition_export_product_request_model_json
            )
        )
        assert stack_definition_export_request_stack_definition_export_product_request_model != False

        # Construct a model instance of StackDefinitionExportRequestStackDefinitionExportProductRequest by calling from_dict on the json representation
        stack_definition_export_request_stack_definition_export_product_request_model_dict = (
            StackDefinitionExportRequestStackDefinitionExportProductRequest.from_dict(
                stack_definition_export_request_stack_definition_export_product_request_model_json
            ).__dict__
        )
        stack_definition_export_request_stack_definition_export_product_request_model2 = (
            StackDefinitionExportRequestStackDefinitionExportProductRequest(
                **stack_definition_export_request_stack_definition_export_product_request_model_dict
            )
        )

        # Verify the model instances are equivalent
        assert (
            stack_definition_export_request_stack_definition_export_product_request_model
            == stack_definition_export_request_stack_definition_export_product_request_model2
        )

        # Convert model instance back to dict and verify no loss of data
        stack_definition_export_request_stack_definition_export_product_request_model_json2 = (
            stack_definition_export_request_stack_definition_export_product_request_model.to_dict()
        )
        assert (
            stack_definition_export_request_stack_definition_export_product_request_model_json2
            == stack_definition_export_request_stack_definition_export_product_request_model_json
        )


# endregion
##############################################################################
# End of Model Tests
##############################################################################
