function PageTemplate({ title, description }) {
  return (
    <div
      style={{
        padding: "40px",
        color: "white",
      }}
    >
      <h1 style={{ fontSize: "38px", marginBottom: "10px" }}>
        {title}
      </h1>

      <p
        style={{
          color: "#9fb3c8",
          fontSize: "18px",
          marginBottom: "30px",
        }}
      >
        {description}
      </p>

      <div
        style={{
          background: "#10243d",
          borderRadius: "20px",
          padding: "30px",
          minHeight: "400px",
        }}
      >
        <h3>Module Ready</h3>

        <p>
          This module is integrated into the HealthAI Hospital Management
          System and is ready for backend integration.
        </p>
      </div>
    </div>
  );
}

export default PageTemplate;