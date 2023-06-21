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
from project.project_v1 import *


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
        mock_response = '{"crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::", "created_at": "2019-01-01T12:00:00.000Z", "cumulative_needs_attention_view": [{"event": "event", "event_id": "event_id", "config_id": "config_id", "config_version": 14}], "cumulative_needs_attention_view_error": false, "id": "id", "location": "location", "resource_group": "resource_group", "state": "state", "event_notifications_crn": "event_notifications_crn", "definition": {"name": "name", "description": "description", "destroy_on_delete": true}, "configs": [{"id": "id", "project_id": "project_id", "version": 7, "is_draft": true, "needs_attention_state": ["anyValue"], "state": "state", "pipeline_state": "pipeline_state", "update_available": true, "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "last_approved": {"is_forced": false, "comment": "comment", "timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id"}, "last_save": "2019-01-01T12:00:00.000Z", "active_draft": {"version": 7, "state": "state", "pipeline_state": "pipeline_state", "href": "href"}, "definition": {"name": "name", "labels": ["labels"], "description": "description", "authorizations": {"trusted_profile": {"id": "id", "target_iam_id": "target_iam_id"}, "method": "method", "api_key": "api_key"}, "compliance_profile": {"id": "id", "instance_id": "instance_id", "instance_location": "instance_location", "attachment_id": "attachment_id", "profile_name": "profile_name"}, "locator_id": "locator_id", "type": "terraform_template", "input": [{"name": "name", "type": "array", "value": "anyValue", "required": true}], "output": [{"name": "name", "description": "description", "value": "anyValue"}], "setting": [{"name": "name", "value": "value"}]}, "href": "href"}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a ProjectConfigAuthTrustedProfile model
        project_config_auth_trusted_profile_model = {}
        project_config_auth_trusted_profile_model['id'] = 'testString'
        project_config_auth_trusted_profile_model['target_iam_id'] = 'testString'

        # Construct a dict representation of a ProjectConfigAuth model
        project_config_auth_model = {}
        project_config_auth_model['trusted_profile'] = project_config_auth_trusted_profile_model
        project_config_auth_model['method'] = 'testString'
        project_config_auth_model['api_key'] = 'testString'

        # Construct a dict representation of a ProjectConfigComplianceProfile model
        project_config_compliance_profile_model = {}
        project_config_compliance_profile_model['id'] = 'testString'
        project_config_compliance_profile_model['instance_id'] = 'testString'
        project_config_compliance_profile_model['instance_location'] = 'testString'
        project_config_compliance_profile_model['attachment_id'] = 'testString'
        project_config_compliance_profile_model['profile_name'] = 'testString'

        # Construct a dict representation of a ProjectConfigInputVariable model
        project_config_input_variable_model = {}
        project_config_input_variable_model['name'] = 'testString'
        project_config_input_variable_model['value'] = 'testString'

        # Construct a dict representation of a ProjectConfigSettingCollection model
        project_config_setting_collection_model = {}
        project_config_setting_collection_model['name'] = 'testString'
        project_config_setting_collection_model['value'] = 'testString'

        # Construct a dict representation of a ProjectConfigPrototype model
        project_config_prototype_model = {}
        project_config_prototype_model['name'] = 'common-variables'
        project_config_prototype_model['labels'] = []
        project_config_prototype_model['description'] = 'testString'
        project_config_prototype_model['authorizations'] = project_config_auth_model
        project_config_prototype_model['compliance_profile'] = project_config_compliance_profile_model
        project_config_prototype_model[
            'locator_id'
        ] = '1082e7d2-5e2f-0a11-a3bc-f88a8e1931fc.018edf04-e772-4ca2-9785-03e8e03bef72-global'
        project_config_prototype_model['input'] = [project_config_input_variable_model]
        project_config_prototype_model['setting'] = [project_config_setting_collection_model]

        # Set up parameter values
        resource_group = 'Default'
        location = 'us-south'
        name = 'acme-microservice'
        description = 'A microservice to deploy on top of ACME infrastructure.'
        destroy_on_delete = True
        configs = [project_config_prototype_model]

        # Invoke method
        response = _service.create_project(
            resource_group,
            location,
            name,
            description=description,
            destroy_on_delete=destroy_on_delete,
            configs=configs,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'resource_group={}'.format(resource_group) in query_string
        assert 'location={}'.format(location) in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'acme-microservice'
        assert req_body['description'] == 'A microservice to deploy on top of ACME infrastructure.'
        assert req_body['destroy_on_delete'] == True
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
        mock_response = '{"crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::", "created_at": "2019-01-01T12:00:00.000Z", "cumulative_needs_attention_view": [{"event": "event", "event_id": "event_id", "config_id": "config_id", "config_version": 14}], "cumulative_needs_attention_view_error": false, "id": "id", "location": "location", "resource_group": "resource_group", "state": "state", "event_notifications_crn": "event_notifications_crn", "definition": {"name": "name", "description": "description", "destroy_on_delete": true}, "configs": [{"id": "id", "project_id": "project_id", "version": 7, "is_draft": true, "needs_attention_state": ["anyValue"], "state": "state", "pipeline_state": "pipeline_state", "update_available": true, "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "last_approved": {"is_forced": false, "comment": "comment", "timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id"}, "last_save": "2019-01-01T12:00:00.000Z", "active_draft": {"version": 7, "state": "state", "pipeline_state": "pipeline_state", "href": "href"}, "definition": {"name": "name", "labels": ["labels"], "description": "description", "authorizations": {"trusted_profile": {"id": "id", "target_iam_id": "target_iam_id"}, "method": "method", "api_key": "api_key"}, "compliance_profile": {"id": "id", "instance_id": "instance_id", "instance_location": "instance_location", "attachment_id": "attachment_id", "profile_name": "profile_name"}, "locator_id": "locator_id", "type": "terraform_template", "input": [{"name": "name", "type": "array", "value": "anyValue", "required": true}], "output": [{"name": "name", "description": "description", "value": "anyValue"}], "setting": [{"name": "name", "value": "value"}]}, "href": "href"}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a ProjectConfigAuthTrustedProfile model
        project_config_auth_trusted_profile_model = {}
        project_config_auth_trusted_profile_model['id'] = 'testString'
        project_config_auth_trusted_profile_model['target_iam_id'] = 'testString'

        # Construct a dict representation of a ProjectConfigAuth model
        project_config_auth_model = {}
        project_config_auth_model['trusted_profile'] = project_config_auth_trusted_profile_model
        project_config_auth_model['method'] = 'testString'
        project_config_auth_model['api_key'] = 'testString'

        # Construct a dict representation of a ProjectConfigComplianceProfile model
        project_config_compliance_profile_model = {}
        project_config_compliance_profile_model['id'] = 'testString'
        project_config_compliance_profile_model['instance_id'] = 'testString'
        project_config_compliance_profile_model['instance_location'] = 'testString'
        project_config_compliance_profile_model['attachment_id'] = 'testString'
        project_config_compliance_profile_model['profile_name'] = 'testString'

        # Construct a dict representation of a ProjectConfigInputVariable model
        project_config_input_variable_model = {}
        project_config_input_variable_model['name'] = 'testString'
        project_config_input_variable_model['value'] = 'testString'

        # Construct a dict representation of a ProjectConfigSettingCollection model
        project_config_setting_collection_model = {}
        project_config_setting_collection_model['name'] = 'testString'
        project_config_setting_collection_model['value'] = 'testString'

        # Construct a dict representation of a ProjectConfigPrototype model
        project_config_prototype_model = {}
        project_config_prototype_model['name'] = 'common-variables'
        project_config_prototype_model['labels'] = []
        project_config_prototype_model['description'] = 'testString'
        project_config_prototype_model['authorizations'] = project_config_auth_model
        project_config_prototype_model['compliance_profile'] = project_config_compliance_profile_model
        project_config_prototype_model[
            'locator_id'
        ] = '1082e7d2-5e2f-0a11-a3bc-f88a8e1931fc.018edf04-e772-4ca2-9785-03e8e03bef72-global'
        project_config_prototype_model['input'] = [project_config_input_variable_model]
        project_config_prototype_model['setting'] = [project_config_setting_collection_model]

        # Set up parameter values
        resource_group = 'Default'
        location = 'us-south'
        name = 'acme-microservice'
        description = 'A microservice to deploy on top of ACME infrastructure.'
        destroy_on_delete = True
        configs = [project_config_prototype_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "resource_group": resource_group,
            "location": location,
            "name": name,
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
        mock_response = '{"limit": 10, "total_count": 0, "first": {"href": "href", "start": "start"}, "last": {"href": "href", "start": "start"}, "previous": {"href": "href", "start": "start"}, "next": {"href": "href", "start": "start"}, "projects": [{"crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::", "created_at": "2019-01-01T12:00:00.000Z", "cumulative_needs_attention_view": [{"event": "event", "event_id": "event_id", "config_id": "config_id", "config_version": 14}], "cumulative_needs_attention_view_error": false, "id": "id", "location": "location", "resource_group": "resource_group", "state": "state", "event_notifications_crn": "event_notifications_crn", "definition": {"name": "name", "description": "description", "destroy_on_delete": true}}]}'
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
        mock_response = '{"limit": 10, "total_count": 0, "first": {"href": "href", "start": "start"}, "last": {"href": "href", "start": "start"}, "previous": {"href": "href", "start": "start"}, "next": {"href": "href", "start": "start"}, "projects": [{"crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::", "created_at": "2019-01-01T12:00:00.000Z", "cumulative_needs_attention_view": [{"event": "event", "event_id": "event_id", "config_id": "config_id", "config_version": 14}], "cumulative_needs_attention_view_error": false, "id": "id", "location": "location", "resource_group": "resource_group", "state": "state", "event_notifications_crn": "event_notifications_crn", "definition": {"name": "name", "description": "description", "destroy_on_delete": true}}]}'
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
        mock_response1 = '{"next":{"start":"1"},"projects":[{"crn":"crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::","created_at":"2019-01-01T12:00:00.000Z","cumulative_needs_attention_view":[{"event":"event","event_id":"event_id","config_id":"config_id","config_version":14}],"cumulative_needs_attention_view_error":false,"id":"id","location":"location","resource_group":"resource_group","state":"state","event_notifications_crn":"event_notifications_crn","definition":{"name":"name","description":"description","destroy_on_delete":true}}],"total_count":2,"limit":1}'
        mock_response2 = '{"projects":[{"crn":"crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::","created_at":"2019-01-01T12:00:00.000Z","cumulative_needs_attention_view":[{"event":"event","event_id":"event_id","config_id":"config_id","config_version":14}],"cumulative_needs_attention_view_error":false,"id":"id","location":"location","resource_group":"resource_group","state":"state","event_notifications_crn":"event_notifications_crn","definition":{"name":"name","description":"description","destroy_on_delete":true}}],"total_count":2,"limit":1}'
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
        mock_response1 = '{"next":{"start":"1"},"projects":[{"crn":"crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::","created_at":"2019-01-01T12:00:00.000Z","cumulative_needs_attention_view":[{"event":"event","event_id":"event_id","config_id":"config_id","config_version":14}],"cumulative_needs_attention_view_error":false,"id":"id","location":"location","resource_group":"resource_group","state":"state","event_notifications_crn":"event_notifications_crn","definition":{"name":"name","description":"description","destroy_on_delete":true}}],"total_count":2,"limit":1}'
        mock_response2 = '{"projects":[{"crn":"crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::","created_at":"2019-01-01T12:00:00.000Z","cumulative_needs_attention_view":[{"event":"event","event_id":"event_id","config_id":"config_id","config_version":14}],"cumulative_needs_attention_view_error":false,"id":"id","location":"location","resource_group":"resource_group","state":"state","event_notifications_crn":"event_notifications_crn","definition":{"name":"name","description":"description","destroy_on_delete":true}}],"total_count":2,"limit":1}'
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
        mock_response = '{"crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::", "created_at": "2019-01-01T12:00:00.000Z", "cumulative_needs_attention_view": [{"event": "event", "event_id": "event_id", "config_id": "config_id", "config_version": 14}], "cumulative_needs_attention_view_error": false, "id": "id", "location": "location", "resource_group": "resource_group", "state": "state", "event_notifications_crn": "event_notifications_crn", "definition": {"name": "name", "description": "description", "destroy_on_delete": true}}'
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
        mock_response = '{"crn": "crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::", "created_at": "2019-01-01T12:00:00.000Z", "cumulative_needs_attention_view": [{"event": "event", "event_id": "event_id", "config_id": "config_id", "config_version": 14}], "cumulative_needs_attention_view_error": false, "id": "id", "location": "location", "resource_group": "resource_group", "state": "state", "event_notifications_crn": "event_notifications_crn", "definition": {"name": "name", "description": "description", "destroy_on_delete": true}}'
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
        mock_response = '{"id": "id", "project_id": "project_id", "version": 7, "is_draft": true, "needs_attention_state": ["anyValue"], "state": "state", "pipeline_state": "pipeline_state", "update_available": true, "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "last_approved": {"is_forced": false, "comment": "comment", "timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id"}, "last_save": "2019-01-01T12:00:00.000Z", "job_summary": {"plan_summary": {"anyKey": "anyValue"}, "apply_summary": {"anyKey": "anyValue"}, "destroy_summary": {"anyKey": "anyValue"}, "message_summary": {"anyKey": "anyValue"}, "plan_messages": {"anyKey": "anyValue"}, "apply_messages": {"anyKey": "anyValue"}, "destroy_messages": {"anyKey": "anyValue"}}, "cra_logs": {"cra_version": "cra_version", "schema_version": "schema_version", "status": "status", "summary": {"anyKey": "anyValue"}, "timestamp": "2019-01-01T12:00:00.000Z"}, "cost_estimate": {"version": "version", "currency": "currency", "totalHourlyCost": "total_hourly_cost", "totalMonthlyCost": "total_monthly_cost", "pastTotalHourlyCost": "past_total_hourly_cost", "pastTotalMonthlyCost": "past_total_monthly_cost", "diffTotalHourlyCost": "diff_total_hourly_cost", "diffTotalMonthlyCost": "diff_total_monthly_cost", "timeGenerated": "2019-01-01T12:00:00.000Z", "user_id": "user_id"}, "last_deployment_job_summary": {"plan_summary": {"anyKey": "anyValue"}, "apply_summary": {"anyKey": "anyValue"}, "destroy_summary": {"anyKey": "anyValue"}, "message_summary": {"anyKey": "anyValue"}, "plan_messages": {"anyKey": "anyValue"}, "apply_messages": {"anyKey": "anyValue"}, "destroy_messages": {"anyKey": "anyValue"}}, "definition": {"name": "name", "labels": ["labels"], "description": "description", "authorizations": {"trusted_profile": {"id": "id", "target_iam_id": "target_iam_id"}, "method": "method", "api_key": "api_key"}, "compliance_profile": {"id": "id", "instance_id": "instance_id", "instance_location": "instance_location", "attachment_id": "attachment_id", "profile_name": "profile_name"}, "locator_id": "locator_id", "type": "terraform_template", "input": [{"name": "name", "type": "array", "value": "anyValue", "required": true}], "output": [{"name": "name", "description": "description", "value": "anyValue"}], "setting": [{"name": "name", "value": "value"}]}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a ProjectConfigAuthTrustedProfile model
        project_config_auth_trusted_profile_model = {}
        project_config_auth_trusted_profile_model['id'] = 'testString'
        project_config_auth_trusted_profile_model['target_iam_id'] = 'testString'

        # Construct a dict representation of a ProjectConfigAuth model
        project_config_auth_model = {}
        project_config_auth_model['trusted_profile'] = project_config_auth_trusted_profile_model
        project_config_auth_model['method'] = 'testString'
        project_config_auth_model['api_key'] = 'testString'

        # Construct a dict representation of a ProjectConfigComplianceProfile model
        project_config_compliance_profile_model = {}
        project_config_compliance_profile_model['id'] = 'testString'
        project_config_compliance_profile_model['instance_id'] = 'testString'
        project_config_compliance_profile_model['instance_location'] = 'testString'
        project_config_compliance_profile_model['attachment_id'] = 'testString'
        project_config_compliance_profile_model['profile_name'] = 'testString'

        # Construct a dict representation of a ProjectConfigInputVariable model
        project_config_input_variable_model = {}
        project_config_input_variable_model['name'] = 'account_id'
        project_config_input_variable_model['value'] = '$configs[].name["account-stage"].input.account_id'

        # Construct a dict representation of a ProjectConfigSettingCollection model
        project_config_setting_collection_model = {}
        project_config_setting_collection_model['name'] = 'IBMCLOUD_TOOLCHAIN_ENDPOINT'
        project_config_setting_collection_model['value'] = 'https://api.us-south.devops.dev.cloud.ibm.com'

        # Set up parameter values
        project_id = 'testString'
        name = 'env-stage'
        locator_id = '1082e7d2-5e2f-0a11-a3bc-f88a8e1931fc.018edf04-e772-4ca2-9785-03e8e03bef72-global'
        labels = ['env:stage', 'governance:test', 'build:0']
        description = 'Stage environment configuration, which includes services common to all the environment regions. There must be a blueprint configuring all the services common to the stage regions. It is a terraform_template type of configuration that points to a Github repo hosting the terraform modules that can be deployed by a Schematics Workspace.'
        authorizations = project_config_auth_model
        compliance_profile = project_config_compliance_profile_model
        input = [project_config_input_variable_model]
        setting = [project_config_setting_collection_model]

        # Invoke method
        response = _service.create_config(
            project_id,
            name,
            locator_id,
            labels=labels,
            description=description,
            authorizations=authorizations,
            compliance_profile=compliance_profile,
            input=input,
            setting=setting,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'env-stage'
        assert (
            req_body['locator_id'] == '1082e7d2-5e2f-0a11-a3bc-f88a8e1931fc.018edf04-e772-4ca2-9785-03e8e03bef72-global'
        )
        assert req_body['labels'] == ['env:stage', 'governance:test', 'build:0']
        assert (
            req_body['description']
            == 'Stage environment configuration, which includes services common to all the environment regions. There must be a blueprint configuring all the services common to the stage regions. It is a terraform_template type of configuration that points to a Github repo hosting the terraform modules that can be deployed by a Schematics Workspace.'
        )
        assert req_body['authorizations'] == project_config_auth_model
        assert req_body['compliance_profile'] == project_config_compliance_profile_model
        assert req_body['input'] == [project_config_input_variable_model]
        assert req_body['setting'] == [project_config_setting_collection_model]

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
        mock_response = '{"id": "id", "project_id": "project_id", "version": 7, "is_draft": true, "needs_attention_state": ["anyValue"], "state": "state", "pipeline_state": "pipeline_state", "update_available": true, "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "last_approved": {"is_forced": false, "comment": "comment", "timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id"}, "last_save": "2019-01-01T12:00:00.000Z", "job_summary": {"plan_summary": {"anyKey": "anyValue"}, "apply_summary": {"anyKey": "anyValue"}, "destroy_summary": {"anyKey": "anyValue"}, "message_summary": {"anyKey": "anyValue"}, "plan_messages": {"anyKey": "anyValue"}, "apply_messages": {"anyKey": "anyValue"}, "destroy_messages": {"anyKey": "anyValue"}}, "cra_logs": {"cra_version": "cra_version", "schema_version": "schema_version", "status": "status", "summary": {"anyKey": "anyValue"}, "timestamp": "2019-01-01T12:00:00.000Z"}, "cost_estimate": {"version": "version", "currency": "currency", "totalHourlyCost": "total_hourly_cost", "totalMonthlyCost": "total_monthly_cost", "pastTotalHourlyCost": "past_total_hourly_cost", "pastTotalMonthlyCost": "past_total_monthly_cost", "diffTotalHourlyCost": "diff_total_hourly_cost", "diffTotalMonthlyCost": "diff_total_monthly_cost", "timeGenerated": "2019-01-01T12:00:00.000Z", "user_id": "user_id"}, "last_deployment_job_summary": {"plan_summary": {"anyKey": "anyValue"}, "apply_summary": {"anyKey": "anyValue"}, "destroy_summary": {"anyKey": "anyValue"}, "message_summary": {"anyKey": "anyValue"}, "plan_messages": {"anyKey": "anyValue"}, "apply_messages": {"anyKey": "anyValue"}, "destroy_messages": {"anyKey": "anyValue"}}, "definition": {"name": "name", "labels": ["labels"], "description": "description", "authorizations": {"trusted_profile": {"id": "id", "target_iam_id": "target_iam_id"}, "method": "method", "api_key": "api_key"}, "compliance_profile": {"id": "id", "instance_id": "instance_id", "instance_location": "instance_location", "attachment_id": "attachment_id", "profile_name": "profile_name"}, "locator_id": "locator_id", "type": "terraform_template", "input": [{"name": "name", "type": "array", "value": "anyValue", "required": true}], "output": [{"name": "name", "description": "description", "value": "anyValue"}], "setting": [{"name": "name", "value": "value"}]}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a ProjectConfigAuthTrustedProfile model
        project_config_auth_trusted_profile_model = {}
        project_config_auth_trusted_profile_model['id'] = 'testString'
        project_config_auth_trusted_profile_model['target_iam_id'] = 'testString'

        # Construct a dict representation of a ProjectConfigAuth model
        project_config_auth_model = {}
        project_config_auth_model['trusted_profile'] = project_config_auth_trusted_profile_model
        project_config_auth_model['method'] = 'testString'
        project_config_auth_model['api_key'] = 'testString'

        # Construct a dict representation of a ProjectConfigComplianceProfile model
        project_config_compliance_profile_model = {}
        project_config_compliance_profile_model['id'] = 'testString'
        project_config_compliance_profile_model['instance_id'] = 'testString'
        project_config_compliance_profile_model['instance_location'] = 'testString'
        project_config_compliance_profile_model['attachment_id'] = 'testString'
        project_config_compliance_profile_model['profile_name'] = 'testString'

        # Construct a dict representation of a ProjectConfigInputVariable model
        project_config_input_variable_model = {}
        project_config_input_variable_model['name'] = 'account_id'
        project_config_input_variable_model['value'] = '$configs[].name["account-stage"].input.account_id'

        # Construct a dict representation of a ProjectConfigSettingCollection model
        project_config_setting_collection_model = {}
        project_config_setting_collection_model['name'] = 'IBMCLOUD_TOOLCHAIN_ENDPOINT'
        project_config_setting_collection_model['value'] = 'https://api.us-south.devops.dev.cloud.ibm.com'

        # Set up parameter values
        project_id = 'testString'
        name = 'env-stage'
        locator_id = '1082e7d2-5e2f-0a11-a3bc-f88a8e1931fc.018edf04-e772-4ca2-9785-03e8e03bef72-global'
        labels = ['env:stage', 'governance:test', 'build:0']
        description = 'Stage environment configuration, which includes services common to all the environment regions. There must be a blueprint configuring all the services common to the stage regions. It is a terraform_template type of configuration that points to a Github repo hosting the terraform modules that can be deployed by a Schematics Workspace.'
        authorizations = project_config_auth_model
        compliance_profile = project_config_compliance_profile_model
        input = [project_config_input_variable_model]
        setting = [project_config_setting_collection_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "name": name,
            "locator_id": locator_id,
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
        mock_response = '{"configs": [{"id": "id", "project_id": "project_id", "version": 7, "is_draft": true, "needs_attention_state": ["anyValue"], "state": "state", "pipeline_state": "pipeline_state", "update_available": true, "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "last_approved": {"is_forced": false, "comment": "comment", "timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id"}, "last_save": "2019-01-01T12:00:00.000Z", "active_draft": {"version": 7, "state": "state", "pipeline_state": "pipeline_state", "href": "href"}, "definition": {"name": "name", "labels": ["labels"], "description": "description", "authorizations": {"trusted_profile": {"id": "id", "target_iam_id": "target_iam_id"}, "method": "method", "api_key": "api_key"}, "compliance_profile": {"id": "id", "instance_id": "instance_id", "instance_location": "instance_location", "attachment_id": "attachment_id", "profile_name": "profile_name"}, "locator_id": "locator_id", "type": "terraform_template", "input": [{"name": "name", "type": "array", "value": "anyValue", "required": true}], "output": [{"name": "name", "description": "description", "value": "anyValue"}], "setting": [{"name": "name", "value": "value"}]}, "href": "href"}]}'
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
        mock_response = '{"configs": [{"id": "id", "project_id": "project_id", "version": 7, "is_draft": true, "needs_attention_state": ["anyValue"], "state": "state", "pipeline_state": "pipeline_state", "update_available": true, "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "last_approved": {"is_forced": false, "comment": "comment", "timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id"}, "last_save": "2019-01-01T12:00:00.000Z", "active_draft": {"version": 7, "state": "state", "pipeline_state": "pipeline_state", "href": "href"}, "definition": {"name": "name", "labels": ["labels"], "description": "description", "authorizations": {"trusted_profile": {"id": "id", "target_iam_id": "target_iam_id"}, "method": "method", "api_key": "api_key"}, "compliance_profile": {"id": "id", "instance_id": "instance_id", "instance_location": "instance_location", "attachment_id": "attachment_id", "profile_name": "profile_name"}, "locator_id": "locator_id", "type": "terraform_template", "input": [{"name": "name", "type": "array", "value": "anyValue", "required": true}], "output": [{"name": "name", "description": "description", "value": "anyValue"}], "setting": [{"name": "name", "value": "value"}]}, "href": "href"}]}'
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
        mock_response = '{"id": "id", "project_id": "project_id", "version": 7, "is_draft": true, "needs_attention_state": ["anyValue"], "state": "state", "pipeline_state": "pipeline_state", "update_available": true, "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "last_approved": {"is_forced": false, "comment": "comment", "timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id"}, "last_save": "2019-01-01T12:00:00.000Z", "job_summary": {"plan_summary": {"anyKey": "anyValue"}, "apply_summary": {"anyKey": "anyValue"}, "destroy_summary": {"anyKey": "anyValue"}, "message_summary": {"anyKey": "anyValue"}, "plan_messages": {"anyKey": "anyValue"}, "apply_messages": {"anyKey": "anyValue"}, "destroy_messages": {"anyKey": "anyValue"}}, "cra_logs": {"cra_version": "cra_version", "schema_version": "schema_version", "status": "status", "summary": {"anyKey": "anyValue"}, "timestamp": "2019-01-01T12:00:00.000Z"}, "cost_estimate": {"version": "version", "currency": "currency", "totalHourlyCost": "total_hourly_cost", "totalMonthlyCost": "total_monthly_cost", "pastTotalHourlyCost": "past_total_hourly_cost", "pastTotalMonthlyCost": "past_total_monthly_cost", "diffTotalHourlyCost": "diff_total_hourly_cost", "diffTotalMonthlyCost": "diff_total_monthly_cost", "timeGenerated": "2019-01-01T12:00:00.000Z", "user_id": "user_id"}, "last_deployment_job_summary": {"plan_summary": {"anyKey": "anyValue"}, "apply_summary": {"anyKey": "anyValue"}, "destroy_summary": {"anyKey": "anyValue"}, "message_summary": {"anyKey": "anyValue"}, "plan_messages": {"anyKey": "anyValue"}, "apply_messages": {"anyKey": "anyValue"}, "destroy_messages": {"anyKey": "anyValue"}}, "active_draft": {"version": 7, "state": "state", "pipeline_state": "pipeline_state", "href": "href"}, "definition": {"name": "name", "labels": ["labels"], "description": "description", "authorizations": {"trusted_profile": {"id": "id", "target_iam_id": "target_iam_id"}, "method": "method", "api_key": "api_key"}, "compliance_profile": {"id": "id", "instance_id": "instance_id", "instance_location": "instance_location", "attachment_id": "attachment_id", "profile_name": "profile_name"}, "locator_id": "locator_id", "type": "terraform_template", "input": [{"name": "name", "type": "array", "value": "anyValue", "required": true}], "output": [{"name": "name", "description": "description", "value": "anyValue"}], "setting": [{"name": "name", "value": "value"}]}}'
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
        mock_response = '{"id": "id", "project_id": "project_id", "version": 7, "is_draft": true, "needs_attention_state": ["anyValue"], "state": "state", "pipeline_state": "pipeline_state", "update_available": true, "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "last_approved": {"is_forced": false, "comment": "comment", "timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id"}, "last_save": "2019-01-01T12:00:00.000Z", "job_summary": {"plan_summary": {"anyKey": "anyValue"}, "apply_summary": {"anyKey": "anyValue"}, "destroy_summary": {"anyKey": "anyValue"}, "message_summary": {"anyKey": "anyValue"}, "plan_messages": {"anyKey": "anyValue"}, "apply_messages": {"anyKey": "anyValue"}, "destroy_messages": {"anyKey": "anyValue"}}, "cra_logs": {"cra_version": "cra_version", "schema_version": "schema_version", "status": "status", "summary": {"anyKey": "anyValue"}, "timestamp": "2019-01-01T12:00:00.000Z"}, "cost_estimate": {"version": "version", "currency": "currency", "totalHourlyCost": "total_hourly_cost", "totalMonthlyCost": "total_monthly_cost", "pastTotalHourlyCost": "past_total_hourly_cost", "pastTotalMonthlyCost": "past_total_monthly_cost", "diffTotalHourlyCost": "diff_total_hourly_cost", "diffTotalMonthlyCost": "diff_total_monthly_cost", "timeGenerated": "2019-01-01T12:00:00.000Z", "user_id": "user_id"}, "last_deployment_job_summary": {"plan_summary": {"anyKey": "anyValue"}, "apply_summary": {"anyKey": "anyValue"}, "destroy_summary": {"anyKey": "anyValue"}, "message_summary": {"anyKey": "anyValue"}, "plan_messages": {"anyKey": "anyValue"}, "apply_messages": {"anyKey": "anyValue"}, "destroy_messages": {"anyKey": "anyValue"}}, "active_draft": {"version": 7, "state": "state", "pipeline_state": "pipeline_state", "href": "href"}, "definition": {"name": "name", "labels": ["labels"], "description": "description", "authorizations": {"trusted_profile": {"id": "id", "target_iam_id": "target_iam_id"}, "method": "method", "api_key": "api_key"}, "compliance_profile": {"id": "id", "instance_id": "instance_id", "instance_location": "instance_location", "attachment_id": "attachment_id", "profile_name": "profile_name"}, "locator_id": "locator_id", "type": "terraform_template", "input": [{"name": "name", "type": "array", "value": "anyValue", "required": true}], "output": [{"name": "name", "description": "description", "value": "anyValue"}], "setting": [{"name": "name", "value": "value"}]}}'
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
        mock_response = '{"id": "id", "project_id": "project_id", "version": 7, "is_draft": true, "needs_attention_state": ["anyValue"], "state": "state", "pipeline_state": "pipeline_state", "update_available": true, "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "last_approved": {"is_forced": false, "comment": "comment", "timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id"}, "last_save": "2019-01-01T12:00:00.000Z", "job_summary": {"plan_summary": {"anyKey": "anyValue"}, "apply_summary": {"anyKey": "anyValue"}, "destroy_summary": {"anyKey": "anyValue"}, "message_summary": {"anyKey": "anyValue"}, "plan_messages": {"anyKey": "anyValue"}, "apply_messages": {"anyKey": "anyValue"}, "destroy_messages": {"anyKey": "anyValue"}}, "cra_logs": {"cra_version": "cra_version", "schema_version": "schema_version", "status": "status", "summary": {"anyKey": "anyValue"}, "timestamp": "2019-01-01T12:00:00.000Z"}, "cost_estimate": {"version": "version", "currency": "currency", "totalHourlyCost": "total_hourly_cost", "totalMonthlyCost": "total_monthly_cost", "pastTotalHourlyCost": "past_total_hourly_cost", "pastTotalMonthlyCost": "past_total_monthly_cost", "diffTotalHourlyCost": "diff_total_hourly_cost", "diffTotalMonthlyCost": "diff_total_monthly_cost", "timeGenerated": "2019-01-01T12:00:00.000Z", "user_id": "user_id"}, "last_deployment_job_summary": {"plan_summary": {"anyKey": "anyValue"}, "apply_summary": {"anyKey": "anyValue"}, "destroy_summary": {"anyKey": "anyValue"}, "message_summary": {"anyKey": "anyValue"}, "plan_messages": {"anyKey": "anyValue"}, "apply_messages": {"anyKey": "anyValue"}, "destroy_messages": {"anyKey": "anyValue"}}, "definition": {"name": "name", "labels": ["labels"], "description": "description", "authorizations": {"trusted_profile": {"id": "id", "target_iam_id": "target_iam_id"}, "method": "method", "api_key": "api_key"}, "compliance_profile": {"id": "id", "instance_id": "instance_id", "instance_location": "instance_location", "attachment_id": "attachment_id", "profile_name": "profile_name"}, "locator_id": "locator_id", "type": "terraform_template", "input": [{"name": "name", "type": "array", "value": "anyValue", "required": true}], "output": [{"name": "name", "description": "description", "value": "anyValue"}], "setting": [{"name": "name", "value": "value"}]}}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a ProjectConfigInputVariable model
        project_config_input_variable_model = {}
        project_config_input_variable_model['name'] = 'account_id'
        project_config_input_variable_model['value'] = '$configs[].name["account-stage"].input.account_id'

        # Construct a dict representation of a ProjectConfigSettingCollection model
        project_config_setting_collection_model = {}
        project_config_setting_collection_model['name'] = 'testString'
        project_config_setting_collection_model['value'] = 'testString'

        # Construct a dict representation of a ProjectConfigAuthTrustedProfile model
        project_config_auth_trusted_profile_model = {}
        project_config_auth_trusted_profile_model['id'] = 'testString'
        project_config_auth_trusted_profile_model['target_iam_id'] = 'testString'

        # Construct a dict representation of a ProjectConfigAuth model
        project_config_auth_model = {}
        project_config_auth_model['trusted_profile'] = project_config_auth_trusted_profile_model
        project_config_auth_model['method'] = 'testString'
        project_config_auth_model['api_key'] = 'testString'

        # Construct a dict representation of a ProjectConfigComplianceProfile model
        project_config_compliance_profile_model = {}
        project_config_compliance_profile_model['id'] = 'testString'
        project_config_compliance_profile_model['instance_id'] = 'testString'
        project_config_compliance_profile_model['instance_location'] = 'testString'
        project_config_compliance_profile_model['attachment_id'] = 'testString'
        project_config_compliance_profile_model['profile_name'] = 'testString'

        # Set up parameter values
        project_id = 'testString'
        id = 'testString'
        locator_id = 'testString'
        input = [project_config_input_variable_model]
        setting = [project_config_setting_collection_model]
        name = 'testString'
        labels = ['testString']
        description = 'testString'
        authorizations = project_config_auth_model
        compliance_profile = project_config_compliance_profile_model

        # Invoke method
        response = _service.update_config(
            project_id,
            id,
            locator_id=locator_id,
            input=input,
            setting=setting,
            name=name,
            labels=labels,
            description=description,
            authorizations=authorizations,
            compliance_profile=compliance_profile,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['locator_id'] == 'testString'
        assert req_body['input'] == [project_config_input_variable_model]
        assert req_body['setting'] == [project_config_setting_collection_model]
        assert req_body['name'] == 'testString'
        assert req_body['labels'] == ['testString']
        assert req_body['description'] == 'testString'
        assert req_body['authorizations'] == project_config_auth_model
        assert req_body['compliance_profile'] == project_config_compliance_profile_model

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
        mock_response = '{"id": "id", "project_id": "project_id", "version": 7, "is_draft": true, "needs_attention_state": ["anyValue"], "state": "state", "pipeline_state": "pipeline_state", "update_available": true, "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "last_approved": {"is_forced": false, "comment": "comment", "timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id"}, "last_save": "2019-01-01T12:00:00.000Z", "job_summary": {"plan_summary": {"anyKey": "anyValue"}, "apply_summary": {"anyKey": "anyValue"}, "destroy_summary": {"anyKey": "anyValue"}, "message_summary": {"anyKey": "anyValue"}, "plan_messages": {"anyKey": "anyValue"}, "apply_messages": {"anyKey": "anyValue"}, "destroy_messages": {"anyKey": "anyValue"}}, "cra_logs": {"cra_version": "cra_version", "schema_version": "schema_version", "status": "status", "summary": {"anyKey": "anyValue"}, "timestamp": "2019-01-01T12:00:00.000Z"}, "cost_estimate": {"version": "version", "currency": "currency", "totalHourlyCost": "total_hourly_cost", "totalMonthlyCost": "total_monthly_cost", "pastTotalHourlyCost": "past_total_hourly_cost", "pastTotalMonthlyCost": "past_total_monthly_cost", "diffTotalHourlyCost": "diff_total_hourly_cost", "diffTotalMonthlyCost": "diff_total_monthly_cost", "timeGenerated": "2019-01-01T12:00:00.000Z", "user_id": "user_id"}, "last_deployment_job_summary": {"plan_summary": {"anyKey": "anyValue"}, "apply_summary": {"anyKey": "anyValue"}, "destroy_summary": {"anyKey": "anyValue"}, "message_summary": {"anyKey": "anyValue"}, "plan_messages": {"anyKey": "anyValue"}, "apply_messages": {"anyKey": "anyValue"}, "destroy_messages": {"anyKey": "anyValue"}}, "definition": {"name": "name", "labels": ["labels"], "description": "description", "authorizations": {"trusted_profile": {"id": "id", "target_iam_id": "target_iam_id"}, "method": "method", "api_key": "api_key"}, "compliance_profile": {"id": "id", "instance_id": "instance_id", "instance_location": "instance_location", "attachment_id": "attachment_id", "profile_name": "profile_name"}, "locator_id": "locator_id", "type": "terraform_template", "input": [{"name": "name", "type": "array", "value": "anyValue", "required": true}], "output": [{"name": "name", "description": "description", "value": "anyValue"}], "setting": [{"name": "name", "value": "value"}]}}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a ProjectConfigInputVariable model
        project_config_input_variable_model = {}
        project_config_input_variable_model['name'] = 'account_id'
        project_config_input_variable_model['value'] = '$configs[].name["account-stage"].input.account_id'

        # Construct a dict representation of a ProjectConfigSettingCollection model
        project_config_setting_collection_model = {}
        project_config_setting_collection_model['name'] = 'testString'
        project_config_setting_collection_model['value'] = 'testString'

        # Construct a dict representation of a ProjectConfigAuthTrustedProfile model
        project_config_auth_trusted_profile_model = {}
        project_config_auth_trusted_profile_model['id'] = 'testString'
        project_config_auth_trusted_profile_model['target_iam_id'] = 'testString'

        # Construct a dict representation of a ProjectConfigAuth model
        project_config_auth_model = {}
        project_config_auth_model['trusted_profile'] = project_config_auth_trusted_profile_model
        project_config_auth_model['method'] = 'testString'
        project_config_auth_model['api_key'] = 'testString'

        # Construct a dict representation of a ProjectConfigComplianceProfile model
        project_config_compliance_profile_model = {}
        project_config_compliance_profile_model['id'] = 'testString'
        project_config_compliance_profile_model['instance_id'] = 'testString'
        project_config_compliance_profile_model['instance_location'] = 'testString'
        project_config_compliance_profile_model['attachment_id'] = 'testString'
        project_config_compliance_profile_model['profile_name'] = 'testString'

        # Set up parameter values
        project_id = 'testString'
        id = 'testString'
        locator_id = 'testString'
        input = [project_config_input_variable_model]
        setting = [project_config_setting_collection_model]
        name = 'testString'
        labels = ['testString']
        description = 'testString'
        authorizations = project_config_auth_model
        compliance_profile = project_config_compliance_profile_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "id": id,
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
        draft_only = False

        # Invoke method
        response = _service.delete_config(
            project_id,
            id,
            draft_only=draft_only,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'draft_only={}'.format('true' if draft_only else 'false') in query_string

    def test_delete_config_all_params_with_retries(self):
        # Enable retries and run test_delete_config_all_params.
        _service.enable_retries()
        self.test_delete_config_all_params()

        # Disable retries and run test_delete_config_all_params.
        _service.disable_retries()
        self.test_delete_config_all_params()

    @responses.activate
    def test_delete_config_required_params(self):
        """
        test_delete_config_required_params()
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

    def test_delete_config_required_params_with_retries(self):
        # Enable retries and run test_delete_config_required_params.
        _service.enable_retries()
        self.test_delete_config_required_params()

        # Disable retries and run test_delete_config_required_params.
        _service.disable_retries()
        self.test_delete_config_required_params()

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
        mock_response = '{"id": "id", "project_id": "project_id", "version": 7, "is_draft": true, "needs_attention_state": ["anyValue"], "state": "state", "pipeline_state": "pipeline_state", "update_available": true, "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "last_approved": {"is_forced": false, "comment": "comment", "timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id"}, "last_save": "2019-01-01T12:00:00.000Z", "job_summary": {"plan_summary": {"anyKey": "anyValue"}, "apply_summary": {"anyKey": "anyValue"}, "destroy_summary": {"anyKey": "anyValue"}, "message_summary": {"anyKey": "anyValue"}, "plan_messages": {"anyKey": "anyValue"}, "apply_messages": {"anyKey": "anyValue"}, "destroy_messages": {"anyKey": "anyValue"}}, "cra_logs": {"cra_version": "cra_version", "schema_version": "schema_version", "status": "status", "summary": {"anyKey": "anyValue"}, "timestamp": "2019-01-01T12:00:00.000Z"}, "cost_estimate": {"version": "version", "currency": "currency", "totalHourlyCost": "total_hourly_cost", "totalMonthlyCost": "total_monthly_cost", "pastTotalHourlyCost": "past_total_hourly_cost", "pastTotalMonthlyCost": "past_total_monthly_cost", "diffTotalHourlyCost": "diff_total_hourly_cost", "diffTotalMonthlyCost": "diff_total_monthly_cost", "timeGenerated": "2019-01-01T12:00:00.000Z", "user_id": "user_id"}, "last_deployment_job_summary": {"plan_summary": {"anyKey": "anyValue"}, "apply_summary": {"anyKey": "anyValue"}, "destroy_summary": {"anyKey": "anyValue"}, "message_summary": {"anyKey": "anyValue"}, "plan_messages": {"anyKey": "anyValue"}, "apply_messages": {"anyKey": "anyValue"}, "destroy_messages": {"anyKey": "anyValue"}}, "active_draft": {"version": 7, "state": "state", "pipeline_state": "pipeline_state", "href": "href"}, "definition": {"name": "name", "labels": ["labels"], "description": "description", "authorizations": {"trusted_profile": {"id": "id", "target_iam_id": "target_iam_id"}, "method": "method", "api_key": "api_key"}, "compliance_profile": {"id": "id", "instance_id": "instance_id", "instance_location": "instance_location", "attachment_id": "attachment_id", "profile_name": "profile_name"}, "locator_id": "locator_id", "type": "terraform_template", "input": [{"name": "name", "type": "array", "value": "anyValue", "required": true}], "output": [{"name": "name", "description": "description", "value": "anyValue"}], "setting": [{"name": "name", "value": "value"}]}}'
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
        mock_response = '{"id": "id", "project_id": "project_id", "version": 7, "is_draft": true, "needs_attention_state": ["anyValue"], "state": "state", "pipeline_state": "pipeline_state", "update_available": true, "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "last_approved": {"is_forced": false, "comment": "comment", "timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id"}, "last_save": "2019-01-01T12:00:00.000Z", "job_summary": {"plan_summary": {"anyKey": "anyValue"}, "apply_summary": {"anyKey": "anyValue"}, "destroy_summary": {"anyKey": "anyValue"}, "message_summary": {"anyKey": "anyValue"}, "plan_messages": {"anyKey": "anyValue"}, "apply_messages": {"anyKey": "anyValue"}, "destroy_messages": {"anyKey": "anyValue"}}, "cra_logs": {"cra_version": "cra_version", "schema_version": "schema_version", "status": "status", "summary": {"anyKey": "anyValue"}, "timestamp": "2019-01-01T12:00:00.000Z"}, "cost_estimate": {"version": "version", "currency": "currency", "totalHourlyCost": "total_hourly_cost", "totalMonthlyCost": "total_monthly_cost", "pastTotalHourlyCost": "past_total_hourly_cost", "pastTotalMonthlyCost": "past_total_monthly_cost", "diffTotalHourlyCost": "diff_total_hourly_cost", "diffTotalMonthlyCost": "diff_total_monthly_cost", "timeGenerated": "2019-01-01T12:00:00.000Z", "user_id": "user_id"}, "last_deployment_job_summary": {"plan_summary": {"anyKey": "anyValue"}, "apply_summary": {"anyKey": "anyValue"}, "destroy_summary": {"anyKey": "anyValue"}, "message_summary": {"anyKey": "anyValue"}, "plan_messages": {"anyKey": "anyValue"}, "apply_messages": {"anyKey": "anyValue"}, "destroy_messages": {"anyKey": "anyValue"}}, "active_draft": {"version": 7, "state": "state", "pipeline_state": "pipeline_state", "href": "href"}, "definition": {"name": "name", "labels": ["labels"], "description": "description", "authorizations": {"trusted_profile": {"id": "id", "target_iam_id": "target_iam_id"}, "method": "method", "api_key": "api_key"}, "compliance_profile": {"id": "id", "instance_id": "instance_id", "instance_location": "instance_location", "attachment_id": "attachment_id", "profile_name": "profile_name"}, "locator_id": "locator_id", "type": "terraform_template", "input": [{"name": "name", "type": "array", "value": "anyValue", "required": true}], "output": [{"name": "name", "description": "description", "value": "anyValue"}], "setting": [{"name": "name", "value": "value"}]}}'
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
        mock_response = '{"id": "id", "project_id": "project_id", "version": 7, "is_draft": true, "needs_attention_state": ["anyValue"], "state": "state", "pipeline_state": "pipeline_state", "update_available": true, "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "last_approved": {"is_forced": false, "comment": "comment", "timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id"}, "last_save": "2019-01-01T12:00:00.000Z", "job_summary": {"plan_summary": {"anyKey": "anyValue"}, "apply_summary": {"anyKey": "anyValue"}, "destroy_summary": {"anyKey": "anyValue"}, "message_summary": {"anyKey": "anyValue"}, "plan_messages": {"anyKey": "anyValue"}, "apply_messages": {"anyKey": "anyValue"}, "destroy_messages": {"anyKey": "anyValue"}}, "cra_logs": {"cra_version": "cra_version", "schema_version": "schema_version", "status": "status", "summary": {"anyKey": "anyValue"}, "timestamp": "2019-01-01T12:00:00.000Z"}, "cost_estimate": {"version": "version", "currency": "currency", "totalHourlyCost": "total_hourly_cost", "totalMonthlyCost": "total_monthly_cost", "pastTotalHourlyCost": "past_total_hourly_cost", "pastTotalMonthlyCost": "past_total_monthly_cost", "diffTotalHourlyCost": "diff_total_hourly_cost", "diffTotalMonthlyCost": "diff_total_monthly_cost", "timeGenerated": "2019-01-01T12:00:00.000Z", "user_id": "user_id"}, "last_deployment_job_summary": {"plan_summary": {"anyKey": "anyValue"}, "apply_summary": {"anyKey": "anyValue"}, "destroy_summary": {"anyKey": "anyValue"}, "message_summary": {"anyKey": "anyValue"}, "plan_messages": {"anyKey": "anyValue"}, "apply_messages": {"anyKey": "anyValue"}, "destroy_messages": {"anyKey": "anyValue"}}, "active_draft": {"version": 7, "state": "state", "pipeline_state": "pipeline_state", "href": "href"}, "definition": {"name": "name", "labels": ["labels"], "description": "description", "authorizations": {"trusted_profile": {"id": "id", "target_iam_id": "target_iam_id"}, "method": "method", "api_key": "api_key"}, "compliance_profile": {"id": "id", "instance_id": "instance_id", "instance_location": "instance_location", "attachment_id": "attachment_id", "profile_name": "profile_name"}, "locator_id": "locator_id", "type": "terraform_template", "input": [{"name": "name", "type": "array", "value": "anyValue", "required": true}], "output": [{"name": "name", "description": "description", "value": "anyValue"}], "setting": [{"name": "name", "value": "value"}]}}'
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


class TestCheckConfig:
    """
    Test Class for check_config
    """

    @responses.activate
    def test_check_config_all_params(self):
        """
        check_config()
        """
        # Set up mock
        url = preprocess_url('/v1/projects/testString/configs/testString/check')
        mock_response = '{"id": "id", "project_id": "project_id", "version": 7, "is_draft": true, "needs_attention_state": ["anyValue"], "state": "state", "pipeline_state": "pipeline_state", "update_available": true, "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "last_approved": {"is_forced": false, "comment": "comment", "timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id"}, "last_save": "2019-01-01T12:00:00.000Z", "job_summary": {"plan_summary": {"anyKey": "anyValue"}, "apply_summary": {"anyKey": "anyValue"}, "destroy_summary": {"anyKey": "anyValue"}, "message_summary": {"anyKey": "anyValue"}, "plan_messages": {"anyKey": "anyValue"}, "apply_messages": {"anyKey": "anyValue"}, "destroy_messages": {"anyKey": "anyValue"}}, "cra_logs": {"cra_version": "cra_version", "schema_version": "schema_version", "status": "status", "summary": {"anyKey": "anyValue"}, "timestamp": "2019-01-01T12:00:00.000Z"}, "cost_estimate": {"version": "version", "currency": "currency", "totalHourlyCost": "total_hourly_cost", "totalMonthlyCost": "total_monthly_cost", "pastTotalHourlyCost": "past_total_hourly_cost", "pastTotalMonthlyCost": "past_total_monthly_cost", "diffTotalHourlyCost": "diff_total_hourly_cost", "diffTotalMonthlyCost": "diff_total_monthly_cost", "timeGenerated": "2019-01-01T12:00:00.000Z", "user_id": "user_id"}, "last_deployment_job_summary": {"plan_summary": {"anyKey": "anyValue"}, "apply_summary": {"anyKey": "anyValue"}, "destroy_summary": {"anyKey": "anyValue"}, "message_summary": {"anyKey": "anyValue"}, "plan_messages": {"anyKey": "anyValue"}, "apply_messages": {"anyKey": "anyValue"}, "destroy_messages": {"anyKey": "anyValue"}}, "active_draft": {"version": 7, "state": "state", "pipeline_state": "pipeline_state", "href": "href"}, "definition": {"name": "name", "labels": ["labels"], "description": "description", "authorizations": {"trusted_profile": {"id": "id", "target_iam_id": "target_iam_id"}, "method": "method", "api_key": "api_key"}, "compliance_profile": {"id": "id", "instance_id": "instance_id", "instance_location": "instance_location", "attachment_id": "attachment_id", "profile_name": "profile_name"}, "locator_id": "locator_id", "type": "terraform_template", "input": [{"name": "name", "type": "array", "value": "anyValue", "required": true}], "output": [{"name": "name", "description": "description", "value": "anyValue"}], "setting": [{"name": "name", "value": "value"}]}}'
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
        x_auth_refresh_token = 'testString'
        is_draft = True

        # Invoke method
        response = _service.check_config(
            project_id,
            id,
            x_auth_refresh_token=x_auth_refresh_token,
            is_draft=is_draft,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'is_draft={}'.format('true' if is_draft else 'false') in query_string

    def test_check_config_all_params_with_retries(self):
        # Enable retries and run test_check_config_all_params.
        _service.enable_retries()
        self.test_check_config_all_params()

        # Disable retries and run test_check_config_all_params.
        _service.disable_retries()
        self.test_check_config_all_params()

    @responses.activate
    def test_check_config_required_params(self):
        """
        test_check_config_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/projects/testString/configs/testString/check')
        mock_response = '{"id": "id", "project_id": "project_id", "version": 7, "is_draft": true, "needs_attention_state": ["anyValue"], "state": "state", "pipeline_state": "pipeline_state", "update_available": true, "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "last_approved": {"is_forced": false, "comment": "comment", "timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id"}, "last_save": "2019-01-01T12:00:00.000Z", "job_summary": {"plan_summary": {"anyKey": "anyValue"}, "apply_summary": {"anyKey": "anyValue"}, "destroy_summary": {"anyKey": "anyValue"}, "message_summary": {"anyKey": "anyValue"}, "plan_messages": {"anyKey": "anyValue"}, "apply_messages": {"anyKey": "anyValue"}, "destroy_messages": {"anyKey": "anyValue"}}, "cra_logs": {"cra_version": "cra_version", "schema_version": "schema_version", "status": "status", "summary": {"anyKey": "anyValue"}, "timestamp": "2019-01-01T12:00:00.000Z"}, "cost_estimate": {"version": "version", "currency": "currency", "totalHourlyCost": "total_hourly_cost", "totalMonthlyCost": "total_monthly_cost", "pastTotalHourlyCost": "past_total_hourly_cost", "pastTotalMonthlyCost": "past_total_monthly_cost", "diffTotalHourlyCost": "diff_total_hourly_cost", "diffTotalMonthlyCost": "diff_total_monthly_cost", "timeGenerated": "2019-01-01T12:00:00.000Z", "user_id": "user_id"}, "last_deployment_job_summary": {"plan_summary": {"anyKey": "anyValue"}, "apply_summary": {"anyKey": "anyValue"}, "destroy_summary": {"anyKey": "anyValue"}, "message_summary": {"anyKey": "anyValue"}, "plan_messages": {"anyKey": "anyValue"}, "apply_messages": {"anyKey": "anyValue"}, "destroy_messages": {"anyKey": "anyValue"}}, "active_draft": {"version": 7, "state": "state", "pipeline_state": "pipeline_state", "href": "href"}, "definition": {"name": "name", "labels": ["labels"], "description": "description", "authorizations": {"trusted_profile": {"id": "id", "target_iam_id": "target_iam_id"}, "method": "method", "api_key": "api_key"}, "compliance_profile": {"id": "id", "instance_id": "instance_id", "instance_location": "instance_location", "attachment_id": "attachment_id", "profile_name": "profile_name"}, "locator_id": "locator_id", "type": "terraform_template", "input": [{"name": "name", "type": "array", "value": "anyValue", "required": true}], "output": [{"name": "name", "description": "description", "value": "anyValue"}], "setting": [{"name": "name", "value": "value"}]}}'
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
        response = _service.check_config(
            project_id,
            id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202

    def test_check_config_required_params_with_retries(self):
        # Enable retries and run test_check_config_required_params.
        _service.enable_retries()
        self.test_check_config_required_params()

        # Disable retries and run test_check_config_required_params.
        _service.disable_retries()
        self.test_check_config_required_params()

    @responses.activate
    def test_check_config_value_error(self):
        """
        test_check_config_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/projects/testString/configs/testString/check')
        mock_response = '{"id": "id", "project_id": "project_id", "version": 7, "is_draft": true, "needs_attention_state": ["anyValue"], "state": "state", "pipeline_state": "pipeline_state", "update_available": true, "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "last_approved": {"is_forced": false, "comment": "comment", "timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id"}, "last_save": "2019-01-01T12:00:00.000Z", "job_summary": {"plan_summary": {"anyKey": "anyValue"}, "apply_summary": {"anyKey": "anyValue"}, "destroy_summary": {"anyKey": "anyValue"}, "message_summary": {"anyKey": "anyValue"}, "plan_messages": {"anyKey": "anyValue"}, "apply_messages": {"anyKey": "anyValue"}, "destroy_messages": {"anyKey": "anyValue"}}, "cra_logs": {"cra_version": "cra_version", "schema_version": "schema_version", "status": "status", "summary": {"anyKey": "anyValue"}, "timestamp": "2019-01-01T12:00:00.000Z"}, "cost_estimate": {"version": "version", "currency": "currency", "totalHourlyCost": "total_hourly_cost", "totalMonthlyCost": "total_monthly_cost", "pastTotalHourlyCost": "past_total_hourly_cost", "pastTotalMonthlyCost": "past_total_monthly_cost", "diffTotalHourlyCost": "diff_total_hourly_cost", "diffTotalMonthlyCost": "diff_total_monthly_cost", "timeGenerated": "2019-01-01T12:00:00.000Z", "user_id": "user_id"}, "last_deployment_job_summary": {"plan_summary": {"anyKey": "anyValue"}, "apply_summary": {"anyKey": "anyValue"}, "destroy_summary": {"anyKey": "anyValue"}, "message_summary": {"anyKey": "anyValue"}, "plan_messages": {"anyKey": "anyValue"}, "apply_messages": {"anyKey": "anyValue"}, "destroy_messages": {"anyKey": "anyValue"}}, "active_draft": {"version": 7, "state": "state", "pipeline_state": "pipeline_state", "href": "href"}, "definition": {"name": "name", "labels": ["labels"], "description": "description", "authorizations": {"trusted_profile": {"id": "id", "target_iam_id": "target_iam_id"}, "method": "method", "api_key": "api_key"}, "compliance_profile": {"id": "id", "instance_id": "instance_id", "instance_location": "instance_location", "attachment_id": "attachment_id", "profile_name": "profile_name"}, "locator_id": "locator_id", "type": "terraform_template", "input": [{"name": "name", "type": "array", "value": "anyValue", "required": true}], "output": [{"name": "name", "description": "description", "value": "anyValue"}], "setting": [{"name": "name", "value": "value"}]}}'
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
                _service.check_config(**req_copy)

    def test_check_config_value_error_with_retries(self):
        # Enable retries and run test_check_config_value_error.
        _service.enable_retries()
        self.test_check_config_value_error()

        # Disable retries and run test_check_config_value_error.
        _service.disable_retries()
        self.test_check_config_value_error()


class TestInstallConfig:
    """
    Test Class for install_config
    """

    @responses.activate
    def test_install_config_all_params(self):
        """
        install_config()
        """
        # Set up mock
        url = preprocess_url('/v1/projects/testString/configs/testString/install')
        mock_response = '{"id": "id", "project_id": "project_id", "version": 7, "is_draft": true, "needs_attention_state": ["anyValue"], "state": "state", "pipeline_state": "pipeline_state", "update_available": true, "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "last_approved": {"is_forced": false, "comment": "comment", "timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id"}, "last_save": "2019-01-01T12:00:00.000Z", "job_summary": {"plan_summary": {"anyKey": "anyValue"}, "apply_summary": {"anyKey": "anyValue"}, "destroy_summary": {"anyKey": "anyValue"}, "message_summary": {"anyKey": "anyValue"}, "plan_messages": {"anyKey": "anyValue"}, "apply_messages": {"anyKey": "anyValue"}, "destroy_messages": {"anyKey": "anyValue"}}, "cra_logs": {"cra_version": "cra_version", "schema_version": "schema_version", "status": "status", "summary": {"anyKey": "anyValue"}, "timestamp": "2019-01-01T12:00:00.000Z"}, "cost_estimate": {"version": "version", "currency": "currency", "totalHourlyCost": "total_hourly_cost", "totalMonthlyCost": "total_monthly_cost", "pastTotalHourlyCost": "past_total_hourly_cost", "pastTotalMonthlyCost": "past_total_monthly_cost", "diffTotalHourlyCost": "diff_total_hourly_cost", "diffTotalMonthlyCost": "diff_total_monthly_cost", "timeGenerated": "2019-01-01T12:00:00.000Z", "user_id": "user_id"}, "last_deployment_job_summary": {"plan_summary": {"anyKey": "anyValue"}, "apply_summary": {"anyKey": "anyValue"}, "destroy_summary": {"anyKey": "anyValue"}, "message_summary": {"anyKey": "anyValue"}, "plan_messages": {"anyKey": "anyValue"}, "apply_messages": {"anyKey": "anyValue"}, "destroy_messages": {"anyKey": "anyValue"}}, "active_draft": {"version": 7, "state": "state", "pipeline_state": "pipeline_state", "href": "href"}, "definition": {"name": "name", "labels": ["labels"], "description": "description", "authorizations": {"trusted_profile": {"id": "id", "target_iam_id": "target_iam_id"}, "method": "method", "api_key": "api_key"}, "compliance_profile": {"id": "id", "instance_id": "instance_id", "instance_location": "instance_location", "attachment_id": "attachment_id", "profile_name": "profile_name"}, "locator_id": "locator_id", "type": "terraform_template", "input": [{"name": "name", "type": "array", "value": "anyValue", "required": true}], "output": [{"name": "name", "description": "description", "value": "anyValue"}], "setting": [{"name": "name", "value": "value"}]}}'
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
        response = _service.install_config(
            project_id,
            id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202

    def test_install_config_all_params_with_retries(self):
        # Enable retries and run test_install_config_all_params.
        _service.enable_retries()
        self.test_install_config_all_params()

        # Disable retries and run test_install_config_all_params.
        _service.disable_retries()
        self.test_install_config_all_params()

    @responses.activate
    def test_install_config_value_error(self):
        """
        test_install_config_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/projects/testString/configs/testString/install')
        mock_response = '{"id": "id", "project_id": "project_id", "version": 7, "is_draft": true, "needs_attention_state": ["anyValue"], "state": "state", "pipeline_state": "pipeline_state", "update_available": true, "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "last_approved": {"is_forced": false, "comment": "comment", "timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id"}, "last_save": "2019-01-01T12:00:00.000Z", "job_summary": {"plan_summary": {"anyKey": "anyValue"}, "apply_summary": {"anyKey": "anyValue"}, "destroy_summary": {"anyKey": "anyValue"}, "message_summary": {"anyKey": "anyValue"}, "plan_messages": {"anyKey": "anyValue"}, "apply_messages": {"anyKey": "anyValue"}, "destroy_messages": {"anyKey": "anyValue"}}, "cra_logs": {"cra_version": "cra_version", "schema_version": "schema_version", "status": "status", "summary": {"anyKey": "anyValue"}, "timestamp": "2019-01-01T12:00:00.000Z"}, "cost_estimate": {"version": "version", "currency": "currency", "totalHourlyCost": "total_hourly_cost", "totalMonthlyCost": "total_monthly_cost", "pastTotalHourlyCost": "past_total_hourly_cost", "pastTotalMonthlyCost": "past_total_monthly_cost", "diffTotalHourlyCost": "diff_total_hourly_cost", "diffTotalMonthlyCost": "diff_total_monthly_cost", "timeGenerated": "2019-01-01T12:00:00.000Z", "user_id": "user_id"}, "last_deployment_job_summary": {"plan_summary": {"anyKey": "anyValue"}, "apply_summary": {"anyKey": "anyValue"}, "destroy_summary": {"anyKey": "anyValue"}, "message_summary": {"anyKey": "anyValue"}, "plan_messages": {"anyKey": "anyValue"}, "apply_messages": {"anyKey": "anyValue"}, "destroy_messages": {"anyKey": "anyValue"}}, "active_draft": {"version": 7, "state": "state", "pipeline_state": "pipeline_state", "href": "href"}, "definition": {"name": "name", "labels": ["labels"], "description": "description", "authorizations": {"trusted_profile": {"id": "id", "target_iam_id": "target_iam_id"}, "method": "method", "api_key": "api_key"}, "compliance_profile": {"id": "id", "instance_id": "instance_id", "instance_location": "instance_location", "attachment_id": "attachment_id", "profile_name": "profile_name"}, "locator_id": "locator_id", "type": "terraform_template", "input": [{"name": "name", "type": "array", "value": "anyValue", "required": true}], "output": [{"name": "name", "description": "description", "value": "anyValue"}], "setting": [{"name": "name", "value": "value"}]}}'
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
                _service.install_config(**req_copy)

    def test_install_config_value_error_with_retries(self):
        # Enable retries and run test_install_config_value_error.
        _service.enable_retries()
        self.test_install_config_value_error()

        # Disable retries and run test_install_config_value_error.
        _service.disable_retries()
        self.test_install_config_value_error()


class TestUninstallConfig:
    """
    Test Class for uninstall_config
    """

    @responses.activate
    def test_uninstall_config_all_params(self):
        """
        uninstall_config()
        """
        # Set up mock
        url = preprocess_url('/v1/projects/testString/configs/testString/uninstall')
        responses.add(
            responses.POST,
            url,
            status=204,
        )

        # Set up parameter values
        project_id = 'testString'
        id = 'testString'

        # Invoke method
        response = _service.uninstall_config(
            project_id,
            id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_uninstall_config_all_params_with_retries(self):
        # Enable retries and run test_uninstall_config_all_params.
        _service.enable_retries()
        self.test_uninstall_config_all_params()

        # Disable retries and run test_uninstall_config_all_params.
        _service.disable_retries()
        self.test_uninstall_config_all_params()

    @responses.activate
    def test_uninstall_config_value_error(self):
        """
        test_uninstall_config_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/projects/testString/configs/testString/uninstall')
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
                _service.uninstall_config(**req_copy)

    def test_uninstall_config_value_error_with_retries(self):
        # Enable retries and run test_uninstall_config_value_error.
        _service.enable_retries()
        self.test_uninstall_config_value_error()

        # Disable retries and run test_uninstall_config_value_error.
        _service.disable_retries()
        self.test_uninstall_config_value_error()


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


class TestListConfigDrafts:
    """
    Test Class for list_config_drafts
    """

    @responses.activate
    def test_list_config_drafts_all_params(self):
        """
        list_config_drafts()
        """
        # Set up mock
        url = preprocess_url('/v1/projects/testString/configs/testString/drafts')
        mock_response = (
            '{"drafts": [{"version": 7, "state": "state", "pipeline_state": "pipeline_state", "href": "href"}]}'
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = 'testString'
        config_id = 'testString'

        # Invoke method
        response = _service.list_config_drafts(
            project_id,
            config_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_config_drafts_all_params_with_retries(self):
        # Enable retries and run test_list_config_drafts_all_params.
        _service.enable_retries()
        self.test_list_config_drafts_all_params()

        # Disable retries and run test_list_config_drafts_all_params.
        _service.disable_retries()
        self.test_list_config_drafts_all_params()

    @responses.activate
    def test_list_config_drafts_value_error(self):
        """
        test_list_config_drafts_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/projects/testString/configs/testString/drafts')
        mock_response = (
            '{"drafts": [{"version": 7, "state": "state", "pipeline_state": "pipeline_state", "href": "href"}]}'
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = 'testString'
        config_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "config_id": config_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_config_drafts(**req_copy)

    def test_list_config_drafts_value_error_with_retries(self):
        # Enable retries and run test_list_config_drafts_value_error.
        _service.enable_retries()
        self.test_list_config_drafts_value_error()

        # Disable retries and run test_list_config_drafts_value_error.
        _service.disable_retries()
        self.test_list_config_drafts_value_error()


class TestGetConfigDraft:
    """
    Test Class for get_config_draft
    """

    @responses.activate
    def test_get_config_draft_all_params(self):
        """
        get_config_draft()
        """
        # Set up mock
        url = preprocess_url('/v1/projects/testString/configs/testString/drafts/38')
        mock_response = '{"id": "id", "project_id": "project_id", "version": 7, "is_draft": true, "needs_attention_state": ["anyValue"], "state": "state", "pipeline_state": "pipeline_state", "update_available": true, "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "last_approved": {"is_forced": false, "comment": "comment", "timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id"}, "last_save": "2019-01-01T12:00:00.000Z", "job_summary": {"plan_summary": {"anyKey": "anyValue"}, "apply_summary": {"anyKey": "anyValue"}, "destroy_summary": {"anyKey": "anyValue"}, "message_summary": {"anyKey": "anyValue"}, "plan_messages": {"anyKey": "anyValue"}, "apply_messages": {"anyKey": "anyValue"}, "destroy_messages": {"anyKey": "anyValue"}}, "cra_logs": {"cra_version": "cra_version", "schema_version": "schema_version", "status": "status", "summary": {"anyKey": "anyValue"}, "timestamp": "2019-01-01T12:00:00.000Z"}, "cost_estimate": {"version": "version", "currency": "currency", "totalHourlyCost": "total_hourly_cost", "totalMonthlyCost": "total_monthly_cost", "pastTotalHourlyCost": "past_total_hourly_cost", "pastTotalMonthlyCost": "past_total_monthly_cost", "diffTotalHourlyCost": "diff_total_hourly_cost", "diffTotalMonthlyCost": "diff_total_monthly_cost", "timeGenerated": "2019-01-01T12:00:00.000Z", "user_id": "user_id"}, "last_deployment_job_summary": {"plan_summary": {"anyKey": "anyValue"}, "apply_summary": {"anyKey": "anyValue"}, "destroy_summary": {"anyKey": "anyValue"}, "message_summary": {"anyKey": "anyValue"}, "plan_messages": {"anyKey": "anyValue"}, "apply_messages": {"anyKey": "anyValue"}, "destroy_messages": {"anyKey": "anyValue"}}, "definition": {"name": "name", "labels": ["labels"], "description": "description", "authorizations": {"trusted_profile": {"id": "id", "target_iam_id": "target_iam_id"}, "method": "method", "api_key": "api_key"}, "compliance_profile": {"id": "id", "instance_id": "instance_id", "instance_location": "instance_location", "attachment_id": "attachment_id", "profile_name": "profile_name"}, "locator_id": "locator_id", "type": "terraform_template", "input": [{"name": "name", "type": "array", "value": "anyValue", "required": true}], "output": [{"name": "name", "description": "description", "value": "anyValue"}], "setting": [{"name": "name", "value": "value"}]}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = 'testString'
        config_id = 'testString'
        version = 38

        # Invoke method
        response = _service.get_config_draft(
            project_id,
            config_id,
            version,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_config_draft_all_params_with_retries(self):
        # Enable retries and run test_get_config_draft_all_params.
        _service.enable_retries()
        self.test_get_config_draft_all_params()

        # Disable retries and run test_get_config_draft_all_params.
        _service.disable_retries()
        self.test_get_config_draft_all_params()

    @responses.activate
    def test_get_config_draft_value_error(self):
        """
        test_get_config_draft_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/projects/testString/configs/testString/drafts/38')
        mock_response = '{"id": "id", "project_id": "project_id", "version": 7, "is_draft": true, "needs_attention_state": ["anyValue"], "state": "state", "pipeline_state": "pipeline_state", "update_available": true, "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "last_approved": {"is_forced": false, "comment": "comment", "timestamp": "2019-01-01T12:00:00.000Z", "user_id": "user_id"}, "last_save": "2019-01-01T12:00:00.000Z", "job_summary": {"plan_summary": {"anyKey": "anyValue"}, "apply_summary": {"anyKey": "anyValue"}, "destroy_summary": {"anyKey": "anyValue"}, "message_summary": {"anyKey": "anyValue"}, "plan_messages": {"anyKey": "anyValue"}, "apply_messages": {"anyKey": "anyValue"}, "destroy_messages": {"anyKey": "anyValue"}}, "cra_logs": {"cra_version": "cra_version", "schema_version": "schema_version", "status": "status", "summary": {"anyKey": "anyValue"}, "timestamp": "2019-01-01T12:00:00.000Z"}, "cost_estimate": {"version": "version", "currency": "currency", "totalHourlyCost": "total_hourly_cost", "totalMonthlyCost": "total_monthly_cost", "pastTotalHourlyCost": "past_total_hourly_cost", "pastTotalMonthlyCost": "past_total_monthly_cost", "diffTotalHourlyCost": "diff_total_hourly_cost", "diffTotalMonthlyCost": "diff_total_monthly_cost", "timeGenerated": "2019-01-01T12:00:00.000Z", "user_id": "user_id"}, "last_deployment_job_summary": {"plan_summary": {"anyKey": "anyValue"}, "apply_summary": {"anyKey": "anyValue"}, "destroy_summary": {"anyKey": "anyValue"}, "message_summary": {"anyKey": "anyValue"}, "plan_messages": {"anyKey": "anyValue"}, "apply_messages": {"anyKey": "anyValue"}, "destroy_messages": {"anyKey": "anyValue"}}, "definition": {"name": "name", "labels": ["labels"], "description": "description", "authorizations": {"trusted_profile": {"id": "id", "target_iam_id": "target_iam_id"}, "method": "method", "api_key": "api_key"}, "compliance_profile": {"id": "id", "instance_id": "instance_id", "instance_location": "instance_location", "attachment_id": "attachment_id", "profile_name": "profile_name"}, "locator_id": "locator_id", "type": "terraform_template", "input": [{"name": "name", "type": "array", "value": "anyValue", "required": true}], "output": [{"name": "name", "description": "description", "value": "anyValue"}], "setting": [{"name": "name", "value": "value"}]}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        project_id = 'testString'
        config_id = 'testString'
        version = 38

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "config_id": config_id,
            "version": version,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_config_draft(**req_copy)

    def test_get_config_draft_value_error_with_retries(self):
        # Enable retries and run test_get_config_draft_value_error.
        _service.enable_retries()
        self.test_get_config_draft_value_error()

        # Disable retries and run test_get_config_draft_value_error.
        _service.disable_retries()
        self.test_get_config_draft_value_error()


# endregion
##############################################################################
# End of Service: Configurations
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region


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
        input_variable_model_json['name'] = 'testString'
        input_variable_model_json['type'] = 'array'
        input_variable_model_json['value'] = 'testString'
        input_variable_model_json['required'] = True

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
        pagination_link_model_json['start'] = 'testString'

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

        project_definition_response_model = {}  # ProjectDefinitionResponse
        project_definition_response_model['name'] = 'testString'
        project_definition_response_model['description'] = 'testString'
        project_definition_response_model['destroy_on_delete'] = True

        project_config_metadata_last_approved_model = {}  # ProjectConfigMetadataLastApproved
        project_config_metadata_last_approved_model['is_forced'] = True
        project_config_metadata_last_approved_model['comment'] = 'testString'
        project_config_metadata_last_approved_model['timestamp'] = '2019-01-01T12:00:00Z'
        project_config_metadata_last_approved_model['user_id'] = 'testString'

        project_config_draft_summary_model = {}  # ProjectConfigDraftSummary
        project_config_draft_summary_model['version'] = 38
        project_config_draft_summary_model['state'] = 'testString'
        project_config_draft_summary_model['pipeline_state'] = 'testString'
        project_config_draft_summary_model['href'] = 'testString'

        project_config_auth_trusted_profile_model = {}  # ProjectConfigAuthTrustedProfile
        project_config_auth_trusted_profile_model['id'] = 'testString'
        project_config_auth_trusted_profile_model['target_iam_id'] = 'testString'

        project_config_auth_model = {}  # ProjectConfigAuth
        project_config_auth_model['trusted_profile'] = project_config_auth_trusted_profile_model
        project_config_auth_model['method'] = 'testString'
        project_config_auth_model['api_key'] = 'testString'

        project_config_compliance_profile_model = {}  # ProjectConfigComplianceProfile
        project_config_compliance_profile_model['id'] = 'testString'
        project_config_compliance_profile_model['instance_id'] = 'testString'
        project_config_compliance_profile_model['instance_location'] = 'testString'
        project_config_compliance_profile_model['attachment_id'] = 'testString'
        project_config_compliance_profile_model['profile_name'] = 'testString'

        input_variable_model = {}  # InputVariable
        input_variable_model['name'] = 'testString'
        input_variable_model['type'] = 'array'
        input_variable_model['value'] = 'testString'
        input_variable_model['required'] = True

        output_value_model = {}  # OutputValue
        output_value_model['name'] = 'testString'
        output_value_model['description'] = 'testString'
        output_value_model['value'] = 'testString'

        project_config_setting_collection_model = {}  # ProjectConfigSettingCollection
        project_config_setting_collection_model['name'] = 'testString'
        project_config_setting_collection_model['value'] = 'testString'

        project_config_definition_model = {}  # ProjectConfigDefinition
        project_config_definition_model['name'] = 'testString'
        project_config_definition_model['labels'] = []
        project_config_definition_model['description'] = 'testString'
        project_config_definition_model['authorizations'] = project_config_auth_model
        project_config_definition_model['compliance_profile'] = project_config_compliance_profile_model
        project_config_definition_model['locator_id'] = 'testString'
        project_config_definition_model['type'] = 'terraform_template'
        project_config_definition_model['input'] = [input_variable_model]
        project_config_definition_model['output'] = [output_value_model]
        project_config_definition_model['setting'] = [project_config_setting_collection_model]

        project_config_collection_member_model = {}  # ProjectConfigCollectionMember
        project_config_collection_member_model['id'] = 'testString'
        project_config_collection_member_model['project_id'] = 'testString'
        project_config_collection_member_model['version'] = 38
        project_config_collection_member_model['is_draft'] = True
        project_config_collection_member_model['needs_attention_state'] = []
        project_config_collection_member_model['state'] = 'testString'
        project_config_collection_member_model['pipeline_state'] = 'testString'
        project_config_collection_member_model['update_available'] = True
        project_config_collection_member_model['created_at'] = '2019-01-01T12:00:00Z'
        project_config_collection_member_model['updated_at'] = '2019-01-01T12:00:00Z'
        project_config_collection_member_model['last_approved'] = project_config_metadata_last_approved_model
        project_config_collection_member_model['last_save'] = '2019-01-01T12:00:00Z'
        project_config_collection_member_model['active_draft'] = project_config_draft_summary_model
        project_config_collection_member_model['definition'] = project_config_definition_model
        project_config_collection_member_model['href'] = 'testString'

        # Construct a json representation of a Project model
        project_model_json = {}
        project_model_json[
            'crn'
        ] = 'crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::'
        project_model_json['created_at'] = '2019-01-01T12:00:00Z'
        project_model_json['cumulative_needs_attention_view'] = [cumulative_needs_attention_model]
        project_model_json['cumulative_needs_attention_view_error'] = True
        project_model_json['id'] = 'testString'
        project_model_json['location'] = 'testString'
        project_model_json['resource_group'] = 'testString'
        project_model_json['state'] = 'testString'
        project_model_json['event_notifications_crn'] = 'testString'
        project_model_json['definition'] = project_definition_response_model
        project_model_json['configs'] = [project_config_collection_member_model]

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
        pagination_link_model['start'] = 'testString'

        cumulative_needs_attention_model = {}  # CumulativeNeedsAttention
        cumulative_needs_attention_model['event'] = 'testString'
        cumulative_needs_attention_model['event_id'] = 'testString'
        cumulative_needs_attention_model['config_id'] = 'testString'
        cumulative_needs_attention_model['config_version'] = 38

        project_definition_response_model = {}  # ProjectDefinitionResponse
        project_definition_response_model['name'] = 'testString'
        project_definition_response_model['description'] = 'testString'
        project_definition_response_model['destroy_on_delete'] = True

        project_collection_member_with_metadata_model = {}  # ProjectCollectionMemberWithMetadata
        project_collection_member_with_metadata_model[
            'crn'
        ] = 'crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::'
        project_collection_member_with_metadata_model['created_at'] = '2019-01-01T12:00:00Z'
        project_collection_member_with_metadata_model['cumulative_needs_attention_view'] = [
            cumulative_needs_attention_model
        ]
        project_collection_member_with_metadata_model['cumulative_needs_attention_view_error'] = True
        project_collection_member_with_metadata_model['id'] = 'testString'
        project_collection_member_with_metadata_model['location'] = 'testString'
        project_collection_member_with_metadata_model['resource_group'] = 'testString'
        project_collection_member_with_metadata_model['state'] = 'testString'
        project_collection_member_with_metadata_model['event_notifications_crn'] = 'testString'
        project_collection_member_with_metadata_model['definition'] = project_definition_response_model

        # Construct a json representation of a ProjectCollection model
        project_collection_model_json = {}
        project_collection_model_json['limit'] = 10
        project_collection_model_json['total_count'] = 0
        project_collection_model_json['first'] = pagination_link_model
        project_collection_model_json['last'] = pagination_link_model
        project_collection_model_json['previous'] = pagination_link_model
        project_collection_model_json['next'] = pagination_link_model
        project_collection_model_json['projects'] = [project_collection_member_with_metadata_model]

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


class TestModel_ProjectCollectionMemberWithMetadata:
    """
    Test Class for ProjectCollectionMemberWithMetadata
    """

    def test_project_collection_member_with_metadata_serialization(self):
        """
        Test serialization/deserialization for ProjectCollectionMemberWithMetadata
        """

        # Construct dict forms of any model objects needed in order to build this model.

        cumulative_needs_attention_model = {}  # CumulativeNeedsAttention
        cumulative_needs_attention_model['event'] = 'testString'
        cumulative_needs_attention_model['event_id'] = 'testString'
        cumulative_needs_attention_model['config_id'] = 'testString'
        cumulative_needs_attention_model['config_version'] = 38

        project_definition_response_model = {}  # ProjectDefinitionResponse
        project_definition_response_model['name'] = 'testString'
        project_definition_response_model['description'] = 'testString'
        project_definition_response_model['destroy_on_delete'] = True

        # Construct a json representation of a ProjectCollectionMemberWithMetadata model
        project_collection_member_with_metadata_model_json = {}
        project_collection_member_with_metadata_model_json[
            'crn'
        ] = 'crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::'
        project_collection_member_with_metadata_model_json['created_at'] = '2019-01-01T12:00:00Z'
        project_collection_member_with_metadata_model_json['cumulative_needs_attention_view'] = [
            cumulative_needs_attention_model
        ]
        project_collection_member_with_metadata_model_json['cumulative_needs_attention_view_error'] = True
        project_collection_member_with_metadata_model_json['id'] = 'testString'
        project_collection_member_with_metadata_model_json['location'] = 'testString'
        project_collection_member_with_metadata_model_json['resource_group'] = 'testString'
        project_collection_member_with_metadata_model_json['state'] = 'testString'
        project_collection_member_with_metadata_model_json['event_notifications_crn'] = 'testString'
        project_collection_member_with_metadata_model_json['definition'] = project_definition_response_model

        # Construct a model instance of ProjectCollectionMemberWithMetadata by calling from_dict on the json representation
        project_collection_member_with_metadata_model = ProjectCollectionMemberWithMetadata.from_dict(
            project_collection_member_with_metadata_model_json
        )
        assert project_collection_member_with_metadata_model != False

        # Construct a model instance of ProjectCollectionMemberWithMetadata by calling from_dict on the json representation
        project_collection_member_with_metadata_model_dict = ProjectCollectionMemberWithMetadata.from_dict(
            project_collection_member_with_metadata_model_json
        ).__dict__
        project_collection_member_with_metadata_model2 = ProjectCollectionMemberWithMetadata(
            **project_collection_member_with_metadata_model_dict
        )

        # Verify the model instances are equivalent
        assert project_collection_member_with_metadata_model == project_collection_member_with_metadata_model2

        # Convert model instance back to dict and verify no loss of data
        project_collection_member_with_metadata_model_json2 = project_collection_member_with_metadata_model.to_dict()
        assert project_collection_member_with_metadata_model_json2 == project_collection_member_with_metadata_model_json


class TestModel_ProjectConfigAuth:
    """
    Test Class for ProjectConfigAuth
    """

    def test_project_config_auth_serialization(self):
        """
        Test serialization/deserialization for ProjectConfigAuth
        """

        # Construct dict forms of any model objects needed in order to build this model.

        project_config_auth_trusted_profile_model = {}  # ProjectConfigAuthTrustedProfile
        project_config_auth_trusted_profile_model['id'] = 'testString'
        project_config_auth_trusted_profile_model['target_iam_id'] = 'testString'

        # Construct a json representation of a ProjectConfigAuth model
        project_config_auth_model_json = {}
        project_config_auth_model_json['trusted_profile'] = project_config_auth_trusted_profile_model
        project_config_auth_model_json['method'] = 'testString'
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


class TestModel_ProjectConfigAuthTrustedProfile:
    """
    Test Class for ProjectConfigAuthTrustedProfile
    """

    def test_project_config_auth_trusted_profile_serialization(self):
        """
        Test serialization/deserialization for ProjectConfigAuthTrustedProfile
        """

        # Construct a json representation of a ProjectConfigAuthTrustedProfile model
        project_config_auth_trusted_profile_model_json = {}
        project_config_auth_trusted_profile_model_json['id'] = 'testString'
        project_config_auth_trusted_profile_model_json['target_iam_id'] = 'testString'

        # Construct a model instance of ProjectConfigAuthTrustedProfile by calling from_dict on the json representation
        project_config_auth_trusted_profile_model = ProjectConfigAuthTrustedProfile.from_dict(
            project_config_auth_trusted_profile_model_json
        )
        assert project_config_auth_trusted_profile_model != False

        # Construct a model instance of ProjectConfigAuthTrustedProfile by calling from_dict on the json representation
        project_config_auth_trusted_profile_model_dict = ProjectConfigAuthTrustedProfile.from_dict(
            project_config_auth_trusted_profile_model_json
        ).__dict__
        project_config_auth_trusted_profile_model2 = ProjectConfigAuthTrustedProfile(
            **project_config_auth_trusted_profile_model_dict
        )

        # Verify the model instances are equivalent
        assert project_config_auth_trusted_profile_model == project_config_auth_trusted_profile_model2

        # Convert model instance back to dict and verify no loss of data
        project_config_auth_trusted_profile_model_json2 = project_config_auth_trusted_profile_model.to_dict()
        assert project_config_auth_trusted_profile_model_json2 == project_config_auth_trusted_profile_model_json


class TestModel_ProjectConfigCollection:
    """
    Test Class for ProjectConfigCollection
    """

    def test_project_config_collection_serialization(self):
        """
        Test serialization/deserialization for ProjectConfigCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        project_config_metadata_last_approved_model = {}  # ProjectConfigMetadataLastApproved
        project_config_metadata_last_approved_model['is_forced'] = True
        project_config_metadata_last_approved_model['comment'] = 'testString'
        project_config_metadata_last_approved_model['timestamp'] = '2019-01-01T12:00:00Z'
        project_config_metadata_last_approved_model['user_id'] = 'testString'

        project_config_draft_summary_model = {}  # ProjectConfigDraftSummary
        project_config_draft_summary_model['version'] = 38
        project_config_draft_summary_model['state'] = 'testString'
        project_config_draft_summary_model['pipeline_state'] = 'testString'
        project_config_draft_summary_model['href'] = 'testString'

        project_config_auth_trusted_profile_model = {}  # ProjectConfigAuthTrustedProfile
        project_config_auth_trusted_profile_model['id'] = 'testString'
        project_config_auth_trusted_profile_model['target_iam_id'] = 'testString'

        project_config_auth_model = {}  # ProjectConfigAuth
        project_config_auth_model['trusted_profile'] = project_config_auth_trusted_profile_model
        project_config_auth_model['method'] = 'testString'
        project_config_auth_model['api_key'] = 'testString'

        project_config_compliance_profile_model = {}  # ProjectConfigComplianceProfile
        project_config_compliance_profile_model['id'] = 'testString'
        project_config_compliance_profile_model['instance_id'] = 'testString'
        project_config_compliance_profile_model['instance_location'] = 'testString'
        project_config_compliance_profile_model['attachment_id'] = 'testString'
        project_config_compliance_profile_model['profile_name'] = 'testString'

        input_variable_model = {}  # InputVariable
        input_variable_model['name'] = 'testString'
        input_variable_model['type'] = 'array'
        input_variable_model['value'] = 'testString'
        input_variable_model['required'] = True

        output_value_model = {}  # OutputValue
        output_value_model['name'] = 'testString'
        output_value_model['description'] = 'testString'
        output_value_model['value'] = 'testString'

        project_config_setting_collection_model = {}  # ProjectConfigSettingCollection
        project_config_setting_collection_model['name'] = 'testString'
        project_config_setting_collection_model['value'] = 'testString'

        project_config_definition_model = {}  # ProjectConfigDefinition
        project_config_definition_model['name'] = 'testString'
        project_config_definition_model['labels'] = []
        project_config_definition_model['description'] = 'testString'
        project_config_definition_model['authorizations'] = project_config_auth_model
        project_config_definition_model['compliance_profile'] = project_config_compliance_profile_model
        project_config_definition_model['locator_id'] = 'testString'
        project_config_definition_model['type'] = 'terraform_template'
        project_config_definition_model['input'] = [input_variable_model]
        project_config_definition_model['output'] = [output_value_model]
        project_config_definition_model['setting'] = [project_config_setting_collection_model]

        project_config_collection_member_model = {}  # ProjectConfigCollectionMember
        project_config_collection_member_model['id'] = 'testString'
        project_config_collection_member_model['project_id'] = 'testString'
        project_config_collection_member_model['version'] = 38
        project_config_collection_member_model['is_draft'] = True
        project_config_collection_member_model['needs_attention_state'] = []
        project_config_collection_member_model['state'] = 'testString'
        project_config_collection_member_model['pipeline_state'] = 'testString'
        project_config_collection_member_model['update_available'] = True
        project_config_collection_member_model['created_at'] = '2019-01-01T12:00:00Z'
        project_config_collection_member_model['updated_at'] = '2019-01-01T12:00:00Z'
        project_config_collection_member_model['last_approved'] = project_config_metadata_last_approved_model
        project_config_collection_member_model['last_save'] = '2019-01-01T12:00:00Z'
        project_config_collection_member_model['active_draft'] = project_config_draft_summary_model
        project_config_collection_member_model['definition'] = project_config_definition_model
        project_config_collection_member_model['href'] = 'testString'

        # Construct a json representation of a ProjectConfigCollection model
        project_config_collection_model_json = {}
        project_config_collection_model_json['configs'] = [project_config_collection_member_model]

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


class TestModel_ProjectConfigCollectionMember:
    """
    Test Class for ProjectConfigCollectionMember
    """

    def test_project_config_collection_member_serialization(self):
        """
        Test serialization/deserialization for ProjectConfigCollectionMember
        """

        # Construct dict forms of any model objects needed in order to build this model.

        project_config_metadata_last_approved_model = {}  # ProjectConfigMetadataLastApproved
        project_config_metadata_last_approved_model['is_forced'] = True
        project_config_metadata_last_approved_model['comment'] = 'testString'
        project_config_metadata_last_approved_model['timestamp'] = '2019-01-01T12:00:00Z'
        project_config_metadata_last_approved_model['user_id'] = 'testString'

        project_config_draft_summary_model = {}  # ProjectConfigDraftSummary
        project_config_draft_summary_model['version'] = 38
        project_config_draft_summary_model['state'] = 'testString'
        project_config_draft_summary_model['pipeline_state'] = 'testString'
        project_config_draft_summary_model['href'] = 'testString'

        project_config_auth_trusted_profile_model = {}  # ProjectConfigAuthTrustedProfile
        project_config_auth_trusted_profile_model['id'] = 'testString'
        project_config_auth_trusted_profile_model['target_iam_id'] = 'testString'

        project_config_auth_model = {}  # ProjectConfigAuth
        project_config_auth_model['trusted_profile'] = project_config_auth_trusted_profile_model
        project_config_auth_model['method'] = 'testString'
        project_config_auth_model['api_key'] = 'testString'

        project_config_compliance_profile_model = {}  # ProjectConfigComplianceProfile
        project_config_compliance_profile_model['id'] = 'testString'
        project_config_compliance_profile_model['instance_id'] = 'testString'
        project_config_compliance_profile_model['instance_location'] = 'testString'
        project_config_compliance_profile_model['attachment_id'] = 'testString'
        project_config_compliance_profile_model['profile_name'] = 'testString'

        input_variable_model = {}  # InputVariable
        input_variable_model['name'] = 'testString'
        input_variable_model['type'] = 'array'
        input_variable_model['value'] = 'testString'
        input_variable_model['required'] = True

        output_value_model = {}  # OutputValue
        output_value_model['name'] = 'testString'
        output_value_model['description'] = 'testString'
        output_value_model['value'] = 'testString'

        project_config_setting_collection_model = {}  # ProjectConfigSettingCollection
        project_config_setting_collection_model['name'] = 'testString'
        project_config_setting_collection_model['value'] = 'testString'

        project_config_definition_model = {}  # ProjectConfigDefinition
        project_config_definition_model['name'] = 'testString'
        project_config_definition_model['labels'] = []
        project_config_definition_model['description'] = 'testString'
        project_config_definition_model['authorizations'] = project_config_auth_model
        project_config_definition_model['compliance_profile'] = project_config_compliance_profile_model
        project_config_definition_model['locator_id'] = 'testString'
        project_config_definition_model['type'] = 'terraform_template'
        project_config_definition_model['input'] = [input_variable_model]
        project_config_definition_model['output'] = [output_value_model]
        project_config_definition_model['setting'] = [project_config_setting_collection_model]

        # Construct a json representation of a ProjectConfigCollectionMember model
        project_config_collection_member_model_json = {}
        project_config_collection_member_model_json['id'] = 'testString'
        project_config_collection_member_model_json['project_id'] = 'testString'
        project_config_collection_member_model_json['version'] = 38
        project_config_collection_member_model_json['is_draft'] = True
        project_config_collection_member_model_json['needs_attention_state'] = []
        project_config_collection_member_model_json['state'] = 'testString'
        project_config_collection_member_model_json['pipeline_state'] = 'testString'
        project_config_collection_member_model_json['update_available'] = True
        project_config_collection_member_model_json['created_at'] = '2019-01-01T12:00:00Z'
        project_config_collection_member_model_json['updated_at'] = '2019-01-01T12:00:00Z'
        project_config_collection_member_model_json['last_approved'] = project_config_metadata_last_approved_model
        project_config_collection_member_model_json['last_save'] = '2019-01-01T12:00:00Z'
        project_config_collection_member_model_json['active_draft'] = project_config_draft_summary_model
        project_config_collection_member_model_json['definition'] = project_config_definition_model
        project_config_collection_member_model_json['href'] = 'testString'

        # Construct a model instance of ProjectConfigCollectionMember by calling from_dict on the json representation
        project_config_collection_member_model = ProjectConfigCollectionMember.from_dict(
            project_config_collection_member_model_json
        )
        assert project_config_collection_member_model != False

        # Construct a model instance of ProjectConfigCollectionMember by calling from_dict on the json representation
        project_config_collection_member_model_dict = ProjectConfigCollectionMember.from_dict(
            project_config_collection_member_model_json
        ).__dict__
        project_config_collection_member_model2 = ProjectConfigCollectionMember(
            **project_config_collection_member_model_dict
        )

        # Verify the model instances are equivalent
        assert project_config_collection_member_model == project_config_collection_member_model2

        # Convert model instance back to dict and verify no loss of data
        project_config_collection_member_model_json2 = project_config_collection_member_model.to_dict()
        assert project_config_collection_member_model_json2 == project_config_collection_member_model_json


class TestModel_ProjectConfigComplianceProfile:
    """
    Test Class for ProjectConfigComplianceProfile
    """

    def test_project_config_compliance_profile_serialization(self):
        """
        Test serialization/deserialization for ProjectConfigComplianceProfile
        """

        # Construct a json representation of a ProjectConfigComplianceProfile model
        project_config_compliance_profile_model_json = {}
        project_config_compliance_profile_model_json['id'] = 'testString'
        project_config_compliance_profile_model_json['instance_id'] = 'testString'
        project_config_compliance_profile_model_json['instance_location'] = 'testString'
        project_config_compliance_profile_model_json['attachment_id'] = 'testString'
        project_config_compliance_profile_model_json['profile_name'] = 'testString'

        # Construct a model instance of ProjectConfigComplianceProfile by calling from_dict on the json representation
        project_config_compliance_profile_model = ProjectConfigComplianceProfile.from_dict(
            project_config_compliance_profile_model_json
        )
        assert project_config_compliance_profile_model != False

        # Construct a model instance of ProjectConfigComplianceProfile by calling from_dict on the json representation
        project_config_compliance_profile_model_dict = ProjectConfigComplianceProfile.from_dict(
            project_config_compliance_profile_model_json
        ).__dict__
        project_config_compliance_profile_model2 = ProjectConfigComplianceProfile(
            **project_config_compliance_profile_model_dict
        )

        # Verify the model instances are equivalent
        assert project_config_compliance_profile_model == project_config_compliance_profile_model2

        # Convert model instance back to dict and verify no loss of data
        project_config_compliance_profile_model_json2 = project_config_compliance_profile_model.to_dict()
        assert project_config_compliance_profile_model_json2 == project_config_compliance_profile_model_json


class TestModel_ProjectConfigDefinition:
    """
    Test Class for ProjectConfigDefinition
    """

    def test_project_config_definition_serialization(self):
        """
        Test serialization/deserialization for ProjectConfigDefinition
        """

        # Construct dict forms of any model objects needed in order to build this model.

        project_config_auth_trusted_profile_model = {}  # ProjectConfigAuthTrustedProfile
        project_config_auth_trusted_profile_model['id'] = 'testString'
        project_config_auth_trusted_profile_model['target_iam_id'] = 'testString'

        project_config_auth_model = {}  # ProjectConfigAuth
        project_config_auth_model['trusted_profile'] = project_config_auth_trusted_profile_model
        project_config_auth_model['method'] = 'testString'
        project_config_auth_model['api_key'] = 'testString'

        project_config_compliance_profile_model = {}  # ProjectConfigComplianceProfile
        project_config_compliance_profile_model['id'] = 'testString'
        project_config_compliance_profile_model['instance_id'] = 'testString'
        project_config_compliance_profile_model['instance_location'] = 'testString'
        project_config_compliance_profile_model['attachment_id'] = 'testString'
        project_config_compliance_profile_model['profile_name'] = 'testString'

        input_variable_model = {}  # InputVariable
        input_variable_model['name'] = 'testString'
        input_variable_model['type'] = 'array'
        input_variable_model['value'] = 'testString'
        input_variable_model['required'] = True

        output_value_model = {}  # OutputValue
        output_value_model['name'] = 'testString'
        output_value_model['description'] = 'testString'
        output_value_model['value'] = 'testString'

        project_config_setting_collection_model = {}  # ProjectConfigSettingCollection
        project_config_setting_collection_model['name'] = 'testString'
        project_config_setting_collection_model['value'] = 'testString'

        # Construct a json representation of a ProjectConfigDefinition model
        project_config_definition_model_json = {}
        project_config_definition_model_json['name'] = 'testString'
        project_config_definition_model_json['labels'] = []
        project_config_definition_model_json['description'] = 'testString'
        project_config_definition_model_json['authorizations'] = project_config_auth_model
        project_config_definition_model_json['compliance_profile'] = project_config_compliance_profile_model
        project_config_definition_model_json['locator_id'] = 'testString'
        project_config_definition_model_json['type'] = 'terraform_template'
        project_config_definition_model_json['input'] = [input_variable_model]
        project_config_definition_model_json['output'] = [output_value_model]
        project_config_definition_model_json['setting'] = [project_config_setting_collection_model]

        # Construct a model instance of ProjectConfigDefinition by calling from_dict on the json representation
        project_config_definition_model = ProjectConfigDefinition.from_dict(project_config_definition_model_json)
        assert project_config_definition_model != False

        # Construct a model instance of ProjectConfigDefinition by calling from_dict on the json representation
        project_config_definition_model_dict = ProjectConfigDefinition.from_dict(
            project_config_definition_model_json
        ).__dict__
        project_config_definition_model2 = ProjectConfigDefinition(**project_config_definition_model_dict)

        # Verify the model instances are equivalent
        assert project_config_definition_model == project_config_definition_model2

        # Convert model instance back to dict and verify no loss of data
        project_config_definition_model_json2 = project_config_definition_model.to_dict()
        assert project_config_definition_model_json2 == project_config_definition_model_json


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


class TestModel_ProjectConfigDraftResponse:
    """
    Test Class for ProjectConfigDraftResponse
    """

    def test_project_config_draft_response_serialization(self):
        """
        Test serialization/deserialization for ProjectConfigDraftResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        project_config_metadata_last_approved_model = {}  # ProjectConfigMetadataLastApproved
        project_config_metadata_last_approved_model['is_forced'] = True
        project_config_metadata_last_approved_model['comment'] = 'testString'
        project_config_metadata_last_approved_model['timestamp'] = '2019-01-01T12:00:00Z'
        project_config_metadata_last_approved_model['user_id'] = 'testString'

        project_config_metadata_job_summary_model = {}  # ProjectConfigMetadataJobSummary
        project_config_metadata_job_summary_model['plan_summary'] = {'anyKey': 'anyValue'}
        project_config_metadata_job_summary_model['apply_summary'] = {'anyKey': 'anyValue'}
        project_config_metadata_job_summary_model['destroy_summary'] = {'anyKey': 'anyValue'}
        project_config_metadata_job_summary_model['message_summary'] = {'anyKey': 'anyValue'}
        project_config_metadata_job_summary_model['plan_messages'] = {'anyKey': 'anyValue'}
        project_config_metadata_job_summary_model['apply_messages'] = {'anyKey': 'anyValue'}
        project_config_metadata_job_summary_model['destroy_messages'] = {'anyKey': 'anyValue'}

        project_config_metadata_cra_logs_model = {}  # ProjectConfigMetadataCraLogs
        project_config_metadata_cra_logs_model['cra_version'] = 'testString'
        project_config_metadata_cra_logs_model['schema_version'] = 'testString'
        project_config_metadata_cra_logs_model['status'] = 'testString'
        project_config_metadata_cra_logs_model['summary'] = {'anyKey': 'anyValue'}
        project_config_metadata_cra_logs_model['timestamp'] = '2019-01-01T12:00:00Z'

        project_config_metadata_cost_estimate_model = {}  # ProjectConfigMetadataCostEstimate
        project_config_metadata_cost_estimate_model['version'] = 'testString'
        project_config_metadata_cost_estimate_model['currency'] = 'testString'
        project_config_metadata_cost_estimate_model['totalHourlyCost'] = 'testString'
        project_config_metadata_cost_estimate_model['totalMonthlyCost'] = 'testString'
        project_config_metadata_cost_estimate_model['pastTotalHourlyCost'] = 'testString'
        project_config_metadata_cost_estimate_model['pastTotalMonthlyCost'] = 'testString'
        project_config_metadata_cost_estimate_model['diffTotalHourlyCost'] = 'testString'
        project_config_metadata_cost_estimate_model['diffTotalMonthlyCost'] = 'testString'
        project_config_metadata_cost_estimate_model['timeGenerated'] = '2019-01-01T12:00:00Z'
        project_config_metadata_cost_estimate_model['user_id'] = 'testString'

        project_config_auth_trusted_profile_model = {}  # ProjectConfigAuthTrustedProfile
        project_config_auth_trusted_profile_model['id'] = 'testString'
        project_config_auth_trusted_profile_model['target_iam_id'] = 'testString'

        project_config_auth_model = {}  # ProjectConfigAuth
        project_config_auth_model['trusted_profile'] = project_config_auth_trusted_profile_model
        project_config_auth_model['method'] = 'testString'
        project_config_auth_model['api_key'] = 'testString'

        project_config_compliance_profile_model = {}  # ProjectConfigComplianceProfile
        project_config_compliance_profile_model['id'] = 'testString'
        project_config_compliance_profile_model['instance_id'] = 'testString'
        project_config_compliance_profile_model['instance_location'] = 'testString'
        project_config_compliance_profile_model['attachment_id'] = 'testString'
        project_config_compliance_profile_model['profile_name'] = 'testString'

        input_variable_model = {}  # InputVariable
        input_variable_model['name'] = 'testString'
        input_variable_model['type'] = 'array'
        input_variable_model['value'] = 'testString'
        input_variable_model['required'] = True

        output_value_model = {}  # OutputValue
        output_value_model['name'] = 'testString'
        output_value_model['description'] = 'testString'
        output_value_model['value'] = 'testString'

        project_config_setting_collection_model = {}  # ProjectConfigSettingCollection
        project_config_setting_collection_model['name'] = 'testString'
        project_config_setting_collection_model['value'] = 'testString'

        project_config_definition_model = {}  # ProjectConfigDefinition
        project_config_definition_model['name'] = 'testString'
        project_config_definition_model['labels'] = []
        project_config_definition_model['description'] = 'testString'
        project_config_definition_model['authorizations'] = project_config_auth_model
        project_config_definition_model['compliance_profile'] = project_config_compliance_profile_model
        project_config_definition_model['locator_id'] = 'testString'
        project_config_definition_model['type'] = 'terraform_template'
        project_config_definition_model['input'] = [input_variable_model]
        project_config_definition_model['output'] = [output_value_model]
        project_config_definition_model['setting'] = [project_config_setting_collection_model]

        # Construct a json representation of a ProjectConfigDraftResponse model
        project_config_draft_response_model_json = {}
        project_config_draft_response_model_json['id'] = 'testString'
        project_config_draft_response_model_json['project_id'] = 'testString'
        project_config_draft_response_model_json['version'] = 38
        project_config_draft_response_model_json['is_draft'] = True
        project_config_draft_response_model_json['needs_attention_state'] = []
        project_config_draft_response_model_json['state'] = 'testString'
        project_config_draft_response_model_json['pipeline_state'] = 'testString'
        project_config_draft_response_model_json['update_available'] = True
        project_config_draft_response_model_json['created_at'] = '2019-01-01T12:00:00Z'
        project_config_draft_response_model_json['updated_at'] = '2019-01-01T12:00:00Z'
        project_config_draft_response_model_json['last_approved'] = project_config_metadata_last_approved_model
        project_config_draft_response_model_json['last_save'] = '2019-01-01T12:00:00Z'
        project_config_draft_response_model_json['job_summary'] = project_config_metadata_job_summary_model
        project_config_draft_response_model_json['cra_logs'] = project_config_metadata_cra_logs_model
        project_config_draft_response_model_json['cost_estimate'] = project_config_metadata_cost_estimate_model
        project_config_draft_response_model_json[
            'last_deployment_job_summary'
        ] = project_config_metadata_job_summary_model
        project_config_draft_response_model_json['definition'] = project_config_definition_model

        # Construct a model instance of ProjectConfigDraftResponse by calling from_dict on the json representation
        project_config_draft_response_model = ProjectConfigDraftResponse.from_dict(
            project_config_draft_response_model_json
        )
        assert project_config_draft_response_model != False

        # Construct a model instance of ProjectConfigDraftResponse by calling from_dict on the json representation
        project_config_draft_response_model_dict = ProjectConfigDraftResponse.from_dict(
            project_config_draft_response_model_json
        ).__dict__
        project_config_draft_response_model2 = ProjectConfigDraftResponse(**project_config_draft_response_model_dict)

        # Verify the model instances are equivalent
        assert project_config_draft_response_model == project_config_draft_response_model2

        # Convert model instance back to dict and verify no loss of data
        project_config_draft_response_model_json2 = project_config_draft_response_model.to_dict()
        assert project_config_draft_response_model_json2 == project_config_draft_response_model_json


class TestModel_ProjectConfigDraftSummary:
    """
    Test Class for ProjectConfigDraftSummary
    """

    def test_project_config_draft_summary_serialization(self):
        """
        Test serialization/deserialization for ProjectConfigDraftSummary
        """

        # Construct a json representation of a ProjectConfigDraftSummary model
        project_config_draft_summary_model_json = {}
        project_config_draft_summary_model_json['version'] = 38
        project_config_draft_summary_model_json['state'] = 'testString'
        project_config_draft_summary_model_json['pipeline_state'] = 'testString'
        project_config_draft_summary_model_json['href'] = 'testString'

        # Construct a model instance of ProjectConfigDraftSummary by calling from_dict on the json representation
        project_config_draft_summary_model = ProjectConfigDraftSummary.from_dict(
            project_config_draft_summary_model_json
        )
        assert project_config_draft_summary_model != False

        # Construct a model instance of ProjectConfigDraftSummary by calling from_dict on the json representation
        project_config_draft_summary_model_dict = ProjectConfigDraftSummary.from_dict(
            project_config_draft_summary_model_json
        ).__dict__
        project_config_draft_summary_model2 = ProjectConfigDraftSummary(**project_config_draft_summary_model_dict)

        # Verify the model instances are equivalent
        assert project_config_draft_summary_model == project_config_draft_summary_model2

        # Convert model instance back to dict and verify no loss of data
        project_config_draft_summary_model_json2 = project_config_draft_summary_model.to_dict()
        assert project_config_draft_summary_model_json2 == project_config_draft_summary_model_json


class TestModel_ProjectConfigDraftSummaryCollection:
    """
    Test Class for ProjectConfigDraftSummaryCollection
    """

    def test_project_config_draft_summary_collection_serialization(self):
        """
        Test serialization/deserialization for ProjectConfigDraftSummaryCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        project_config_draft_summary_model = {}  # ProjectConfigDraftSummary
        project_config_draft_summary_model['version'] = 38
        project_config_draft_summary_model['state'] = 'testString'
        project_config_draft_summary_model['pipeline_state'] = 'testString'
        project_config_draft_summary_model['href'] = 'testString'

        # Construct a json representation of a ProjectConfigDraftSummaryCollection model
        project_config_draft_summary_collection_model_json = {}
        project_config_draft_summary_collection_model_json['drafts'] = [project_config_draft_summary_model]

        # Construct a model instance of ProjectConfigDraftSummaryCollection by calling from_dict on the json representation
        project_config_draft_summary_collection_model = ProjectConfigDraftSummaryCollection.from_dict(
            project_config_draft_summary_collection_model_json
        )
        assert project_config_draft_summary_collection_model != False

        # Construct a model instance of ProjectConfigDraftSummaryCollection by calling from_dict on the json representation
        project_config_draft_summary_collection_model_dict = ProjectConfigDraftSummaryCollection.from_dict(
            project_config_draft_summary_collection_model_json
        ).__dict__
        project_config_draft_summary_collection_model2 = ProjectConfigDraftSummaryCollection(
            **project_config_draft_summary_collection_model_dict
        )

        # Verify the model instances are equivalent
        assert project_config_draft_summary_collection_model == project_config_draft_summary_collection_model2

        # Convert model instance back to dict and verify no loss of data
        project_config_draft_summary_collection_model_json2 = project_config_draft_summary_collection_model.to_dict()
        assert project_config_draft_summary_collection_model_json2 == project_config_draft_summary_collection_model_json


class TestModel_ProjectConfigGetResponse:
    """
    Test Class for ProjectConfigGetResponse
    """

    def test_project_config_get_response_serialization(self):
        """
        Test serialization/deserialization for ProjectConfigGetResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        project_config_metadata_last_approved_model = {}  # ProjectConfigMetadataLastApproved
        project_config_metadata_last_approved_model['is_forced'] = True
        project_config_metadata_last_approved_model['comment'] = 'testString'
        project_config_metadata_last_approved_model['timestamp'] = '2019-01-01T12:00:00Z'
        project_config_metadata_last_approved_model['user_id'] = 'testString'

        project_config_metadata_job_summary_model = {}  # ProjectConfigMetadataJobSummary
        project_config_metadata_job_summary_model['plan_summary'] = {'anyKey': 'anyValue'}
        project_config_metadata_job_summary_model['apply_summary'] = {'anyKey': 'anyValue'}
        project_config_metadata_job_summary_model['destroy_summary'] = {'anyKey': 'anyValue'}
        project_config_metadata_job_summary_model['message_summary'] = {'anyKey': 'anyValue'}
        project_config_metadata_job_summary_model['plan_messages'] = {'anyKey': 'anyValue'}
        project_config_metadata_job_summary_model['apply_messages'] = {'anyKey': 'anyValue'}
        project_config_metadata_job_summary_model['destroy_messages'] = {'anyKey': 'anyValue'}

        project_config_metadata_cra_logs_model = {}  # ProjectConfigMetadataCraLogs
        project_config_metadata_cra_logs_model['cra_version'] = 'testString'
        project_config_metadata_cra_logs_model['schema_version'] = 'testString'
        project_config_metadata_cra_logs_model['status'] = 'testString'
        project_config_metadata_cra_logs_model['summary'] = {'anyKey': 'anyValue'}
        project_config_metadata_cra_logs_model['timestamp'] = '2019-01-01T12:00:00Z'

        project_config_metadata_cost_estimate_model = {}  # ProjectConfigMetadataCostEstimate
        project_config_metadata_cost_estimate_model['version'] = 'testString'
        project_config_metadata_cost_estimate_model['currency'] = 'testString'
        project_config_metadata_cost_estimate_model['totalHourlyCost'] = 'testString'
        project_config_metadata_cost_estimate_model['totalMonthlyCost'] = 'testString'
        project_config_metadata_cost_estimate_model['pastTotalHourlyCost'] = 'testString'
        project_config_metadata_cost_estimate_model['pastTotalMonthlyCost'] = 'testString'
        project_config_metadata_cost_estimate_model['diffTotalHourlyCost'] = 'testString'
        project_config_metadata_cost_estimate_model['diffTotalMonthlyCost'] = 'testString'
        project_config_metadata_cost_estimate_model['timeGenerated'] = '2019-01-01T12:00:00Z'
        project_config_metadata_cost_estimate_model['user_id'] = 'testString'

        project_config_draft_summary_model = {}  # ProjectConfigDraftSummary
        project_config_draft_summary_model['version'] = 38
        project_config_draft_summary_model['state'] = 'testString'
        project_config_draft_summary_model['pipeline_state'] = 'testString'
        project_config_draft_summary_model['href'] = 'testString'

        project_config_auth_trusted_profile_model = {}  # ProjectConfigAuthTrustedProfile
        project_config_auth_trusted_profile_model['id'] = 'testString'
        project_config_auth_trusted_profile_model['target_iam_id'] = 'testString'

        project_config_auth_model = {}  # ProjectConfigAuth
        project_config_auth_model['trusted_profile'] = project_config_auth_trusted_profile_model
        project_config_auth_model['method'] = 'testString'
        project_config_auth_model['api_key'] = 'testString'

        project_config_compliance_profile_model = {}  # ProjectConfigComplianceProfile
        project_config_compliance_profile_model['id'] = 'testString'
        project_config_compliance_profile_model['instance_id'] = 'testString'
        project_config_compliance_profile_model['instance_location'] = 'testString'
        project_config_compliance_profile_model['attachment_id'] = 'testString'
        project_config_compliance_profile_model['profile_name'] = 'testString'

        input_variable_model = {}  # InputVariable
        input_variable_model['name'] = 'testString'
        input_variable_model['type'] = 'array'
        input_variable_model['value'] = 'testString'
        input_variable_model['required'] = True

        output_value_model = {}  # OutputValue
        output_value_model['name'] = 'testString'
        output_value_model['description'] = 'testString'
        output_value_model['value'] = 'testString'

        project_config_setting_collection_model = {}  # ProjectConfigSettingCollection
        project_config_setting_collection_model['name'] = 'testString'
        project_config_setting_collection_model['value'] = 'testString'

        project_config_definition_model = {}  # ProjectConfigDefinition
        project_config_definition_model['name'] = 'testString'
        project_config_definition_model['labels'] = []
        project_config_definition_model['description'] = 'testString'
        project_config_definition_model['authorizations'] = project_config_auth_model
        project_config_definition_model['compliance_profile'] = project_config_compliance_profile_model
        project_config_definition_model['locator_id'] = 'testString'
        project_config_definition_model['type'] = 'terraform_template'
        project_config_definition_model['input'] = [input_variable_model]
        project_config_definition_model['output'] = [output_value_model]
        project_config_definition_model['setting'] = [project_config_setting_collection_model]

        # Construct a json representation of a ProjectConfigGetResponse model
        project_config_get_response_model_json = {}
        project_config_get_response_model_json['id'] = 'testString'
        project_config_get_response_model_json['project_id'] = 'testString'
        project_config_get_response_model_json['version'] = 38
        project_config_get_response_model_json['is_draft'] = True
        project_config_get_response_model_json['needs_attention_state'] = []
        project_config_get_response_model_json['state'] = 'testString'
        project_config_get_response_model_json['pipeline_state'] = 'testString'
        project_config_get_response_model_json['update_available'] = True
        project_config_get_response_model_json['created_at'] = '2019-01-01T12:00:00Z'
        project_config_get_response_model_json['updated_at'] = '2019-01-01T12:00:00Z'
        project_config_get_response_model_json['last_approved'] = project_config_metadata_last_approved_model
        project_config_get_response_model_json['last_save'] = '2019-01-01T12:00:00Z'
        project_config_get_response_model_json['job_summary'] = project_config_metadata_job_summary_model
        project_config_get_response_model_json['cra_logs'] = project_config_metadata_cra_logs_model
        project_config_get_response_model_json['cost_estimate'] = project_config_metadata_cost_estimate_model
        project_config_get_response_model_json[
            'last_deployment_job_summary'
        ] = project_config_metadata_job_summary_model
        project_config_get_response_model_json['active_draft'] = project_config_draft_summary_model
        project_config_get_response_model_json['definition'] = project_config_definition_model

        # Construct a model instance of ProjectConfigGetResponse by calling from_dict on the json representation
        project_config_get_response_model = ProjectConfigGetResponse.from_dict(project_config_get_response_model_json)
        assert project_config_get_response_model != False

        # Construct a model instance of ProjectConfigGetResponse by calling from_dict on the json representation
        project_config_get_response_model_dict = ProjectConfigGetResponse.from_dict(
            project_config_get_response_model_json
        ).__dict__
        project_config_get_response_model2 = ProjectConfigGetResponse(**project_config_get_response_model_dict)

        # Verify the model instances are equivalent
        assert project_config_get_response_model == project_config_get_response_model2

        # Convert model instance back to dict and verify no loss of data
        project_config_get_response_model_json2 = project_config_get_response_model.to_dict()
        assert project_config_get_response_model_json2 == project_config_get_response_model_json


class TestModel_ProjectConfigInputVariable:
    """
    Test Class for ProjectConfigInputVariable
    """

    def test_project_config_input_variable_serialization(self):
        """
        Test serialization/deserialization for ProjectConfigInputVariable
        """

        # Construct a json representation of a ProjectConfigInputVariable model
        project_config_input_variable_model_json = {}
        project_config_input_variable_model_json['name'] = 'testString'
        project_config_input_variable_model_json['value'] = 'testString'

        # Construct a model instance of ProjectConfigInputVariable by calling from_dict on the json representation
        project_config_input_variable_model = ProjectConfigInputVariable.from_dict(
            project_config_input_variable_model_json
        )
        assert project_config_input_variable_model != False

        # Construct a model instance of ProjectConfigInputVariable by calling from_dict on the json representation
        project_config_input_variable_model_dict = ProjectConfigInputVariable.from_dict(
            project_config_input_variable_model_json
        ).__dict__
        project_config_input_variable_model2 = ProjectConfigInputVariable(**project_config_input_variable_model_dict)

        # Verify the model instances are equivalent
        assert project_config_input_variable_model == project_config_input_variable_model2

        # Convert model instance back to dict and verify no loss of data
        project_config_input_variable_model_json2 = project_config_input_variable_model.to_dict()
        assert project_config_input_variable_model_json2 == project_config_input_variable_model_json


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
        project_config_metadata_cost_estimate_model_json['currency'] = 'testString'
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


class TestModel_ProjectConfigMetadataCraLogs:
    """
    Test Class for ProjectConfigMetadataCraLogs
    """

    def test_project_config_metadata_cra_logs_serialization(self):
        """
        Test serialization/deserialization for ProjectConfigMetadataCraLogs
        """

        # Construct a json representation of a ProjectConfigMetadataCraLogs model
        project_config_metadata_cra_logs_model_json = {}
        project_config_metadata_cra_logs_model_json['cra_version'] = 'testString'
        project_config_metadata_cra_logs_model_json['schema_version'] = 'testString'
        project_config_metadata_cra_logs_model_json['status'] = 'testString'
        project_config_metadata_cra_logs_model_json['summary'] = {'anyKey': 'anyValue'}
        project_config_metadata_cra_logs_model_json['timestamp'] = '2019-01-01T12:00:00Z'

        # Construct a model instance of ProjectConfigMetadataCraLogs by calling from_dict on the json representation
        project_config_metadata_cra_logs_model = ProjectConfigMetadataCraLogs.from_dict(
            project_config_metadata_cra_logs_model_json
        )
        assert project_config_metadata_cra_logs_model != False

        # Construct a model instance of ProjectConfigMetadataCraLogs by calling from_dict on the json representation
        project_config_metadata_cra_logs_model_dict = ProjectConfigMetadataCraLogs.from_dict(
            project_config_metadata_cra_logs_model_json
        ).__dict__
        project_config_metadata_cra_logs_model2 = ProjectConfigMetadataCraLogs(
            **project_config_metadata_cra_logs_model_dict
        )

        # Verify the model instances are equivalent
        assert project_config_metadata_cra_logs_model == project_config_metadata_cra_logs_model2

        # Convert model instance back to dict and verify no loss of data
        project_config_metadata_cra_logs_model_json2 = project_config_metadata_cra_logs_model.to_dict()
        assert project_config_metadata_cra_logs_model_json2 == project_config_metadata_cra_logs_model_json


class TestModel_ProjectConfigMetadataJobSummary:
    """
    Test Class for ProjectConfigMetadataJobSummary
    """

    def test_project_config_metadata_job_summary_serialization(self):
        """
        Test serialization/deserialization for ProjectConfigMetadataJobSummary
        """

        # Construct a json representation of a ProjectConfigMetadataJobSummary model
        project_config_metadata_job_summary_model_json = {}
        project_config_metadata_job_summary_model_json['plan_summary'] = {'anyKey': 'anyValue'}
        project_config_metadata_job_summary_model_json['apply_summary'] = {'anyKey': 'anyValue'}
        project_config_metadata_job_summary_model_json['destroy_summary'] = {'anyKey': 'anyValue'}
        project_config_metadata_job_summary_model_json['message_summary'] = {'anyKey': 'anyValue'}
        project_config_metadata_job_summary_model_json['plan_messages'] = {'anyKey': 'anyValue'}
        project_config_metadata_job_summary_model_json['apply_messages'] = {'anyKey': 'anyValue'}
        project_config_metadata_job_summary_model_json['destroy_messages'] = {'anyKey': 'anyValue'}

        # Construct a model instance of ProjectConfigMetadataJobSummary by calling from_dict on the json representation
        project_config_metadata_job_summary_model = ProjectConfigMetadataJobSummary.from_dict(
            project_config_metadata_job_summary_model_json
        )
        assert project_config_metadata_job_summary_model != False

        # Construct a model instance of ProjectConfigMetadataJobSummary by calling from_dict on the json representation
        project_config_metadata_job_summary_model_dict = ProjectConfigMetadataJobSummary.from_dict(
            project_config_metadata_job_summary_model_json
        ).__dict__
        project_config_metadata_job_summary_model2 = ProjectConfigMetadataJobSummary(
            **project_config_metadata_job_summary_model_dict
        )

        # Verify the model instances are equivalent
        assert project_config_metadata_job_summary_model == project_config_metadata_job_summary_model2

        # Convert model instance back to dict and verify no loss of data
        project_config_metadata_job_summary_model_json2 = project_config_metadata_job_summary_model.to_dict()
        assert project_config_metadata_job_summary_model_json2 == project_config_metadata_job_summary_model_json


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
        project_config_metadata_last_approved_model_json['is_forced'] = True
        project_config_metadata_last_approved_model_json['comment'] = 'testString'
        project_config_metadata_last_approved_model_json['timestamp'] = '2019-01-01T12:00:00Z'
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


class TestModel_ProjectConfigPrototype:
    """
    Test Class for ProjectConfigPrototype
    """

    def test_project_config_prototype_serialization(self):
        """
        Test serialization/deserialization for ProjectConfigPrototype
        """

        # Construct dict forms of any model objects needed in order to build this model.

        project_config_auth_trusted_profile_model = {}  # ProjectConfigAuthTrustedProfile
        project_config_auth_trusted_profile_model['id'] = 'testString'
        project_config_auth_trusted_profile_model['target_iam_id'] = 'testString'

        project_config_auth_model = {}  # ProjectConfigAuth
        project_config_auth_model['trusted_profile'] = project_config_auth_trusted_profile_model
        project_config_auth_model['method'] = 'testString'
        project_config_auth_model['api_key'] = 'testString'

        project_config_compliance_profile_model = {}  # ProjectConfigComplianceProfile
        project_config_compliance_profile_model['id'] = 'testString'
        project_config_compliance_profile_model['instance_id'] = 'testString'
        project_config_compliance_profile_model['instance_location'] = 'testString'
        project_config_compliance_profile_model['attachment_id'] = 'testString'
        project_config_compliance_profile_model['profile_name'] = 'testString'

        project_config_input_variable_model = {}  # ProjectConfigInputVariable
        project_config_input_variable_model['name'] = 'testString'
        project_config_input_variable_model['value'] = 'testString'

        project_config_setting_collection_model = {}  # ProjectConfigSettingCollection
        project_config_setting_collection_model['name'] = 'testString'
        project_config_setting_collection_model['value'] = 'testString'

        # Construct a json representation of a ProjectConfigPrototype model
        project_config_prototype_model_json = {}
        project_config_prototype_model_json['name'] = 'testString'
        project_config_prototype_model_json['labels'] = []
        project_config_prototype_model_json['description'] = 'testString'
        project_config_prototype_model_json['authorizations'] = project_config_auth_model
        project_config_prototype_model_json['compliance_profile'] = project_config_compliance_profile_model
        project_config_prototype_model_json['locator_id'] = 'testString'
        project_config_prototype_model_json['input'] = [project_config_input_variable_model]
        project_config_prototype_model_json['setting'] = [project_config_setting_collection_model]

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
        project_config_resource_model_json[
            'resource_crn'
        ] = 'crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::'
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
        project_config_resource_model[
            'resource_crn'
        ] = 'crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::'
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


class TestModel_ProjectConfigSettingCollection:
    """
    Test Class for ProjectConfigSettingCollection
    """

    def test_project_config_setting_collection_serialization(self):
        """
        Test serialization/deserialization for ProjectConfigSettingCollection
        """

        # Construct a json representation of a ProjectConfigSettingCollection model
        project_config_setting_collection_model_json = {}
        project_config_setting_collection_model_json['name'] = 'testString'
        project_config_setting_collection_model_json['value'] = 'testString'

        # Construct a model instance of ProjectConfigSettingCollection by calling from_dict on the json representation
        project_config_setting_collection_model = ProjectConfigSettingCollection.from_dict(
            project_config_setting_collection_model_json
        )
        assert project_config_setting_collection_model != False

        # Construct a model instance of ProjectConfigSettingCollection by calling from_dict on the json representation
        project_config_setting_collection_model_dict = ProjectConfigSettingCollection.from_dict(
            project_config_setting_collection_model_json
        ).__dict__
        project_config_setting_collection_model2 = ProjectConfigSettingCollection(
            **project_config_setting_collection_model_dict
        )

        # Verify the model instances are equivalent
        assert project_config_setting_collection_model == project_config_setting_collection_model2

        # Convert model instance back to dict and verify no loss of data
        project_config_setting_collection_model_json2 = project_config_setting_collection_model.to_dict()
        assert project_config_setting_collection_model_json2 == project_config_setting_collection_model_json


class TestModel_ProjectDefinitionResponse:
    """
    Test Class for ProjectDefinitionResponse
    """

    def test_project_definition_response_serialization(self):
        """
        Test serialization/deserialization for ProjectDefinitionResponse
        """

        # Construct a json representation of a ProjectDefinitionResponse model
        project_definition_response_model_json = {}
        project_definition_response_model_json['name'] = 'testString'
        project_definition_response_model_json['description'] = 'testString'
        project_definition_response_model_json['destroy_on_delete'] = True

        # Construct a model instance of ProjectDefinitionResponse by calling from_dict on the json representation
        project_definition_response_model = ProjectDefinitionResponse.from_dict(project_definition_response_model_json)
        assert project_definition_response_model != False

        # Construct a model instance of ProjectDefinitionResponse by calling from_dict on the json representation
        project_definition_response_model_dict = ProjectDefinitionResponse.from_dict(
            project_definition_response_model_json
        ).__dict__
        project_definition_response_model2 = ProjectDefinitionResponse(**project_definition_response_model_dict)

        # Verify the model instances are equivalent
        assert project_definition_response_model == project_definition_response_model2

        # Convert model instance back to dict and verify no loss of data
        project_definition_response_model_json2 = project_definition_response_model.to_dict()
        assert project_definition_response_model_json2 == project_definition_response_model_json


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

        project_definition_response_model = {}  # ProjectDefinitionResponse
        project_definition_response_model['name'] = 'testString'
        project_definition_response_model['description'] = 'testString'
        project_definition_response_model['destroy_on_delete'] = True

        # Construct a json representation of a ProjectSummary model
        project_summary_model_json = {}
        project_summary_model_json[
            'crn'
        ] = 'crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::'
        project_summary_model_json['created_at'] = '2019-01-01T12:00:00Z'
        project_summary_model_json['cumulative_needs_attention_view'] = [cumulative_needs_attention_model]
        project_summary_model_json['cumulative_needs_attention_view_error'] = True
        project_summary_model_json['id'] = 'testString'
        project_summary_model_json['location'] = 'testString'
        project_summary_model_json['resource_group'] = 'testString'
        project_summary_model_json['state'] = 'testString'
        project_summary_model_json['event_notifications_crn'] = 'testString'
        project_summary_model_json['definition'] = project_definition_response_model

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


# endregion
##############################################################################
# End of Model Tests
##############################################################################
