run:
	@echo "🔍 Checking if Docker is running..."
	@if ! docker info >/dev/null 2>&1; then \
		echo "🚨 Docker is not running! Please start Docker and try again."; \
		exit 1; \
	fi
	@echo "✅ Docker is running!"

	@echo "🔍 Checking for .env file..."
	@if [ ! -f .env ]; then \
		echo "🚨 .env file is missing! Creating a template..."; \
		echo "REDDIT_CLIENT_ID=" > .env; \
		echo "REDDIT_CLIENT_SECRET=" >> .env; \
		echo "REDDIT_USER_AGENT=" >> .env; \
		echo "⚠️  Please fill in the missing values in the .env file from your Reddit app."; \
		exit 1; \
	fi
	@echo "✅ .env file found!"

	@echo "🔍 Validating .env keys..."
	@if ! grep -q 'REDDIT_CLIENT_ID=' .env || \
	    ! grep -q 'REDDIT_CLIENT_SECRET=' .env || \
	    ! grep -q 'REDDIT_USER_AGENT=' .env; then \
		echo "🚨 Missing required keys in .env file!"; \
		echo "⚠️  Ensure the .env file contains the following keys:"; \
		echo "    REDDIT_CLIENT_ID=your_client_id"; \
		echo "    REDDIT_CLIENT_SECRET=your_client_secret"; \
		echo "    REDDIT_USER_AGENT=your_user_agent"; \
		exit 1; \
	fi
	@echo "✅ All required keys are present in .env!"

	@echo "🚀 Starting application with Docker Compose..."
	@docker-compose up --build
