# Codebuild setup for bdp

1. Set up so that we've got the proper role to do the things we need to do
2. create a docker container that can be given env variables and will run cloudformation to set up new projects

  - ecr repo? create it
  - code build could be bastardized to simply promote ecr images across environ
  - run docker container event-api to report things that resides in the buildspec-override


GITHUB
  - Create a single use token for bdpuser from github
  - a simple github builder job that will handle docker artifact creation
    Sets us up with defaults:
      - Role
      - multiple github locations for overrides
      - source-location: https://login-user-name:personal-access-token@github.com/repo-owner-name/repo-name.git
