import { links } from "../../data/links";
import "./navbar.css";

export default function Navbar() {
  return (
    <div className="container">
      <ul className="link-list">
        {links.map((link) => (
          <NavItem link={link} />
        ))}
      </ul>
    </div>
  );
}

function NavItem({ link }) {
  return (
    <li className="list-item">
      <a className="link" href={link.href}>
        {link.title}
      </a>
    </li>
  );
}
