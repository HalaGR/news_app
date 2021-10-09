pipeline {

	agent any //run code with agent slave
		
		stages {
		
			stage("clone") { // stage Build
			
				steps {
					git branch: 'main', url: 'https://github.com/HalaGR/news_app.git' //clone repo
          			
				}
			}
			stage("Build"){
			    steps{
                    sh "pip install -r requirements.txt"
				    sh "python app.py"
			    }
			}
        }

			
    }