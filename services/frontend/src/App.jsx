import './App.css'

function App() {
  const services = [
    {
      name: 'API Gateway',
      description: 'Central entry point for routing frontend requests to backend microservices.',
      status: 'Operational',
    },
    {
      name: 'Auth Service',
      description: 'Handles user authentication, login simulation, and token validation flow.',
      status: 'Operational',
    },
    {
      name: 'Patient Service',
      description: 'Manages patient profiles, records, and sample healthcare data.',
      status: 'Operational',
    },
    {
      name: 'Appointment Service',
      description: 'Supports appointment scheduling, consultation tracking, and care coordination.',
      status: 'Operational',
    },
    {
      name: 'Notification Service',
      description: 'Simulates patient alerts, appointment reminders, and system notifications.',
      status: 'Operational',
    },
    {
      name: 'AI Service',
      description: 'Provides simulated triage and patient risk scoring for platform demonstration.',
      status: 'Operational',
    },
  ]

  const stats = [
    { value: '6', label: 'Microservices' },
    { value: '3', label: 'Environments' },
    { value: '24/7', label: 'Monitoring Ready' },
    { value: 'GitOps', label: 'Deployment Model' },
  ]

  return (
    <main className="app">
      <nav className="navbar">
        <div className="brand">
          <div className="brand-icon">+</div>
          <div>
            <h1>CareLink AI</h1>
            <p>Cloud-native healthcare platform</p>
          </div>
        </div>

        <div className="nav-links">
          <a href="#services">Services</a>
          <a href="#platform">Platform</a>
          <a href="#devops">DevOps</a>
        </div>
      </nav>

      <section className="hero">
        <div className="hero-content">
          <p className="eyebrow">Healthcare • AI • DevOps • Kubernetes</p>

          <h2>
            <span className="hero-title-brand">CareLink AI</span>
            <br />
            Intelligent healthcare operations for modern medical teams.
          </h2>

          <p className="hero-text">
            A production-style healthcare platform designed to demonstrate
            enterprise DevOps practices including microservices, Docker,
            Kubernetes, CI/CD, GitOps, monitoring, logging, autoscaling,
            and cloud deployment.
          </p>

          <div className="hero-actions">
            <a href="#services" className="primary-button">View Services</a>
            <a href="#devops" className="secondary-button">Explore DevOps Stack</a>
          </div>
        </div>

        <div className="hero-panel">
          <div className="panel-header">
            <span className="pulse"></span>
            <p>Platform Status</p>
          </div>

          <h3>All core services operational</h3>

          <div className="health-card">
            <span>Care coordination</span>
            <strong>Active</strong>
          </div>

          <div className="health-card">
            <span>AI triage simulation</span>
            <strong>Ready</strong>
          </div>

          <div className="health-card">
            <span>Microservice monitoring</span>
            <strong>Enabled</strong>
          </div>
        </div>
      </section>

      <section className="stats-section">
        {stats.map((item) => (
          <article className="stat-card" key={item.label}>
            <h3>{item.value}</h3>
            <p>{item.label}</p>
          </article>
        ))}
      </section>

      <section className="section" id="services">
        <div className="section-heading">
          <p className="eyebrow">Microservices Architecture</p>
          <h2>Independent services designed for scalable healthcare delivery.</h2>
          <p>
            Each service is containerized independently and prepared for Kubernetes
            deployment, monitoring, scaling, and GitOps-based release management.
          </p>
        </div>

        <div className="service-grid">
          {services.map((service) => (
            <article className="service-card" key={service.name}>
              <div className="service-top">
                <h3>{service.name}</h3>
                <span>{service.status}</span>
              </div>
              <p>{service.description}</p>
            </article>
          ))}
        </div>
      </section>

      <section className="platform-section" id="platform">
        <div className="platform-card">
          <p className="eyebrow">Patient Journey</p>
          <h2>From access to care coordination.</h2>

          <div className="timeline">
            <div>
              <span>01</span>
              <p>Patient accesses the frontend dashboard.</p>
            </div>
            <div>
              <span>02</span>
              <p>Requests are routed through the API Gateway.</p>
            </div>
            <div>
              <span>03</span>
              <p>Backend services manage authentication, records, and appointments.</p>
            </div>
            <div>
              <span>04</span>
              <p>AI service provides simulated triage and risk scoring support.</p>
            </div>
          </div>
        </div>

        <div className="notice-card">
          <h3>Responsible AI Notice</h3>
          <p>
            AI responses in this project are simulated for DevOps and platform
            engineering demonstration only. They are not medical advice, diagnosis,
            or treatment recommendations.
          </p>
        </div>
      </section>

      <section className="devops-section" id="devops">
        <div>
          <p className="eyebrow">DevOps Engineering</p>
          <h2>Built to demonstrate real DevOps workflows.</h2>
          <p>
            The platform is designed for infrastructure automation, container
            orchestration, CI/CD, GitOps delivery, observability, incident response,
            and cost-conscious AWS deployment.
          </p>
        </div>

        <div className="stack-list">
          <span>AWS</span>
          <span>Terraform</span>
          <span>Amazon EKS</span>
          <span>Docker</span>
          <span>Kubernetes</span>
          <span>Helm</span>
          <span>Jenkins</span>
          <span>Argo CD</span>
          <span>Prometheus</span>
          <span>Grafana</span>
          <span>Loki</span>
          <span>Alertmanager</span>
        </div>
      </section>
    </main>
  )
}

export default App