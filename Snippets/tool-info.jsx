export const ToolInfo = ({ icon, name, children }) => {
  return (
    <div
      className="not-prose"
      style={{
        display: "flex",
        alignItems: "flex-start",
        gap: "16px",
        margin: "16px 0",
      }}
    >
      <img
        src={icon}
        alt={`${name} button`}
        style={{
          width: "40px",
          height: "40px",
          objectFit: "contain",
          flexShrink: 0,
        }}
      />

      <div>
        <strong>{name}</strong>
        <div style={{ marginTop: "4px" }}>{children}</div>
      </div>
    </div>
  );
};