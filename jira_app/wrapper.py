from __future__ import unicode_literals
from jira.client import JIRA
from rest_framework.response import Response
from rest_framework import status


class jirawrapper(object):

    def __init__(self):
        self.jira = self.__authenticate()

    def __authenticate(self):
        options = {'server': 'https://gvmani155.atlassian.net'}
        jira = JIRA(options, basic_auth=('gvmani155@gmail.com', '9494123456a!'))
        return jira

    def project_creation(self,data):
        try:
            project = self.jira.create_project(name=data['name'], key=data['key'], template_name=data['template_name'])
            data = []
            data.append({'name':project['projectName'],'key':project['projectKey'],'id':project['projectId']})
            return data
        except Exception as e:
            return "Error Occured - ",str(e.text)

    def get_all_projectlist(self):
        project = self.jira.projects()
        return project


    def adding_component(self,data):
        try:
            Components = self.jira.create_component(name=data['name'],project=data['project'],description=data['description'],assigneeType=data['assigneeType'])
            return Components
        except Exception as e:
            return "Error Occured - ",str(e.text)

    def get_all_components_of_project(self):
        comps = self.jira.project_components('MH')
        return comps


    def issue_creation(self,data):
        try:
            project = self.jira.create_issue(project=data['project']['key'], summary=data['summary'],description=data['description'],issuetype=data['issuetype'],components=data['components'])
            return project
        except:
            return Response("Issue Is Not Created Due To Some Bad Request", status=status.HTTP_400_BAD_REQUEST)
    
    def get_all_issues(self):
        issue = self.jira.search_issues('issuetype=Task')
        return issue
        # issue = self.jira.search_issues('issuetype=Bug')
        # issue = self.jira.search_issues('issuetype=Story')

    def subtask_creation(self,data):
        try:
            sub_task = self.jira.create_issue(project=data['project'], summary=data['summary'],description=data['description'],issuetype=data['issuetype'],parent=data['parent'],labels=data['labels'])
            return sub_task
        except:
            return Response("Sub_task Is Not Created Due To Some Bad Request", status=status.HTTP_400_BAD_REQUEST)


    def get_all_sub_tasks(self):
        project_issues = self.jira.search_issues('issuetype=Bug')
        # project_issues = self.jira.search_issues('issuetype=Task')
        # project_issues = self.jira.search_issues('issuetype=Story')
        return project_issues

    def creating_sprint(self,data):
        try:
            Sprints = self.jira.create_sprint(name=data['name'],board_id=data['board_id'])#,startDate=data['None'],endDate=data['None'])
            return Sprints
        except:
            return Response("Sprint Is Not Created Due To Some Bad Request", status=status.HTTP_400_BAD_REQUEST)


    def get_all_sprints(self):
        sprint_list = self.jira.sprints(board_id=2)
        return sprint_list


    def adding_comment(self,data):
        try:
            comment = self.jira.add_comment(issue=data['issue'],body=data['body'])
            return comment
        except:
            return Response("Comment Is Not Added Due To Some Bad Request", status=status.HTTP_400_BAD_REQUEST)


    def get_all_Sprint_issues_of_project(self):
        sprintlist = self.jira.search_issues('issuetype=Story')
        return sprintlist


    def move_issues(self):
        ai = self.jira.move_to_backlog(issue_keys='SSP-24')
        return ai