
import React, { useEffect, useState } from "react";
import axios from "axios";

import { Container, Row, Col, Card, Nav, Navbar } from "react-bootstrap";
import { NavLink } from "react-router-dom";
import { FaTrophy } from "react-icons/fa"; // Trophy icon
import "./BadgesPage.css"; // Import custom CSS

const BadgesPage = () => {
  const [student, setStudent] = useState(null);

  // State to track which badge image is hovered
  const [hoveredBadgeIndex, setHoveredBadgeIndex] = useState(null);

  useEffect(() => {
    axios
      .get("/api/badges", { withCredentials: true })
      .then((response) => {
        setStudent(response.data);
      })
      .catch((error) => console.error("Error fetching student data:", error));
  }, []);

  if (!student) {
    return <div>Loading...</div>;
  }

  return (
    <>
      {/* Navigation Bar */}
      <Navbar expand="lg" className="navbar-asu shadow-sm">
        <Container>
          <Navbar.Brand className="navbar-brand">
            AchievementHub
          </Navbar.Brand>
          <Navbar.Toggle aria-controls="navbarNav" />
          <Navbar.Collapse id="navbarNav">
            <Nav className="ms-auto">
              <Nav.Link as={NavLink} to="/badges" className="nav-link-asu">
                My Badges
              </Nav.Link>
              <Nav.Link as={NavLink} to="/" className="nav-link-asu">
                Logout
              </Nav.Link>
            </Nav>
          </Navbar.Collapse>
        </Container>
      </Navbar>

      {/* Badges Section */}
      <Container className="mt-5">
        <h1 className="fw-bold text-center">Badges Earned</h1>
        <Row className="mt-4">
          {student.badges.map((badge, index) => (
            <Col md={4} className="mb-4" key={index}>
              <Card className="h-100 shadow-sm badge-card">
                {/* Trophy Icon and Count */}
                <div className="trophy-badge">
                  <FaTrophy className="trophy-icon" /> ×{badge.trophyCount}
                </div>
                <div className="image-container">
                  <Card.Img
                    src={`http://127.0.0.1:5000${badge.image}`}
                    alt={badge.title}
                    className={`front-image ${
                      hoveredBadgeIndex === index ? "rotate" : ""
                    }`}
                    onMouseEnter={() => setHoveredBadgeIndex(index)} // Set hovered badge
                    onMouseLeave={() => setHoveredBadgeIndex(null)} // Reset hover
                  />
                  <Card.Img
                    src={`http://127.0.0.1:5000${badge.secondaryImage}`}
                    alt={`${badge.title} Back`}
                    className={`back-image ${
                      hoveredBadgeIndex === index ? "rotate" : ""
                    }`}
                    onMouseEnter={() => setHoveredBadgeIndex(index)} // Set hovered badge
                    onMouseLeave={() => setHoveredBadgeIndex(null)} // Reset hover
                  />
                </div>
                <Card.Body className="text-center">
                  <Card.Title>{badge.title}</Card.Title>
                </Card.Body>
              </Card>
            </Col>
          ))}
        </Row>
      </Container>
    </>
  );
};

export default BadgesPage;
