# Use specific Python version for better reproducibility
FROM python:3.13-slim-bullseye

# Add metadata
LABEL maintainer="Emmanuel BRUNO <emmanuel.bruno@univ-tln.fr>"
LABEL description="Multi-architecture demo container"
LABEL version="0.1.0"

# Create non-root user
RUN groupadd -r appuser && useradd -r -g appuser appuser

# Set working directory and switch to non-root user
WORKDIR /app

# Copy application with correct permissions
COPY --chown=appuser:appuser app.py .

# Set file permissions
RUN chmod 550 /app/app.py

# Switch to non-root user
USER appuser

# Use exec form of CMD
CMD ["python", "-u", "app.py"]