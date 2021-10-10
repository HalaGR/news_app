pipeline {

	agent any //run code with agent slave
		
		stages {
		    stage("kill if still running"){
		        steps{
		            sh 'jps | grep app | awk \'{print "kill -9" $1}\' | bash -x | true'
		        }
		    }
		
			stage("clone") { // stage Build
			
				steps {
					git branch: 'main', url: 'https://github.com/HalaGR/news_app.git' //clone repo
          			
				}
			}
			stage("Build"){
			    steps{
			       // sh 'python3 -v'
				   sh 'pip3 install -r requirements.txt'
				   //sh 'nohub python3 app.py &'
				   sh 'BUILD_ID=dontKillMe nohup python3 app.py &'
			    }
			}
        }

			
}
