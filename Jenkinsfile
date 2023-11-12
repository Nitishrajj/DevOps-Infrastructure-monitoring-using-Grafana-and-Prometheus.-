#Writeyourpipelinehere
pipeline {
    agent any

    stages {
        #you can write different stages here
        stage('Remote SSH - 1') {
            steps {
                script {
                    def remote = [:]
                    remote.name = 'remotehostname'
                    remote.host = 'remotehostipadd'
                    remote.user = 'remotehostuser'
                    remote.password = 'remotehostpassword'
                    remote.allowAnyHosts = true

                    sshCommand remote: remote, command: "python test.py"
                }
            }
        }
        stage('Remote SSH - 2') {
            steps {
                script {
                    def remote = [:]
                    remote.name = 'remotehostname'
                    remote.host = 'remotehostipadd'
                    remote.user = 'remotehostuser'
                    remote.password = 'remotehostpassword'
                    remote.allowAnyHosts = true

                    sshCommand remote: remote, command: "python test.py"
                }
            }
        }
    }
}