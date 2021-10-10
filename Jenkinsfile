pipeline {

	agent any //run code with agent slave
		
		stages {
		    stage("kill if still running"){
		        steps{
		            sh 'jps | grep app | awk \'{print "kill -9" $1}\' | bash -x | true' //if app still running kill it
		        }
		    }
		
			stage("clone") { // stage Build
			
				steps {
					git branch: 'main', url: 'https://github.com/HalaGR/news_app.git' //clone repo
          			
				}
			}
			stage("Build"){
			    steps{
				   sh 'pip3 install -r requirements.txt'
				   sh 'JENKINS_NODE_COOKIE=dontKillMe nohup python3 app.py &' //run app in BG
			    }
			}
			stage("send slack"){
			    steps{
			        slackSend channel: 'jenkins', message: 'hello from jenkins!!', teamDomain: 'forsa-hq', tokenCredentialId: 'slack' // send message when built 
			
			    }
			}
        }

			
}
