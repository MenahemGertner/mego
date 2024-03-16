import { links } from "../../data/links";
import "./navbar.css";

export default function Navbar() {
  return (
    <nav className="container">
      <ul className="link-list">
        {links.map((item) => (
          <NavItem link={item} />
        ))}
      </ul>
    </nav>
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
